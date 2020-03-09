#include <stdio.h>


int main(){
    long int n, x, k;
    int i = 0;
    char opcao;

    scanf("%c\n", &opcao);

    scanf("%d\n", &n);

    int v[n][n];

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            scanf("%d", &v[i][j]);
        }
    }

    int soma = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < i; j++){
            printf("%d ", v[i][j]);
            soma = soma + v[i][j];
        }
    }

    int media;
    media = soma / (n * n); 

    if (opcao == 'S'){
        printf("%d\n", soma);
    }
    if (opcao == 'M'){
        printf("%d\n", media);
    }
    
    


}

