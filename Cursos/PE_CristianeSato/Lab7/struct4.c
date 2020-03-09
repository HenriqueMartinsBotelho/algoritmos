/* Ao modificar r, modificamos o valor de c1 e de c2?
Descomente as linhas apropriadas no código para dar a sua resposta.

Tente responder na sua cabeça primeiro sem alterar o código.
Você pode alterar depois para verificar sua resposta, mas não esqueça de 
imprimir apenas MUDA c1, MUDA c2 ou NAO MUDA NENHUM na hora de submeter. */

#include <stdio.h>

typedef struct cor_s {
  int *r;
  int *g;
  int *b;
} cor;

int main(void) {
  int r=1, g=2, b=4;
  cor c1 = {&r, &g, &b};
  cor c2 = c1;
  r = 127;

  //printf("%d %d\n", *c1.r, *c2.r);
  
  printf("MUDA c1\n");
  printf("MUDA c2\n");
  //printf("NAO MUDA NENHUM\n");
  
  return 0;
}