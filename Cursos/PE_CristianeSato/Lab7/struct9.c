#include <stdio.h>

typedef struct country_s {
  char sigla[3];
  double populacao;
} country;

void imprime (country c) {
  printf("%s %.1f\n", c.sigla, c.populacao);
}

void muda (country *c1, country *c2) {
  country c = *c1;
  *c1 = *c2;
  *c2 = c;
}

int main(void) {
  country brasil = {"BRA", 209.3};
  country argentina = {"ARG", 44.2};
  
  imprime(brasil);
  imprime(argentina);
  //chame sua funcao aqui
  muda (&brasil, &argentina);
  
  imprime(brasil);
  imprime(argentina);
  return 0;
}