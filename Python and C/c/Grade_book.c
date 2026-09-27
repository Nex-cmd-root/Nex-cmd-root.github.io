#include <stdio.h>

int average();

int main() {

   printf("What are your five scores test scores?\n");

   int avg_score = average();
   if (avg_score == 1) {
     return 1; // Exit if there was an invalid input
   }

   printf("Your average score is %d.\n", avg_score);

   if (avg_score >= 90){
       printf("Excellent, you got an A+ overall!");
        } else if (avg_score >= 80){
             printf("This is very good, an A overall!");
        } else if (avg_score >= 75){
             printf("Nice, you got a B+ overall!");
        } else if (avg_score >= 70){
             printf("Good work, a B overall.");
        } else if (avg_score >= 65){
             printf("That's a C+, not bad for an average.");
        } else if (avg_score >= 60){
             printf("C, an average mark overall.");
        } else if (avg_score >= 55){
             printf("A D+, you're cutting it close.");
        } else if (avg_score >= 50){
             printf("You barely made it with a D.");
        } else {
             printf("You got a failing grade, better luck next time.");
        }
   return 0;
}

int average() {

   int scores[] = {0, 0, 0, 0, 0};
   int i;
   int total = 0;

   for (i = 0; i < 5; i++) {
      if (scanf("%d", &scores[i]) != 1) {
            printf("\nInvalid input type! Exiting system.\n");
            return 1;
        };
      if (scores[i] > 100 || scores[i] < 0) {
         printf("Enter a valid range from 0 to 100.");
         i--;
      }
   }

   for (i = 0; i < 5; i++) {
      total += scores[i];
   }

   int average = total / 5;

return average;
}
