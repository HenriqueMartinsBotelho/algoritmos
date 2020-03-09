#include<stdio.h>

/* retorna o mdc entre n1 e n2 */
/* assumindo n1<n2 */
int mdc(int n1, int n2);

/*retorna o mmc entre n1 e n2*/
int mmc(int n1, int n2);
  
/* nao modifique o main!! */
int main() {
  int n1, n2, r;
  scanf("%d %d", &n1, &n2);

  if (n1<n2) r = mmc(n1,n2);
  else r = mmc(n2, n1);
  
  printf("%d\n", r);
}

int mdc(int n1, int n2){
  if (n2==0){
    return n1;
}
  else{
    return mdc(n2,n1 % n2);
}
}

int mmc(int n1, int n2){
    int x;
    x = n1 * n2/mdc(n1,n2);
    return x;
}