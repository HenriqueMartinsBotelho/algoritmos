#include <stdio.h>


int main(){
    int a, b, count, count2, sizea, digito;
    int vetor[20];
    int vetor2[20];
    count = 0;
    scanf("%d", &a);
    scanf("%d", &b);
    sizea = a;

    while (sizea != 0)
    {
        sizea /= 10;
        ++count;
    }

    for (int i = 0; i < count; i++ ){
        digito = a % 10;
        a = a / 10;
        vetor[i] = digito; 
    }

    count2 = 0;
    for (int i = count - 1; i >= 0; i-- ){
        digito = b % 10;
        b = b / 10;
        if (vetor[i] == digito){
            count2++;
        }
    }

    if (count == count2)
        printf("espelho\n");
    else{
        printf("nao espelho\n");
    }

}