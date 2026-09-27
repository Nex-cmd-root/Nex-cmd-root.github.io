#include <stdio.h>

struct student {
    int scores[3];
    float average;
};

// Return type matches our structural float type
float calculate_student_average(struct student *grades_ptr);

int main() {
    struct student s1;

    // Correctly populating our custom struct package
    s1.scores[0] = 85;
    s1.scores[1] = 78;
    s1.scores[2] = 91;

    // Passing the address of our struct instance
    float avg_score = calculate_student_average(&s1);
    
    printf("\nYour average score is: %.2f\n", avg_score);

    // Grade breakdown
    if (avg_score >= 90.0) {
        printf("Excellent, you got an A+ overall!\n");
    } else if (avg_score >= 80.0) {
        printf("This is very good, an A overall!\n");
    } else {
        printf("You passed, but keep studying!\n"); 
    }

    return 0;
}

float calculate_student_average(struct student *grades_ptr) {
    int total = 0;

    // Use the arrow operator to safely crawl the internal array
    for (int i = 0; i < 3; i++) {
        total += grades_ptr->scores[i];
    }
    
    // (float) protects our decimals. We divide directly by 3.
    grades_ptr->average = (float)total / 3;
    
    return grades_ptr->average;
}