// This program allocates a large amount of memory (X GB) and locks it in RAM using mlock.
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>

int main() {
    long int alloc_size = 50L * 1024 * 1024 * 1024;  // 16 GB
    char *memory = (char *)malloc(alloc_size);  // Use malloc instead of calloc

    if (memory == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }

    // Lock the allocated memory in RAM
    int err = mlock(memory, alloc_size);

    if (err == 0) {
        printf("Memory successfully allocated and locked in RAM.\n");
    } else {
        perror("mlock failed");
        exit(EXIT_FAILURE);
    }

    // Keep the program running indefinitely
    while (1) {
        sleep(10000);
    }

    // Unreachable code, but included for completeness
    free(memory);
    return 0;
}
