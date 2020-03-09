#include <stdio.h>


int main(){
    int n;
    scanf("%d", &n);
    int m1[n][n];
    int m2[n][n];

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            scanf("%d", &m1[i][j]);
        }
    }

    //Transpondo
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            m2[i][j] = m1[j][i]; 
        }
    }
    
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            printf("%d ", m2[i][j]);
        }
        printf("\n");
    }
    printf("\n");

}
