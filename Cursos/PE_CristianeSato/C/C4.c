#include <stdio.h>

int soma2(long int n, int *v, long int x);

int main(){
    long int n, x, k;
    int i = 0;
    int v[100];

    scanf("%li\n", &n);

    for (int i = 0; i < n; i++){
        scanf("%li", &v[i]);
    }
    
    scanf("%d", &x);

    if (soma2(n, v, x)){
        printf("SIM\n");
    }
}

int soma2(long int n, int *v, long int x){

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (x == (v[i] + v[j]) && i != j )
                return 1;
        }
        
    }
    return 0;
}