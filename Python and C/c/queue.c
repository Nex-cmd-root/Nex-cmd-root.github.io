#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

// A parent structure to manage the two gateway pointer addresses
struct Queue {
    struct Node *front;
    struct Node *rear;
};

// Tool to initialize a fresh, empty queue structure
struct Queue* create_queue() {
    struct Queue *q = (struct Queue*)malloc(sizeof(struct Queue));
    q->front = q->rear = NULL;
    return q;
}

// ENQUEUE: Adds an item to the rear of the line
void enqueue(struct Queue *q, int new_data) {
    struct Node *new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = NULL;

    // If queue is completely empty, the new node becomes BOTH front and rear
    if (q->rear == NULL) {
        q->front = q->rear = new_node;
        return;
    }

    // Otherwise, stitch it to the end of the existing line and advance the rear pointer
    q->rear->next = new_node;
    q->rear = new_node;
}

// DEQUEUE: Removes the oldest item from the front of the line
int dequeue(struct Queue *q) {
    if (q->front == NULL) {
        printf("Queue Underflow (The line is empty!)\n");
        return -1;
    }

    struct Node *temp = q->front;
    int value = temp->data;

    q->front = q->front->next; // Slide the front pointer to the next person in line

    // If the front just stepped off into NULL, the queue is empty; reset rear too
    if (q->front == NULL) {
        q->rear = NULL;
    }

    free(temp); // Free memory block
    return value;
}

void print_queue (struct Queue *q) {
    struct Node *current = q->front;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    struct Queue *queue = create_queue();

    enqueue(queue, 100);
    enqueue(queue, 200);
    enqueue(queue, 300);

    print_queue(queue);

    dequeue(queue);

    print_queue(queue);

    free(queue); // clean up the queue structure itself (not the nodes, which are freed in dequeue)

return 0;
}