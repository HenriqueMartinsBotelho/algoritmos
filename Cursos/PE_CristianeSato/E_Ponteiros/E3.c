/*
 Faça uma função arredonda que recebe um vetor v (como um int *) e posições de inicio e fim. 
A sua função deve modificar v arredondando os valores v[inicio] a v[fim-1] de modo que se v[i] 
não é um múltiplo de 10, então ele é arredondado para cima para o múltiplo de 10 mais próximo. 
Por exemplo, 81 e 87 são arredondados para 90. 80 não muda. 

Exemplo de entrada

5 15
40 51 62 13 84 25 66 97 28 59 90 31 12 53 84 95 16 57 78 99
Exemplo de saída

40 51 62 13 84 30 70 100 30 60 90 40 20 60 90 95 16 57 78 99 */

#include <stdio.h>

void arredonda(int v[], int inicio, int fim);

int main() {
  int inicio , fim, i;
  int v[20];
  scanf("%d %d", &inicio, &fim);
  for (i=0; i<20; i++) {
    scanf("%d", &v[i]);
  }
  arredonda(v, inicio, fim);
  for(i=0; i<19; i++) {
    printf("%d ", v[i]);
  }
  printf("%d\n", v[19]);  
}


void arredonda(int v[], int inicio, int fim){
    for (int i = inicio; i < fim; i++){
        if (v[i] % 10 != 0){
            v[i] = v[i] + 10 - (v[i] % 10 );
        }
    }
}