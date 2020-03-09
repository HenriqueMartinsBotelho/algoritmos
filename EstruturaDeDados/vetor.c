#include <stdio.h>



/**************************ORDENAÇÃO***********************************

    Recebe um vetor a quantidade de elementos e o ordena.
    A chave é o elemento que esta sendo comparado com os outros.
    j se inicia sendo o elemento anteiror a chave.
*/

void InsertionSort(int n, int v[]){
    
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


int main(){
    int v[100];

    int n;
    printf("Digite a quantidade de elementos do vetor\n");
    scanf("%d", &n);
    printf("Digite os elementos: \n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &v[i]);
    }
    
    InsertionSort(n,v);
    
    for (int i = 0; i < n; i++)
    {
        printf("%d ", v[i]);
    }
    
    printf("\n");






/*

Insertion Sort versão passo a passo

void InsertionSort(int n, int v[]){
    
    int key, j;

    for (int i = 1; i < n; i++)
    {
        key = v[i];
        j =  i - 1;
        while (j >= 0 && v[j] > key)
        {
            v[j + 1] = v[j];
            j = j - 1;
        }
        for (int h = 0; h < n; h++)
        {
            printf("%d ", v[h]);
        }
        v[j+1] = key;
        printf("\n");
        
    }
    
}


*/








    
}