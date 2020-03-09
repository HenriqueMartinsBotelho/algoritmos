#include <stdio.h>

int valida(int n);

int main(){
    int teste = valida(12345);
    printf("%d/n", teste);
}

int valida(int n){
    int soma = 0;
    int x;
    while(n % 10 != 0){
        x = n % 10;
        soma += x;
        n = n / 10;
    }
    return soma;
}



