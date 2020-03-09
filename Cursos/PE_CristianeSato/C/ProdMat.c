#include <stdio.h>


int main(){
    int n;
    scanf("%d", &n);
    int m1[n][n];
    int m2[n][n];
    int m3[n][n];

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


    int a, b, x;
    for (a = 0; a < n; a++){
        for (b = 0; b < n; b++){
            x = 0;
            for (int i = 0; i < n; i++){
                x = x + m1[a][i]*m2[i][b];
            }
             m3[a][b] = x; 
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





