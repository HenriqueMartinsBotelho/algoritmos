// Inverter recursivamente um vetor


#include <stdio.h> 
  
void inverte(int vetor[], int inicio, int fim) 
{ 
   int temp; 
   if (inicio >= fim) 
     return; 
   temp = vetor[inicio];    
   vetor[inicio] = vetor[fim]; 
   vetor[fim] = temp; 
   inverte(vetor, inicio+1, fim-1);    
}      
  

int main () {
 int n, i, vetor[1000];
 scanf ("%d", &n);
 for (i = 0; i < n; i++){
  scanf ("%d", &vetor[i]);
 }
 inverte(vetor, 0, n-1);

  for (int i = 0; i < n; i++){
    printf("%d ", vetor[i]);
  }
  printf("\n");

 return 0;
}