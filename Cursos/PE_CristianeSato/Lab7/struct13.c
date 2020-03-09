/* Crie uma struct aluno_s com campos:
- int nota: representando a nota em uma prova
- int ano: o ano de ingresso do aluno
Defina um tipo aluno para essa struct.

Entrada:
A primeira linha é composta de um inteiro n.
As n linhas são referentes aos dados de cada aluno. Cada linha tem 2 valores: o primeiro representando a nota do aluno (de 0 a 100) e o segundo o ano de ingresso do aluno.
Exemplo: */

#include <stdio.h>

typedef struct aluno_s{
    int nota;
    int ano;
}aluno;


typedef struct vetor_s{
    int qt;
    aluno *alunos;
}vetor;

int main() {

    int n;
    scanf("%d", &n); 
    
    vetor v = {n};
    v.alunos = malloc(sizeof(aluno)*n);
    vetor *va = &v;

    int nota, ano;
    scanf("%d %d\n", nota, ano);
    aluno a = {nota, ano};
    for (int i = 0; i < n; i++){
        va->alunos[0] = a;
    }
    

  return 0;
}