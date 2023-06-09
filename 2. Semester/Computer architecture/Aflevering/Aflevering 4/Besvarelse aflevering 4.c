#include <stdlib.h> // For malloc
#include <stdio.h> // For printf

// Malloc: 10.55 - 11.36 
// Calloc: 12.48.45 - 13.45 

int main(){
    printf("Integers are %d bytes in this computer\n", (int) sizeof(int));
    unsigned long long i=0;
    while(1){
        // Try to allocate 'i' million ints
        void *memory = calloc(i * 1E6, sizeof(int));
        if(memory == NULL){
            // malloc failed to allocate the memory we asked for
            return -1;
    }
        // 'llu' is for 'long long unsigned'
        printf("Successfully allocated %llu million integers\n", i);
        ++i;
    }
    return 0; 
}
