#include <stdio.h>

int main() {
    int balance = 1000;
    int deposit = 0;
    int withdraw = 0;
    int choice = 0;

    // Declaring the pointer here is perfectly fine
    FILE *file_ptr;

    do {
        printf("\nHello, what would you like to do today?\n\n");
        printf("1. Check Balance\n");
        printf("2. Deposit\n");
        printf("3. Withdraw\n");
        printf("4. Exit\n");
        printf("Enter option: ");

        if (scanf("%d", &choice) != 1) {
            printf("\nInvalid input type! Exiting system.\n");
            return 1;
        }

        switch (choice) {
            case 1:
                printf("\nYour balance is $%d.\n", balance);
                break;

            case 2:
                printf("\nHow much would you like to deposit? $");
                if (scanf("%d", &deposit) != 1) return 1;

                if (deposit <= 0) {
                    printf("Invalid amount. Must deposit more than $0.\n");
                } else {
                    balance += deposit;
                    printf("You have successfully deposited $%d.\n", deposit);

                    // LOG ONLY ON SUCCESS: Open, write, close right here
                    file_ptr = fopen("receipt.txt", "a");
                    if (file_ptr == NULL) {
                        printf("Error: Could not update receipt log.\n");
                        return 1;
                    }
                    fprintf(file_ptr, "Deposited: $%d (New Balance: $%d)\n", deposit, balance);
                    fclose(file_ptr);
                }
                break;

            case 3:
                printf("\nHow much would you like to withdraw? $");
                if (scanf("%d", &withdraw) != 1) return 1;

                if (withdraw <= 0) {
                    printf("Invalid amount. Must withdraw more than $0.\n");
                } else if (withdraw > balance) {
                    printf("Insufficient balance! Transaction canceled.\n");
                    // No file logging happens here because it failed!
                } else {
                    balance -= withdraw;
                    printf("You have successfully withdrawn $%d.\n", withdraw);

                    // LOG ONLY ON SUCCESS: Open, write, close right here
                    file_ptr = fopen("receipt.txt", "a");
                    if (file_ptr == NULL) {
                        printf("Error: Could not update receipt log.\n");
                        return 1;
                    }
                    fprintf(file_ptr, "Withdrew: $%d (New Balance: $%d)\n", withdraw, balance);
                    fclose(file_ptr);
                }
                break;

            case 4:
                printf("\nThank you for using our ATM. Goodbye!\n");
                break;

            default:
                printf("\nInvalid choice. Please select 1-4.\n");
        }
        
        // The second switch is removed to prevent accidental, false logging!

    } while (choice != 4);

    return 0;
}