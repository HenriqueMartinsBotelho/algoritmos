#include <stdio.h>

int soma_divisores(int n);

/* Nao modifique o main!! */
int main() {
  int n;
  scanf("%d", &n);
  if(soma_divisores(n) == n) {
    printf("SIM\n");
  } else {
    printf("NAO\n");
  }
  return 0;
}


int soma_divisores(int n){
    int soma = 0;
    for (int i = 1; i < n; i++)
    {
        if (n % i == 0)
        {
            soma = soma + i;
        }
    }
    return soma;
}