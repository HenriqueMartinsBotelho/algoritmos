#include <stdio.h>


int main(){
    int n;
    int m1[100][100];
    int m2[100][100];
    int m3[100][100];
    scanf("%d", &n);

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            scanf("%d", &m1[i][j]);
        }
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            scanf("%d", &m2[i][j]);
        }
    }

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            m3[i][j] = m1[i][j] + m2[i][j]; 
        }
    }
    
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            printf("%d ", m3[i][j]);
        }
        printf("\n");
    }
    printf("\n");

}
