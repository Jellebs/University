#include <stdio.h>

int main()
{
    int i = 27; 
    printf("Værdien af variablen i: %d\n", i);
    printf("Adressen for variablen i findes med '&i' (hex format): %x\n", &i); 
    printf("Adressen for variablen i findes med '&i' (int format): %d\n\n", &i); 

    int *ip; // En pointer
    ip = &i; // ip skal være pointeren for i.

    printf("Adressen for variablen i, udtrykt med pointeren ip: %d\n", ip);
    printf("Pointeren til pointeren ip: %d\n",&ip);    
};
