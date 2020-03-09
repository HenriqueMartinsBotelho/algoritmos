#include <stdio.h>

int catalan(int n);

int main(){

    int n;
    scanf("%d", &n);

    printf("%d\n", catalan(n));    

    return 0;
}


int catalan(int n){
    if (n == 0){
        return 1;
    }
    else{
        
        return (4*n - 2.0)/(n+1.0) * catalan(n-1);
    }
}