#include <stdio.h>

int main(){
    int p;
    int t = 0;
    scanf("%d", &p);
    for (int i = 2; i < p; i++){
        if (p % i == 0){
            t = 1;
        }
    }
    if (t == 1 || p == 1)
        printf("COMPOSTO\n");
    else
        printf("PRIMO\n");
    
}