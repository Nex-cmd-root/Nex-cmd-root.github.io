#include <stdio.h>

// Clean prototype: Takes the starting address and the number of elements
float calculate_average(int *ptr, int size);

int main() {
    int grades[3] = {85, 90, 95};

    // Pass the starting address ('grades') and the size ('3') to the function
    float avg_score = calculate_average(grades, 3);
    
    printf("\nYour average score is: %.2f\n", avg_score);

    // Grade breakdown
    if (avg_score >= 90.0) {
        printf("Excellent, you got an A+ overall!\n");
    } else if (avg_score >= 80.0) {
        printf("This is very good, an A overall!\n");
    } else if (avg_score >= 75.0) {
        printf("Nice, you got a B+ overall!\n");
    } else if (avg_score >= 70.0) {
        printf("Good work, a B overall.\n");
    } else {
        printf("You passed, but keep studying!\n"); // Shortened for scannability
    }

    return 0;
}

// The function now owns the memory navigation logic!
float calculate_average(int *ptr, int size) {
    int total = 0;
    
    for (int i = 0; i < size; i++) {
        total += *ptr; // Grab the value at the current locker
        ptr++;         // Move to the next consecutive locker
    }
    
    return (float)total / size; 
}