#include <stdio.h>

int main(){
    int n;
    int N[1000];
    scanf("%d", &n);
    int x, i;
    for (i = 0, x = 0; i < 1000; i++){
        printf("N[%d] = %d\n", i, x);
        x++;
        if (x == n){
            x = 0;
        }
    }
      
}
