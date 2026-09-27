#include <stdio.h>
#include <stdlib.h>

int main() {

   int num_scores = 0;
   int *dynamic_array;
   int total = 0;

   printf("How many test scores do you want to enter? \n");
   scanf("%d", &num_scores);

   dynamic_array = (int *)malloc(num_scores * sizeof(int));

   if (dynamic_array == NULL) {
      printf("Error: System out of memory!\n");
      return 1;
   }

   printf("Enter your %d test scores\n", num_scores);
   for (int i = 0; i < num_scores; i++) {
      if (scanf("%d", &dynamic_array[i]) != 1) {
         printf("Invalid input! Please enter digits only.\n");
         return 1; 
      }
   }

   for (int i = 0; i < num_scores; i++) {
      total += dynamic_array[i];
   }

   printf("%d", total);

   free(dynamic_array);
return 0;
}