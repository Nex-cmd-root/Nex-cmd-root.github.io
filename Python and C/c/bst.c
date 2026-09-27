#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* create_node(int value) {
    struct TreeNode *new_node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    new_node->data = value;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

struct TreeNode* search_tree(struct TreeNode *root, int target) {
    if (root == NULL || root->data == target) {
        return root;
    }
    if (target < root->data) {
        return search_tree(root->left, target);
    }
    return search_tree(root->right, target);
}

// FIX: Recursive cleanup function (Post-Order Traversal)
void free_tree(struct TreeNode *root) {
    if (root == NULL) return;

    // 1. Clear out the left sub-branches first
    free_tree(root->left);
    
    // 2. Clear out the right sub-branches second
    free_tree(root->right);
    
    // 3. Now that the children are gone, it is safe to free the parent node
    free(root);
}

int main() {
    struct TreeNode *root = create_node(50);

    root->left = create_node(30);
    root->right = create_node(70);
    root->left->left = create_node(20);

    // Test for a node that exists
    printf("Searching for 20: ");
    if (search_tree(root, 20) != NULL) {
        printf("Found node!\n");
    } else {
        printf("Not in tree.\n"); // Cleaned up redundant 'else if'
    }

    // Test for a node that does not exist
    printf("Searching for 99: ");
    if (search_tree(root, 99) != NULL) {
        printf("Found node!\n");
    } else {
        printf("Not in tree.\n");
    }

    // Safely clear out every dynamic node on the heap
    free_tree(root);
    root = NULL;

    return 0;
}