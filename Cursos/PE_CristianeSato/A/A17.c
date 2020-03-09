#include<stdio.h>

/* retorna o mdc entre n1 e n2 */
/* assumindo n1<n2 */
int mdc(int n1, int n2);

/* nao modifique o main!! */
int main() {
  int n1, n2, r;
  scanf("%d %d", &n1, &n2);

  if (n1<n2) r = mdc(n1,n2);
  else r = mdc(n2, n1);
  
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
