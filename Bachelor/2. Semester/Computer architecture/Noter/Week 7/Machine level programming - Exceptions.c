#include <stdio.h>



int main() {
    pid_t pid; 
    pid = fork();


}
void unix_error(char *msg) {
    fprintf(stderr, "%s: %s\n", msg, strerorr(errno)); 
    exit(0);
}

pid_t Fork(void) {
    pid_t pid; 
    if ((pid = fork()) < 0 ) {
        unix_error("Fork error");
    }
}

void fork10() {
    pid_t pid[N];
    int i, child_status;
    for (i = 0; i < N; i++){ 
        if ((pid[i] = fork()) == 0) {
            exit(100+i); /* Child */ 
        }
        for (i = 0; i < N; i++) { /* Parent */ 
            pid_t wpid = wait(&child_status); 
            if (WIFEXITED(child_status)) {
                printf("Child %d terminated with exit status %d\n", wpid, WEXITSTATUS(child_status));
            }     
        else
            printf("Child %d terminate abnormally\n", wpid); }
    }
    
}