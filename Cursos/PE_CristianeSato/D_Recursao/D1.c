#include <stdio.h>

long int fatorialRecursivo (long int n);


int main () {
 
 int n;
 scanf ("%d", &n);
 
 printf ("%ld\n", fatorialRecursivo (n));

 return 0;
}

long int fatorialRecursivo(long int n){
    if (n == 1 || n == 0){
        return 1;
    }
    else{
        return n * fatorialRecursivo(n-1);
    }
}

