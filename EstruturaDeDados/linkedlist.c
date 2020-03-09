/*

A linked list has the following properties.

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

typedef struct node_s {
    int conteudo;
    struct node_s *prox;
}node;

typedef struct lista_s {
    node *primeiro;
} lista;

/* Um nó c e um ponteiro p para um nó podem agora ser declarados
 * assim: node c; node *p;
 * Se c é um nó então c.conteudo é o conteúdo do nó e 
 * c.prox é o endereço da célula seguinte.
 * Se p é o endereço de uma nó, então p->conteudo é o conteudo
 * do nó e p->seg e o endereço da célula seguinte.
 * Se p é o endereço do último nó então p->prox vale NULL. 
 * O endereço de uma lista encadeada é o endereço de sua primeira
 * célula.a Se "p" é o endereço de uma lista então podemos simplesmente
 * dizer "p é uma lista".
 * A seguinte observação coloca em evidência a natureza recursiva das
 * listas encadeadas: para toda lista encadeada p, 
 * 1. p é NULL ou
 * 2. p->prox é uma lista encadeada.
*/

/****************************  Inicializa a lista
 * Recebe uma ponteiro para a lista;
***************************** */
void init_lista(lista *lt) {
    lt->primeiro = NULL;
}


/****************************  Checa se a lista tem elementos
 * se primeiro apontar para NULL então a lista não tem elementos
***************************** */
int lista_vazia(lista lt) {
 if (lt.primeiro == NULL) {
   return 1;
 }
 return 0;
}

/**************************** Adiciona novo nó no começo
 * Recebe um valor do conteúdo do novo nó e um endereço de um nó
 * Aloca espaço para esse novo nó
 * Define o conteúdo dele como sendo v
 * Aponta ele para o elemento que lt aponta
 * Aponta lt para ele
***************************** */
void adiciona (int v, lista *lt){
    node *novo = malloc(sizeof(node));
    novo->conteudo = v;
    novo->prox = lt->primeiro;
    lt->primeiro = novo;
}




/**************************** Imprime a lista
 * Cria um ponteiro nd apontando para o primeiro elemento da lista
 * vai mudando o ponteiro para o proximo da lista
 * Quando nd valer NULL é porque chegamos ao fim.
***************************** */
void percorre(lista lt) {
 for(node *nd = lt.primeiro; nd != NULL; nd = nd->prox)
    imprime_node(*nd);
}




int main(){

    lista lt;
    init_lista(&lt);


    return 0;
}


