#include <stdio.h>

int main(){
    int n, x;
    int v[100];

    for (int i = 0; i < 100; i++){
        v[i] = 0;
    }
    

    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        scanf("%d", &x);
        v[x]++;
    }

    int cout = 0;
    for (int i = 0; i < 100; i++){
        if (v[i] > 0){
            cout++;
        }
    }
    printf("%d\n", cout);
      
}