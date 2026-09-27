#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main() {
    int number, guess, attempts = 0;

    // Generate a random number between 1 and 100
    srand(time(0));
    number = rand() % 100 + 1;
    printf("Welcome to the Guessing Game!\n");
    printf("I have selected a number between 1 and 100. can you guess what it is?\n");
    do {
        printf("Enter your guess: ");
        scanf("%d", &guess);
        attempts++;
        if (guess < number) {
            printf("Too low! Try again.\n");
        } else if (guess > number) {
            printf("Too high! Try again.\n");
        } else {
            printf("Congratulations! You guessed the number %d in %d attempts.\n", number, attempts);
        }
    } while (guess != number);
    return 0;
}