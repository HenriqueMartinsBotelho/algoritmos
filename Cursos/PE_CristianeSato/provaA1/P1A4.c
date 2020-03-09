#include <stdio.h>

int mult(int numbers[], int n);


int main(){
    
    int n;
    scanf("%d", &n);
    
    int v[n];
    int x;
    for (int i = 0; i < n; i++){
        scanf("%d", &x);
        v[i] = x;
    }
    
    printf("%d\n", mult(v, n));

}

int mult(int numbers[], int n){
    if(n <= 0)
        return 1;
    else
        return mult(numbers, n-1) * numbers[n-1];
}