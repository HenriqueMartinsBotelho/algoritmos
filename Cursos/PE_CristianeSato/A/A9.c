#include <stdio.h>

int main(){

    float A, P, IMC;
    scanf("%f", &A);
    scanf("%f", &P);
    IMC = P/(A*A);
    if (IMC < 16)
        printf("Magreza grave\n");
    if (IMC > 16 && IMC < 17)
        printf("Magreza moderada\n");
    else if (IMC > 17 && IMC < 18.5)
        printf("Magreza leve\n");
    else if (IMC > 18.5 && IMC < 25)
        printf("Saudavel\n");
    else if (IMC > 25 && IMC < 30)
        printf("Sobrepeso\n");
    else if (IMC > 30 && IMC < 35)
        printf("Obesidade Grau I\n");
    else if (IMC > 35 && IMC < 40)
        printf("Obesidade Grau II (severa)\n");    
    else if (IMC >= 40)
        printf("Obesidade Grau III (morbida)\n");

    return 0;
}