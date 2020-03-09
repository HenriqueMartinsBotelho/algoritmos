#include <stdio.h>


int main(){
    long int n, x, k;
    int i = 0;
    int v[100][100];

    scanf("%li\n", &n);

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            scanf("%d", &v[i][j]);
        }
    }

    int soma = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < i; j++){
            soma = soma + v[i][j];
        }
    }

    printf("%d\n", soma);

}

