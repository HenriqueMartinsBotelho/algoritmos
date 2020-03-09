#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node *next;
}Node;

void printList(struct Node *node);
void PushFront(struct Node** head_ref, int new_data);

int main(){
    struct Node* head = NULL; // Lista vazia
    printList(head);
    return 0;
}

void printList(struct Node *node){
    while (node != NULL){
        printf(" %d ", node->data);
        node = node->next;
    }    
}
