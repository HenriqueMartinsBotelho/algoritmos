#include<stdio.h>

/* retorna 1, se eh possivel dar o troco em duas notas */
/* retorna 0, caso contrario */
int troco(int valor);

int main() {
  int n, m;

  while(1) {
    scanf("%d %d", &n, &m);
    if(!n && !m) break;

    if(troco(m-n)) {
      printf("possible\n");
    } else {
      printf("impossible\n");
    }
  }
  return 0;
}

int troco(int valor){
    int v = valor;
    int i = 0;
    int count = 1;
    int newValor;
    int x = 1;
    int aprovado = 0;
    int notas[6] = {2,5,10,20,50,100};
    if (valor <= 200){
        
        for (int i = 0; i < 6; i++)
        {
            if (valor - notas[i] > 0){
                newValor = valor - notas[i];
                aprovado = 1;
            }
        }

        if(aprovado){
            for (int i = 0; i < 6; i++)
            {
                if (newValor - notas[i] == 0){
                    return 1;
                }
            }
        }
    }
    else
    {
        return 0;
    }
    return 0;
}