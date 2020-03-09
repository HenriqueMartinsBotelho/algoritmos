// Retorna valor absoluto usando ponteiros

#include <stdio.h>

void absoluto(int *p);

int main() {
 
 int x;
 int n, i;
 scanf("%d", &n);

for(int i = 0; i < n; i++){
    scanf("%d", &x);
    absoluto(&x);
    printf("%d\n", x);
}

 return 0;

}

void absoluto(int *p){
    if(*p >= 0){
        return;
    }
    *p = -*p;
}