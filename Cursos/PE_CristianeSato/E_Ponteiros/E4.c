#include <stdio.h>
#include <stdlib.h>

int main(){

    int qnt, n;
    double x;
    double mediana;
    void InsertionSort(int n, double v[]);
    double *medianas = (double *)malloc(100 * sizeof(double));
    

    scanf("%d", &qnt);

    for (int i = 0; i < qnt; i++)
    {
        scanf("%d", &n);
        double *v = (double *)malloc(n * sizeof(double));
        
        for (int j = 0; j < n; j++)
        {
            scanf("%lf", &v[j]);
        }
        
        InsertionSort(n, v);
        
        mediana = v[n/2];
        medianas[i] = mediana;
    }
    for (int h = 0; h < qnt; h++){
        printf("%.2lf\n", medianas[h]);
    }
    
}

void InsertionSort(int n, double v[]){
    
    int key, j;

    for (int i = 1; i < n; i++){
        key = v[i];
        j =  i - 1;
        while (j >= 0 && v[j] > key){
            v[j + 1] = v[j];
            j = j - 1;
        }
        v[j+1] = key;
    }
    
}
