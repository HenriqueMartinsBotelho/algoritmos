Address: &A[i] e (A + i) significam a mesma coisa
Value: A[i] e *(A + i) significam a mesma coisa 

Operações com ponteiros
Suponhamos dois ponteiros inicializados p1 e p2. Podemos fazer dois tipos de atribuição entre eles:

p1 = p2;
Esse primeiro exemplo fará com que p1 aponte para o mesmo lugar que p2. Ou seja, usar p1 será equivalente a usar p2 após essa atribuição.

*p1 = *p2;
Nesse segundo caso, estamos a igualar os valores apontados pelos dois ponteiros: alteraremos o valor apontado por p1 para o valor apontado por p2.

Agora vamos dar mais alguns exemplos com o ponteiro p:

p++;
Aqui estamos a incrementar o ponteiro. Quando incrementamos um ponteiro ele passa a apontar para o próximo valor do mesmo tipo em relação ao valor para o qual o ponteiro aponta. Isto é, se temos um ponteiro para um inteiro e o incrementamos, ele passa a apontar para o próximo inteiro. Note que o incremento não ocorre byte-a-byte!

(*p)++;
Aqui, colocamos *p entre parênteses para especificar que queremos alterar o valor apontado por p. Ou seja, aqui iremos incrementar o conteúdo da variável apontada pelo ponteiro p.

*p++
Neste caso, o efeito não é tão claro quanto nos outros exemplos. A precedência do operador ++ sobre o operador * faz com que a expressão seja equivalente a (*p)++. O valor atual de p é retornado ao operador *, e o valor de p é incrementado. Ou seja, obtemos o valor atual do ponteiro e já o fazemos apontar para o próximo valor.

x = *(p + 15);
Esta linha atribui a uma variável x o conteúdo do décimo-quinto inteiro adiante daquele apontado por p. Por exemplo, suponhamos que tivéssemos uma série de variáveis i0, i1, i2, … i15 e que p apontasse para i0. Nossa variável x receberia o valor de i15.

Tente acompanhar este exemplo dos dois tipos de atribuição de ponteiros:

int *a, *b, c = 4, d = 2;
a = &c;        // a apontará para c
b = &d;        // b apontará para d
*b = 8;        // altero o valor existente na variavel d
*a = *b;       // copio o valor de d (apontado por b)
                 // para c (apontado por a)
*a = 1;        // altero o valor da variável c
b = a;         // b aponta para o mesmo lugar que a,
                 // ou seja, para c
*b = 0;        // altero o valor de c






/* ponteiro para memória que será alocada */
int *p;
int i;

/* alocar 10 elementos inteiros, ou seja, ( sizeof (int) * 10 ) */
p = (int *) malloc(sizeof(int) * 10);
      
// Atribuindo e imprimindo valores ao vetor   
for(i = 0; i < 10; i++) {
  p[i] = i;
  printf ("%d\n", p[i]);
}

/* libera a memória alocada por malloc */
free (p);


 /* Vetores e ponteiros */

int vetor [4] = {10, 20, 30, 40};
int *p = vetor;

printf("%d", *p); // Imprime 10

int *p2 = &vetor[2];
printf("%d", *p2); // Imprime 30

++p;

printf("%p", *p); // Imprime 20

*(p + 2) = 50; // Altera o terceiro elemento do vetor para 50


// Swap

void swap(int *xp, int *yp) 
{ 
    int temp = *xp; 
    *xp = *yp; 
    *yp = temp; 
} 
  
int main() 
{ 
    int x, y; 
    printf("Enter Value of x "); 
    scanf("%d", &x); 
    printf("\nEnter Value of y "); 
    scanf("%d", &y); 
    swap(&x, &y); 
    printf("\nAfter Swapping: x = %d, y = %d", x, y); 
    return 0; 
} 