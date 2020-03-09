#include <stdio.h>

int soma(long int n, int *v);

int main(){
    long int n;
    int i = 0;
    int v[100];

    scanf("%li\n", &n);

   

 for (int i = 0; i < n; i++){
        scanf("%li", &v[i]);
    }
    
    printf("%li\n", soma(n, v));
}

int soma(long int n, int *v){
    long int soma = 0;
    for (int i = 0; i < n; i++){
        soma = soma + v[i];
    }
    return soma;
}