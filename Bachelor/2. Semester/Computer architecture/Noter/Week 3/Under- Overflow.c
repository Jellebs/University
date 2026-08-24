#include <stdio.h> 
#include <limits.h> 
int add(int a, int b) { // Adding numbers 
    return a + b;
}

int operat(unsigned int x, unsigned int y) { // Exercise. 
    unsigned int t = x << 5;
    t = t - x;
    y = y >> 3; 
    return t + y; 
}


int main() {
    printf("%d\n", add(INT_MIN, INT_MIN));
    printf("%d\n", add(INT_MIN, INT_MAX)); 
    printf("%d\n", add(INT_MAX, INT_MAX));

}