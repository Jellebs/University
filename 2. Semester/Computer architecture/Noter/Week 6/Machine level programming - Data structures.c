#include <stdio.h>

// %rax bruges som standard som return value
// %rsp har en stack af pointers og viser hvilken operation i stacken der skal kaldes næst

#define ZLEN 5
typedef int zip_dig[ZLEN];

int get_digit(zip_dig z, int digit) {
    return z[digit];
}

void zincr(zip_dig z) {
    size_t i;
    for (i = 0; i < ZLEN; i++) {
        printf("%d", z[i]++);
        printf("\n"); 
        
    }
}

int main(){
    zip_dig cmu = { 1, 5, 2, 1, 3 };    
    zincr(cmu);
    size_t i; 
    for (i = 0; i < ZLEN; i++) {
        printf("\n");
        int digit = get_digit(cmu, i); 
        printf("%d", digit); 
    }
    
    
}



