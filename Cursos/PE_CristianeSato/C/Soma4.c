#include <stdio.h>


int main(){
    long int n, x, k;
    int i = 0;
    

    scanf("%d\n", &n);

    int v[n][n];

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            scanf("%d", &v[i][j]);
        }
    }

    int soma = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < (n - i - 1); j++){
            printf("%d ", v[i][j]);
            soma = soma + v[i][j];
        }
        printf("%d\n");
    }

    printf("%d\n", soma);

}

