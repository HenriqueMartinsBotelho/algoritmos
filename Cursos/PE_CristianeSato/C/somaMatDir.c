#include <stdio.h>


int main(){
    int t1,t3;
    scanf("%d", &t1);
    int m1[t1][t1];
    int m2[t1][t1];
    t3 = t1 + t1;
    int m3[t3][t3];

    for (int i = 0; i < t1; i++){
        for (int j = 0; j < t1; j++){
            scanf("%d", &m1[i][j]);
        }
    }

    for (int i = 0; i < t1; i++){
        for (int j = 0; j < t1; j++){
            scanf("%d", &m2[i][j]);
        }
    }

    //Zerando a matriz
    for (int i = 0; i < t3; i++){
        for (int j = 0; j < t3; j++){
            m3[i][j] = 0; 
        }
    }


    //Primeira soma
    for (int i = 0; i < t1; i++){
        for (int j = 0; j < t1; j++){
            m3[i][j] = m1[i][j]; 
        }
    }


    //Segunda soma 
    int a = 0;
    int b = 0;
    for (int i = t1; i < t3; i++){
        for (int j = t1; j < t3; j++){
            m3[i][j] = m2[a][b];
            b++; 
        }
        a++;
        b = 0;
    }

    
    for (int i = 0; i < t3; i++){
        for (int j = 0; j < t3; j++){
            printf("%d ", m3[i][j]);
        }
        printf("\n");
    }
    printf("\n");

}
