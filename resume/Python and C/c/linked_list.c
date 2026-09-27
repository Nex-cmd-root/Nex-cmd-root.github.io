#include <stdio.h>
#include <stdlib.h>

// The blueprint for a single link in our chain
struct Node {
    int data;           // The cargo
    struct Node *next;  // The map pointer to the next locker block
};

void search_list (struct Node *head, int target);

int main() {
    // Create pointers to track our chain links
    struct Node *head = NULL;
    struct Node *second = NULL;
    struct Node *third = NULL;

    // Allocate 3 separate nodes randomly on the heap
    head = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));

    // Assign data and wire them together!
    head->data = 10;       // First node holds 10
    head->next = second;   // First node points to the second node's address

    second->data = 20;     // Second node holds 20
    second->next = third;  // Second node points to the third node's address

    third->data = 30;      // Third node holds 30
    third->next = NULL;    // The end of the chain points to NULL (the ground)

    // Let's print the list by following the chain!
    struct Node *current = head;
    while (current != NULL) {
        printf("Node Data: %d\n", current->data);
        current = current->next; // Slide down the wire to the next locker address!
    }

    search_list (head, 20);
    search_list (head, 99);

    // Freeing memory requires looping through and freeing each node individually
    free(head);
    free(second);
    free(third);

    return 0;
}

void search_list (struct Node *head, int target) {

    struct Node *current = head;
    while (current != NULL) {
        if (current->data == target) {
        printf("Target found!\n");
        return;
    }
    current = current->next; // No else needed!
    }
    printf("target not in list.\n");
}