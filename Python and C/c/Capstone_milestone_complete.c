#include <stdio.h>
#include <stdlib.h>

struct student {
    int id;
    int grade;
    char name[50];
};

void save_database(struct student *database_array, int num_students);

int main() {
    int num_students = 0;
    struct student *database_array = NULL;

    printf("How many students are in your class?\n");
    while (scanf("%d", &num_students) != 1 || num_students <= 0) {
        printf("Error: Invalid input. Please enter a positive number: ");
        while (getchar() != '\n'); // Clear buffer
    }
    while (getchar() != '\n'); // Clean any final trailing newlines before entry loop

    database_array = (struct student *)malloc(num_students * sizeof(struct student));

    if (database_array == NULL) {
        printf("Error: System out of memory.\n");
        return 1;
    }

    for (int i = 0; i < num_students; i++) {
        printf("\nEntering data for student %d:\n", i + 1);

        printf("Enter student ID (format: xxxxx): ");
        while (scanf("%d", &database_array[i].id) != 1) {
            printf("Invalid ID. Enter digits only: ");
            while (getchar() != '\n');
        }

        printf("Enter student grade (0 to 100): ");
        while (scanf("%d", &database_array[i].grade) != 1 || database_array[i].grade < 0 || database_array[i].grade > 100) {
            printf("Invalid grade. Enter a number between 0 and 100: ");
            while (getchar() != '\n');
        }
        while (getchar() != '\n'); // Clean buffer cleanly right before fgets

        printf("Enter student name: ");
        fgets(database_array[i].name, sizeof(database_array[i].name), stdin);

        // Remove trailing newline character
        for (int j = 0; database_array[i].name[j] != '\0'; j++) {
            if (database_array[i].name[j] == '\n') {
                database_array[i].name[j] = '\0';
                break;
            }
        }
    }

    save_database(database_array, num_students);

    free(database_array);
    database_array = NULL;
    
    return 0;
}

void save_database(struct student *database_array, int num_students) { 
    FILE *file_ptr = fopen("classroom_db.txt", "w"); 
    
    if (file_ptr == NULL) { 
        printf("Error: Could not update classroom_db.txt\n"); 
        return; 
    } 
    
    for (int i = 0; i < num_students; i++) {
        fprintf(file_ptr, "Student %d:\n", i + 1);
        fprintf(file_ptr, "Student ID: %d\n", database_array[i].id); 
        fprintf(file_ptr, "Student Grade: %d\n", database_array[i].grade); 
        fprintf(file_ptr, "Student Name: %s\n\n", database_array[i].name); 
    } 

    fclose(file_ptr);
    printf("\nDatabase successfully saved to 'classroom_db.txt'.\n");
}