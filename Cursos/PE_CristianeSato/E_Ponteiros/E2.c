#include<stdio.h>

void troca(int *p1, int *p2);

int main() {
 int x, y;
 int n;
 scanf("%d", &n);

 while(n){
    n--;
    scanf("%d %d", &x, &y);
    troca(&x, &y);
    printf("%d %d\n", x, y);
 }
 
 return 0;

}

void troca(int *p1, int *p2){
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}
