#include <stdio.h>

void swap(long *xp, long *yp) {
    long t0 = *xp;
    long t1 = *yp;
    *xp = t1;
    *yp = t0;
}
long arith(long x, long y, long z) {
    long t1 = x+y;
    long t2 = z+t1;
    long t3 = x+4;
    long t4 = y * 48; 
    long t5 = t3 + t4; 
    long rval = t2 * t5; 
    return rval;
}
// Conditional coding
int gt(long x, long y) {
    if (x < y) { // cmpq %rsi, %rdi # x: y
    //jle .L4 # less or equal, måske vurderes de bagvendt så y < x, hvilket er her. Ellers er det en fejl, og, at der skal stå jg, greater than
    } else { //.L4 

    }
    return x > y;
    
    
}

int main() {
    long a = 10; 
    long b = 5;
    swap(&a,&b);
    printf("a: %ld & b: %ld", a, b);
}