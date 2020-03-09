#include <stdio.h>

int valores(int n, int *v, int x);

int main(){
    int n, x, k;
    int i = 0;
    int v[10000];

    scanf("%d\n", &n);

    for (int i = 0; i < n; i++){
        scanf("%d\n", &v[i]);
    }
    
    scanf("%d", &x);


    printf("%d\n", valores(n, v, x));
}

int valores(int n, int *v, int x){
    int j = 0;
    for (int i = 0; i < n; i++){
        if(v[i] >= x)
            j++;
    }
    return j;
}