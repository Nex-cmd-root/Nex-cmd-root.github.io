#include <stdio.h>

int main() {

   int number;
   printf("Enter your number:\n");
   scanf("%d", &number);

   int remainder = number % 2;
   if(remainder == 0) {
    printf("%d is an even number.", number);
   } else {
     printf("%d is an odd number.", number);
   }

return 0;
}