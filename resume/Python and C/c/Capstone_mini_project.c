#include <stdio.h>
#include <stdlib.h>

struct student {
   int id;
   int grade;
   char name[50];
};

void save_database (struct student *database_array, int num_students);

int main() {

   int num_students = 0;
   struct student *database_array = NULL;

   printf("How many students are in your class?\n");
   // Loop until the user provides a valid integer
   while (scanf("%d", &num_students) != 1) {
      printf("Error: Invalid input. Please enter a number: ");
        
         // Clear the bad text (like "abc") out of the buffer
         while (getchar() != '\n'); 
   }

   database_array = (struct student *)malloc(num_students * sizeof(struct student));

   if (database_array == NULL) {
      printf("Error, system out of memory.");
      return 1;
   }

   for (int i = 0; i < num_students; i++) {

      printf("\nEntering data for student %d:\n", i + 1);

      printf("Enter student ID. format: xxxxx\n");
      if (scanf("%d", &database_array[i].id) != 1 || num_students <= 0) {
         printf("Invalid number of students.\n");
         return 1;
      }

      printf("Enter student grade from 0 to 100.\n");
      if (scanf("%d", &database_array[i].grade) != 1 || num_students <= 0) {
         printf("Invalid number of students.\n");
         return 1;
      }

      printf("Enter student name.\n");

      getchar(); 
      fgets(database_array[i].name, sizeof(database_array[i].name), stdin);

         // Remove trailing newline character added by fgets, if any
         for (int j = 0; database_array[i].name[j] != '\0'; j++) {
            if (database_array[i].name[j] == '\n') {
               database_array[i].name[j] = '\0';
               break;
            }
         }
   }

   save_database (database_array, num_students);

   free(database_array);
   database_array = NULL;
return 0;
}

void save_database (struct student *database_array, int num_students) { 
    FILE *file_ptr; 
    file_ptr = fopen("classroom_db.txt", "w"); 
    
    if (file_ptr == NULL) { 
        printf("Error: could not update classroom_db.txt"); 
        return; // Return void instead of 1
    } 
    
    for (int i = 0; i < num_students; i++) {
        fprintf(file_ptr, "student %d:\n", i + 1);
        fprintf(file_ptr, "student ID: %d\n", database_array[i].id); 
        fprintf(file_ptr, "student grade: %d\n", database_array[i].grade); 
        fprintf(file_ptr, "student name: %s\n\n", database_array[i].name); 
    } 

    fclose(file_ptr);
    printf("\nDatabase successfully saved to 'classroom_db.txt'.\n");
}