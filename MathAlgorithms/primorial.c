#include <stdio.h>


int isprime(int p){
    int i;
    int divisores = 0;
    for(i = 1; i <= p; i++){
        if(p % i == 0)
            divisores++;
    }
    if( divisores == 2)
        return 1; //verdadeiro
    else
        return 0; //falso

}

int primorial(int n){
    if(n == 1)
        return 1;
    if(n == 2)
        return 2;
    while(n != 2) {
        if (isprime(n))
            return n * primorial(n - 1);
        else
            return primorial(n - 1);
    }
}

int main(){

    printf("%d\n",primorial(1));
    printf("%d\n",primorial(2));
    printf("%d\n",primorial(3));
    printf("%d\n",primorial(4));
    printf("%d\n",primorial(5));
    printf("%d\n",primorial(6));
    printf("%d\n",primorial(7));
    printf("%d\n",primorial(8));
    printf("%d\n",primorial(9));
    printf("%d\n",primorial(10));
    printf("%d\n",primorial(11));
    printf("%d\n",primorial(12));
    printf("%d\n",primorial(13));
    return 0;

}