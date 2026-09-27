#include <stdio.h>
#include <time.h>
#include <stdlib.h>

// If you want to change the difficulty, you only change these two numbers
// #define is a keyword that allows you to define constants in C. Here, we define the minimum and maximum numbers for the guessing game.
#define MIN_NUM 1
#define MAX_NUM 100

int main() {
    int number = 0;
    int guess = 0;
    int attempts = 0;

    // Seed using NULL instead of 0
    srand(time(NULL));
    number = rand() % (MAX_NUM - MIN_NUM + 1) + MIN_NUM;

    // Dynamic strings based on our macros
    printf("Welcome to the Guessing Game!\n");
    printf("I have selected a number between %d and %d. Can you guess it?\n", MIN_NUM, MAX_NUM);

    do {
        printf("Enter your guess: ");
        
        // Protect against letters or symbols breaking the program
        if (scanf("%d", &guess) != 1) {
            printf("Invalid input! Please enter digits only.\n");
            return 1; 
        }

        attempts++;

        if (guess < number) {
            printf("Too low! Try again.\n");
        } else if (guess > number) {
            printf("Too high! Try again.\n");
        } else {
            printf("Congratulations! You guessed the number %d in %d attempts.\n", number, attempts);
        }
    } while (guess != number);

    return 0; // Properly close the main function
}