#include<stdio.h>

/* retorna o numero de anos para o populacao de A ultrapassar a de B
   se for menos de 100 anos*/
/* caso contrario, devolve um numero inteiro > 100 */
int resolve(double pa, double pb, double ga, double gb);

int main() {
  int n;
  double pa, pb, ga, gb;
  int i, r;
  scanf("%d", &n);
  for(i=0; i<n; i++) {
    scanf("%lf %lf %lf %lf", &pa, &pb, &ga, &gb);
    r = resolve(pa, pb, ga, gb);
    if(r==1) {
      printf("1 ano.\n");
    } else if (r<= 100) {
      printf("%d anos.\n", r);
    } else {
      printf("Mais de 1 seculo.\n");
    }
  }
}


int resolve(double pa, double pb, double ga, double gb){
    int pfa = pa;
    int pfb = pb;
    int anos = 0;

    while (pfa <= pfb){
        pfa = pfa + (ga/100)*pfa;
        pfb = pfb + (gb/100)*pfb;
        anos++;
    }

    return anos;

}