#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

// PUSH: Adds a node to the top of the stack
void push(struct Node **top_ref, int new_data) {
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    if (new_node == NULL) {
        printf("Stack Overflow (Out of memory)\n");
        return;
    }
    new_node->data = new_data;
    new_node->next = (*top_ref);
    (*top_ref) = new_node;
}

// POP: Removes the top node and returns its data
int pop(struct Node **top_ref) {
    if (*top_ref == NULL) {
        printf("Stack Underflow (The stack is empty!)\n");
        return -1; // Return an error value
    }
    
    struct Node *temp = *top_ref;   // Hold onto the current top node temporarily
    int popped_value = temp->data;  // Extract the data cargo
    
    *top_ref = (*top_ref)->next;    // Move the top tracker down to the next node
    
    free(temp);                     // Safely delete the old top node from the heap
    return popped_value;            // Return the extracted number
}

int peek(struct Node *top) {
    if (top == NULL) {
        printf("The stack is empty!\n");
        return -1;
    }
    return top->data;
}

int main() {
    struct Node *stack = NULL; // Start with an empty stack

    printf("--- Pushing Items Onto Stack ---\n");
    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30); // 30 is now at the very top

    printf("\nRemaining item at top of stack: %d\n", peek(stack));

    printf("\n--- Popping Items Off Stack ---\n");
    printf("Popped: %d\n", pop(&stack)); // Should pop 30
    printf("Popped: %d\n", pop(&stack)); // Should pop 20

    printf("\nRemaining item at top of stack: %d\n", peek(stack)); // Should be 10

    // Clean up remaining nodes
    free(stack);
    return 0;
}