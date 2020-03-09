#include <stdio.h>

int contar (int vetor[1000], int n, int x);

int main () {
 int n, i, vetor[1000], x;
 scanf ("%d", &n);
 for (i = 0; i < n; i++) {
 scanf ("%d", &vetor[i]);
 }
 scanf ("%d", &x);
 printf ("%d\n", contar (vetor, n, x));
 return 0;
}

int contar (int vetor[], int n, int x){
    if (n > 0 && vetor[n-1] >= x)
        return contar(vetor, n-1, x) + 1;
    else if (n == 0)
            return 0;
    else 
        return contar(vetor, n-1, x);
}

