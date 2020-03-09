/*

A single linked list has the following properties.

1) Sucessive elements are connected by pointers
2) The last element points to NULL
3) Can grow or shring in size during execution of a program
4) Can be made just as long as required
5) Does not wast memory space. It allocates memory as list grows.


Uma lista encadeada é uma sequência de registros chamados de node;
Cada node contém um objeto de determinado tipo e o endereço do node
sequinte (no caso do último node esse endereço é NULL)
Os nodes que armazenam elementos consecutivos da sequência não ficam 
necessáriamente em posições consecutivas da memória.

*/


#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode{
    int data; // dado do tipo inteiro (poderia ser outro tipo)
    struct ListNode* next; // pointer to next node
}node;

int ListLength(node *head);



int main(){

    // Inicializando a lista
    node *head;
    head = (node*)malloc(sizeof(node));
    head->data = 10;
    head->next = NULL;

    // O segundo nó pode ser adicionando da seguinte forma
    head->next = (node*)malloc(sizeof(node));
    head->next->data = 20;
    head->next->next = NULL;

    // Imprimindo o tamanho da lista
    int tamanho;
    tamanho = ListLength(head);
    printf("Tamanho da lista: %d\n", tamanho);

    return 0;
}

/*                  Conta número de nós na lista
    * Time complexity: O(n), for scanning the list of size n.
    * Space COmplexity: O(1), for creating a temporary variable.  
*/
int ListLength(node *head){
    node *current = head;
    int count = 0;
    while(current != NULL){
        count++;
        current = current->next;
    }
    return count;
}


/*                  Insere nó no início da lista
*/

