/*
Original Source: http:// www.sfu.ca/~reilande/
(lightly edited for clarity)

Travel Agent Simulation: by Steve Reilander

The program simulates a travel agency, where multiple agents book tickets 
to the same flight. The agents are child processes created by the fork() function.

A flight has fixed number of seats, each process has access to the seats and can 
book them. The program will protect the seats from other travel agents to avoid
double-booking. This is accomplished using Inter-Process Communication (IPC) with pipes.

Heavy commenting on sections here as this is intended as a helpful guide
for people learning about fork() and pipes.
*/


#include <iostream>     // For writing to the console
#include <sys/types.h>  // Data type declarations like the process ID (pid_t)
#include <unistd.h>     // Functions for managing processes (fork, getpid, ...)
#include <sys/wait.h>   // For sleeping the agents after booking a ticket

// For calling functions from the C++ standard library without the 'std::' prefix
using namespace std;

// Control the number of travel agents - easy to change for test runs
const int NUMBER_OF_CHILDREN = 5;

// Easy to change number of seats for different test runs
const int INITIAL_NUMBER_OF_SEATS = 15;


// The program uses the variable 'seats_left' to know when the flight is totally
// booked and time to shut down.  The algorithm for this requires
// seats_left = ( 2 - number of children) to know it has completed.
// This value is highly dependent on what the children do when they notice there are
// no more seats.
const int PARENT_CONTROL = (2 - NUMBER_OF_CHILDREN);

// Required as a paramater for sending ints down a pipe
const int SIZE_OF_INT = sizeof(int);


// Delcare the travel agent function ahead, we will implement it after main()
void travel_agent(int *child_to_parent, int *parent_to_child, int id);

int main()
{
    // Create 2 pipes to talk from children -> parent and parent -> children
    // create an int array of size 2, then declare a pipe with the pipe() function
    // using the array as a parameter as so:
    int child_to_parent[2];
    int parent_to_child[2];
    pipe(child_to_parent);
    pipe(parent_to_child);

    // Array of Process IDs of the child processes, used when the children are shut down
    // 'pid_t' is the variable type needed
    pid_t agent_pids[NUMBER_OF_CHILDREN];

    // Number of available seats 
    int seats_left = INITIAL_NUMBER_OF_SEATS;

    // For keeping track if we are in the parent of child after the fork() call
    int pid;

    // Create the travel agents
    for (int i = 0; i < NUMBER_OF_CHILDREN; i++)
    {
        // The Fork
        pid = fork();

        // Error catching: pid < 0 is returned when there is a failure
        if (pid < 0)
        {
            cout << "OH SNAP! Child " << i << " failed" << endl;
            return -1;
        }

        // Fork succeeded

        // !!!!!!!!!!!!
        // Everything after this point runs in both the parent and the child process!
        // We can run specific code blocks only in the parent or the child by checking
        // the returned Process ID.

        // If the pid is 0, we are in the child process. Output some useful
        // information, and then start running the travel agent function.
        if (pid == 0)
        {
            // output to show when children are created
            cout << " [Agent " << i << "] created, PID= " << getpid() << endl;

            // Start a travel agent function 
            travel_agent(child_to_parent, parent_to_child, i);

            // It is very important to break the children from the for loop. Otherwise they
            // will continue the for loop and create more children themselves!
            break;
        }
        // If the pid is greater than 0, we are in the parent and 'pid' stores the child process ID. 
        // We need to store these IDs in the parent, so we can shut down the children at the end.
        else
        {
            // Store the child's process ID
            agent_pids[i] = pid;
        }

    } // end child creation for loop



    // Parent and control function. Check for pid=0 so this only runs in the parent!
    if (pid > 0)
    { 
        // We don't know how long it will take for the agents to book the whole plane. 
        // Start an infinite loop that we can exit by settting the 'loop' variable to false
        bool loop = true;
        while (loop)
        {
            // This is the IPC part of the main function.  we want to make sure that only one travel
            // agent can read the number of seats left at a time.  We also need to make sure that only
            // one agent can book a seat at a time.  If we don't protect the seats_left variable, we will
            // be able to over book the flight, which we want to avoid.
            // We accomplish the protection of the critical section with pipes. When a process
            // reads from a pipe, if there is nothing in it to read, it will wait for something
            // to be written into it before continuing.  When something is written into a pipe, that
            // data can only be read once and only by one process.  If there are 5 processes all waiting
            // to read the same pipe and then there is one write to the pipe, only ONE of the 5
            // waiting processes will get to read what was written and continue, while the other 4 will
            // keep waiting.
            // We will start by writing the current seats_left variable into the parent->child pipe.
            // and in the travel agent function, they will start by reading from the parent->child pipe.
            // the travel agent will, after reading from the child->parent pipe, book a seat, and then
            // write the value of the remaining seats back to the parent by the child->parent pipe.
            // this is basically forcing all of the travel agents to read the seats_left variable one at a time
            // and doesn't allow the the main function to write the seats_left while a travel agent is booking
            // a seat.
            
            // Write to the children seats_left and then wait for a response from the children
            cout << "[Parent] Announcing " << seats_left << " seats left to agents" << endl;
            write(parent_to_child[1], &seats_left, SIZE_OF_INT);
            read(child_to_parent[0], &seats_left, SIZE_OF_INT);
            
            // If there are seats left, output how many are left
            if (seats_left > 0){
                cout << "[Parent] Seats left: " << seats_left << endl;
                // Sleep for random time between 1-2 seconds 
                // (so we, terribly slow humans can follow in the console what's happening step-by-step)
                usleep(1000000 + (rand() % 1000000));
            }
            else if(seats_left == 0){
                cout << "-------------------------------------------------------------------------------------" << endl
                     << "[Parent] NO MORE SEATS LEFT! Wait for all agents to realize this and stop listening." << endl
                     << "-------------------------------------------------------------------------------------" << endl;
            }

            // When seats_left < PARENT_CONTROL, all children have finished their loops
            if (seats_left < PARENT_CONTROL)
            {
                // Exit the loop
                loop = false;
                cout << "[Parent] Exit loop. PID: " << getpid() << endl;
            }
        } // end while

        // Here is a solution to an interesting problem, known as Zombies.  A zombie is a child process that
        // continues running after the parent has terminated.  Without this next for loop, it is possible to get
        // zombies.  This is what waitpid is for.  waitpid will force the current process to wait for another process
        // to terminate before continuing.  in the for loop, we force main to wait for each of its children to terminate
        // before continuing.
        for (int i = 0; i < NUMBER_OF_CHILDREN; i++)
        {
            cout << "[Parent] Waiting Agent PID=" << agent_pids[i] << " to finish..." << endl;
            waitpid(agent_pids[i], NULL, 0);
            cout << "[Parent] Agent PID=" << agent_pids[i] << " has shut down." << endl;
        }

    } // end parent-only code

    // This is the joined section of the program. All processes, parent and children, will run this section
    // after the waitpid code. the last line shown will always be "There are no ZOMBIES".  If we remove the waitpid
    // section it will be possible to see output ater "There are no ZOMBIES", and it will even be possible to see
    // output after a new prompt line.
    if (pid > 0){
        cout << "[Parent] There are no ZOMBIES!" << endl;
    }

    cout << "Process " << getpid() << " exiting." << endl;

    return 0;
}

void travel_agent(int *child_to_parent, int *parent_to_child, int id)
{
    // Start listening in loop that we can end when we want
    bool loop = true;
    // Declare seats_left as a local variable
    int seats_left = 0;
    while (loop)
    {
        // wait for parent to write, then process seats left
        read(parent_to_child[0], &seats_left, SIZE_OF_INT);
        
        // If there are seats left, write out how many and then 'book' a seat
        // declare thread number, and pid
        if (seats_left > 0)
        {
            cout << " [Agent #" << id << "] There are " << seats_left << " seat(s), booking one!" << endl;
            seats_left--;

            // if we booked the last seat, stop looping
            if (seats_left == 0){
                loop = false;
            }

            // tell the parent how many seats are left and get off the CPU (don't be a hog)
            write(child_to_parent[1], &seats_left, SIZE_OF_INT);
            
        }

        // If there are no seats left on the plane, stop looping and write back to the parent
        else
        {
            loop = false;
            seats_left--;
            write(child_to_parent[1], &seats_left, SIZE_OF_INT);
        }
    }
}