#include <stdio.h>


void numeros(int vector[],int size);

int busca(int v[],long int n,int valor);

int main(void) {
 long int n;
 int x;
 
 scanf("%li",&n);
 int v[n];
 
 numeros(v, n); // Le os n números e armazena no vetor v.
  
  while (scanf ("%d", &x) != EOF) {
     if(busca(v,  n,  x) == 1)
        printf("SIM\n");
     else 
        printf("CHAVE NAO ENCONTRADA\n");
  }
  return 0;
}


void numeros(int v[], int n){
  for(int i=0; i < n; i++){
    scanf("%d", &v[i]);
  }
}


int busca(int v[], long int n, int valor){
    for(int i = 0; i < n; i++){
        if(valor == v[i])
            return 1;
    }
    return 0; 
}

