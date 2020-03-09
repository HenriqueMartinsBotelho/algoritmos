#include <stdio.h>
#include <math.h>



typedef struct ponto_s{
    double x;
    double y;
}ponto;

typedef struct circulo_s{
    ponto centro;
    double raio;
}circulo;

double dist(ponto c, ponto p){
    double x = pow((c.x - p.x), 2) + pow((c.y - p.y), 2);
    x = sqrt(x);
    return x;
}

int dentro(circulo c, ponto p){
    double y = dist(c.centro, p);
    if (y < c.raio){
        return 1;
    }
    return 0;
}



int main(void) {
  circulo c;
  ponto p;
  scanf("%lf %lf", &p.x, &p.y);
  scanf("%lf %lf %lf", &c.centro.x, &c.centro.y, &c.raio); 
  if(dentro(c,p)) printf("DENTRO\n");
  else printf("FORA\n");
  return 0;
}