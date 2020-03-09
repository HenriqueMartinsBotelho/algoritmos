#include <stdio.h>

// Esta funcao calcula recursivamente a potencia
// de 'a' elevado a 'n'.
 
long int potenciaRecursivo (long int a, long int n);

int main () {
 int a, n;
 scanf ("%d", &a);
 scanf ("%d", &n);
 printf ("%ld\n", potenciaRecursivo (a, n));
 return 0;
}

long int potenciaRecursivo (long int a, long int n){
    if(n == 1)
        return a;
    else
        return a * potenciaRecursivo(a,n-1);
    
}