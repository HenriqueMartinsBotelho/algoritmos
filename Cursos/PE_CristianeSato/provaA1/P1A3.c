#include <stdio.h>

int main(){
   
   int n, x;
   scanf("%d", &n);
   
   int m[n][n];
   for (int i = 0; i < n; i++){
       for (int j = 0; j < n; j++){
           scanf("%d", &x);
           m[i][j] = x;
       }
   }

   
   int n2 = 2*n;
   int m2[n2][n2];

    // Parte 1: -A
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            m2[i][j] = -1 * m[i][j];
        }
    }
    
    // Parte 2: J
    for (int i = 0; i < n; i++){
        for (int j = n; j < n2; j++){
            m2[i][j] = 1;
        }
    }

    // Parte 3: A
    for (int i = n, im = 0; i < n2; i++, im++){
        for (int j = n, jm = 0; j < n2; j++, jm++){
            m2[i][j] = m[im][jm];
        }
    }

    //Parte 4: I
    for (int i = n; i < n2; i++){
        for (int j = 0; j < n; j++){
            if (i == (j+n))
                m2[i][j] = 1;
            else
                m2[i][j] = 0;
        }
    }




   
   for (int i = 0; i < n2; i++){
       for (int j = 0; j < n2; j++){
           printf("%d ", m2[i][j]);
       }
       printf("\n");
   }


}