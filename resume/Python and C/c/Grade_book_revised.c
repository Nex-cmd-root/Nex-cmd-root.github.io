#include <stdio.h>

// Pass the array and its size into the function
float calculate_average(int grades[], int size);

int main() {
    int test_scores[5] = {0};
    int i = 0;

    printf("Enter your five test scores (0 - 100):\n");

    // Handle input gathering inside main to keep data safe
    for (i = 0; i < 5; i++) {
        printf("Score %d: ", i + 1);
        
        if (scanf("%d", &test_scores[i]) != 1) {
            printf("\nInvalid input type! Exiting system.\n");
            return 1;
        }

        // Keep looping on the same index until a valid score is entered
        if (test_scores[i] > 100 || test_scores[i] < 0) {
            printf("Error: Score must be between 0 and 100. Try again.\n");
            i--; 
        }
    }

    // Call our calculation function
    float avg_score = calculate_average(test_scores, 5);
    printf("\nYour average score is: %.2f\n", avg_score);

    // Grade breakdown (Using floating point boundaries)
    if (avg_score >= 90.0) {
        printf("Excellent, you got an A+ overall!\n");
    } else if (avg_score >= 80.0) {
        printf("This is very good, an A overall!\n");
    } else if (avg_score >= 75.0) {
        printf("Nice, you got a B+ overall!\n");
    } else if (avg_score >= 70.0) {
        printf("Good work, a B overall.\n");
    } else if (avg_score >= 65.0) {
        printf("That's a C+, not bad for an average.\n");
    } else if (avg_score >= 60.0) {
        printf("C, an average mark overall.\n");
    } else if (avg_score >= 55.0) {
        printf("A D+, you're cutting it close.\n");
    } else if (avg_score >= 50.0) {
        printf("You barely made it with a D.\n");
    } else {
        printf("You got a failing grade, better luck next time.\n");
    }

    return 0;
}

// Clean utility function focused solely on math
float calculate_average(int grades[], int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        total += grades[i];
    }
    // (float) converts total temporarily so C performs decimal division
    return (float)total / size; 
}