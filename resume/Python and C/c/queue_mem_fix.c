#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

struct Queue {
    struct Node *front;
    struct Node *rear;
};

struct Queue* create_queue() {
    struct Queue *q = (struct Queue*)malloc(sizeof(struct Queue));
    q->front = q->rear = NULL;
    return q;
}

void enqueue(struct Queue *q, int new_data) {
    struct Node *new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = NULL;

    if (q->rear == NULL) {
        q->front = q->rear = new_node;
        return;
    }

    q->rear->next = new_node;
    q->rear = new_node;
}

int dequeue(struct Queue *q) {
    if (q->front == NULL) {
        printf("Queue Underflow (The line is empty!)\n");
        return -1;
    }

    struct Node *temp = q->front;
    int value = temp->data;

    q->front = q->front->next;

    if (q->front == NULL) {
        q->rear = NULL;
    }

    free(temp);
    return value;
}

void print_queue(struct Queue *q) {
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

    printf("Initial Queue: ");
    print_queue(queue);

    dequeue(queue);

    printf("After 1 Dequeue: ");
    print_queue(queue);

    // FIX: Clear out any remaining nodes left in line before destroying the box
    while (queue->front != NULL) {
        dequeue(queue); // Dequeue safely handles data extraction and freeing the nodes!
    }

    // Now that the line is empty, it is 100% safe to free the parent tracking box
    free(queue); 
    queue = NULL;

    return 0;
}