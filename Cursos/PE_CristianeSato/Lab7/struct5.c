/* 1. Crie um struct prova_s com o seguintes campos:
- double notas[100]
- int n
- double media
- double minimo
- double maximo
- double variancia
2. Crie um tipo prova para struct prova_s

No main:
1. Crie uma variável prova p
2. Leia um inteiro n seguido de n notas, preenchendo p.
Você pode assumir que as notas são números de 0 a 10 (não precisa verificar).
3. Preencha os campos media, minimo, maximo e variancia de p. Não use funções prontas.
 Na dúvida sobre qual tipo de variância usar, é a variância amostral.
4. Imprima os campos media, minimo, maximo e variancia acessando os campos de p.
 Imprima com 2 casas decimais. */


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct prova_s{
     double notas[100];
     int n;
     double media;
     double minimo;
     double maximo;
     double variancia;
 }prova;
 
int main(){

    prova p;

    int n;
    scanf("%d",&n);
    
    // Lendo as n notas
    double x;
    double soma = 0;
    double minimo = 11;
    double maximo = -1;
    for (int i = 0; i < n; i++){
        scanf("%lf", &x);
        p.notas[i] = x;
        soma += x;
        if (x < minimo)
            minimo = x;
        if (x > maximo)
            maximo = x;
    }
    p.media = soma/n;
    p.minimo = minimo;
    p.maximo = maximo;

    soma = 0;
    int variancia = 0;
    for(int i = 0; i < n; i++){
        soma += pow((p.notas[i] - p.media), 2);
    }
    variancia = soma/(n-1);
                    
    p.variancia = variancia;           
    

    // Imprimindo
    //for (int i = 0; i < n; i++){
    //    printf("%lf", p.notas[i]);
    //}
    printf("%.2lf ",p.media);
    printf("%.2lf ",p.minimo);
    printf("%.2lf ",p.maximo);
    printf("%.2lf\n",p.variancia);
    


    return 0;
}