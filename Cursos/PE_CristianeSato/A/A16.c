#include <stdio.h>

int main(){
    int n = 100000;
    int menor;
    while(n >= 0)
    {
        scanf("%d\n", &n);
        if (n < menor && menor >= 0)
            menor = n;
    } 
    printf(" a %d\n", menor);
}