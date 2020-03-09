#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    struct Node *next;
} Node;


void printList(struct Node *node);
void PushFront(struct Node** head_ref, int new_data);


int main() {   
  struct Node* head = NULL; // Lista vazia 
  PushFront(&head, 10);
  printf("%p\n", head);
  PushFront(&head, 20);
  printf("%p\n", head);
  printf("Lista: "); 
  printList(head); 
  printf("\n");
  return 0; 
} 

void printList(struct Node *node) { 
  while (node != NULL) { 
     printf(" %d ", node->data); 
     node = node->next; 
  } 
} 

// Complexidade O(1)
void PushFront(struct Node** head_ref, int new_data) { 
    struct Node* new_node = (struct Node*) malloc(sizeof(Node)); /* 1. Alocação do nó */ 
    new_node->data = new_data;  /* 2. Colocando o dado no nó  */
    new_node->next = (*head_ref); 
    (*head_ref) = new_node; 

