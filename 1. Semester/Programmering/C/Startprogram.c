#include <stdio.h>
#include <string.h>

int x = 27;
char mitForBogstav = 'A';
char mitDyr[] = "abe"; 

int main()
{
    printf("Velkommen til mit første C-Program\n");
    printf("x=%d\n", x); 

    strcpy(mitDyr, "Løve");
    printf("\nMit kæledyr er en %s", mitDyr); 
    return(0);
}; 
// ‰d - int 
// %s - liste af characters. 


