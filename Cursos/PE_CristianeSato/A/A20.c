#include<stdio.h>

 /* retorna 1 se a bola cai no buraco na posicao n com velocidade
inicial EXATAMENTE v */
 /* caso contrario, retorna 0*/
int checa (int n, int v);

int main () {
  int n, v, i, possivel;

  while(1) {
    scanf("%d %d", &n, &v);
    if(n==0) break;

    possivel = 0;
    for (i=1; i<=v; i++) {
      if(checa(n,i)) {
	printf("possivel\n");
	possivel = 1;
	break;
      }
    }
    if(!possivel) printf("impossivel\n");
  }
  return 0;
}


int checa (int n, int v){
    int x = 0;

    while (v != 0){
        for (int j = 1; j <= v; j++){
            x = x + v;
            if (x == n){
                return 1;
            }
        }
        v--;
    }
    return 0;
}