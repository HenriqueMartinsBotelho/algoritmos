#include <stdio.h>

int main(){
    int div, n;
    div = 1;

    scanf("%d", &n);

    for (int i = 2; i < n; i = i + 2)
    {
        if (n % i == 0)
        {
            div++;
        }
    }
    
    if (n % 2 == 0){
        printf("%d\n",div);
    }
    else{
        printf("%d\n",0);
    }
    return 0;
}