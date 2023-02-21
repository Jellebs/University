#include <stdio.h>
#include <string.h>

void helloWorld() {
    printf("Hello World!\n");
}

int adder(int x, int y) { return x + y; }

void besvarelse1() {
    int val = adder(2, 3);
    printf("%d", val); 
}
void omvendOrd(char streng[], char *omvendt[]) { //printf("%d", strrev("")) ville have gjort det samme. Denne teknik kan dog bruges til næste besvarelse.
    int i; 
    int MAKS = strlen(streng) - 1;
    printf("%d\n", MAKS);
    printf("%s\n", streng);
    printf("%s\n", *omvendt);

    for (i = 0; i <= MAKS; i ++) {
        omvendt[i] = &streng[MAKS - i];
        printf("i: %d\n", i);
        printf("Ord: %s\n", streng);
        printf("Omvendt: %s\n", *omvendt);
    }
    
    //omvendt = &omvendtOrd;    
}

void besvarelse2() {
    char ord[] = { "Skisportsudoever" };
    char *omvendt[] = { "" }; 
    omvendOrd(&ord[0], &omvendt[0]);
    //printf("Ord: %s\n", ord); 
    //printf("Omvendt: %s\n", omvendt);

}

int main(void) {
    //besvarelse1();
    
    besvarelse2();
}

