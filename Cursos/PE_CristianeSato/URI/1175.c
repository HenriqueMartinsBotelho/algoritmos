#include <stdio.h>

int main(){
    int n;
    int v[20];
    for (int i = 0; i < 20; i++){
    scanf("%d", &v[i]);   
    }
    for (int i = 19; i >= 0; i--)
    {
        printf("N[%d] = %d\n",19-i, v[i]);
    }
    
    
}