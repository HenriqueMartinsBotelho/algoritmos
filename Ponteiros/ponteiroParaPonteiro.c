#include <stdio.h>
#include <stdlib.h>


int main(){



    int a = 10;

    int* p = &a;
    int** pp = &p;

    printf("Enderaco de a %p \n", &a);
    printf("Enderaco de a %p \n", p);
    printf("Valor de a %d \n", *p);
    
    printf("Enderaco de p %p \n", &p);
    printf("Enderaco de p %p \n", pp);
    printf("Valor de p %d \n",  *pp);




    return 0;
}
