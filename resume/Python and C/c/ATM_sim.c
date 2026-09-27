#include <stdio.h>

int main() {

   int balance = 1000;
   int deposit = 0;
   int withdraw = 0;
   int choice = 0;

   do {
     printf("\nHello, what would you like to do today?\n\n");
     printf("1. Check Balance,\n 2. Deposit,\n 3. Withdraw,\n 4. Exit.\n");
     scanf("%d", &choice);

  
      switch (choice) {
         case 1:
            printf("Your balance is %d.\n", balance);
         break;
         case 2:
            printf("\nHow much would you like to deposit?\n");
            scanf("%d", &deposit);
            balance += deposit;
            printf("\nYou have succesfully deposited %d.\n", deposit);
         break;
         case 3:
            printf("\nHow much would you like to withdraw?\n");
            scanf("%d", &withdraw);
            balance -= withdraw;
            if (balance < 0) {
               printf("\ninsufficient balance.\n");
               balance += withdraw;
            } else {
            printf("\nYou have succesfully withdrawn %d.\n", withdraw);
              }
         break;
         case 4:
            printf("Thank you for using our ATM. Goodbye!\n");
         break;
         default:
            printf("\nInvalid choice.\n");
       }
   } while (choice != 4);
return 0;
}