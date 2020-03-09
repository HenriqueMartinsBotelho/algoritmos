#include <stdio.h>
#include <stdlib.h>

void imprime_matriz( int **matriz);
int soma(int **matriz, int l, int c);

void imprime_matriz( int **matriz){
  int i, k;
	for (i=0; i<10; i++){
		printf("\n");
		for (k=0; k<10; k++){
			if(matriz[i][k] != (char)'*'){
				printf(" %d ", matriz[i][k]);
			}
			else {
				printf(" %c ", matriz[i][k]);
			}
		}
	}
}


int entorno(int **matriz, int l, int c){
  int i, j;
  int soma = 0;	
  if (matriz[l-1][c-1] == '*')
   soma++;
  if (matriz[i-1][j] == '*')
   soma++;              
  if (matriz[i-1][j+1] == '*')
   soma++;
   if (matriz[i][j-1] == '*')
   soma++;
    if (matriz[i][j+1] == '*')
    soma++;
    if (matriz[i+1][j+1] == '*')
    soma++;
return soma;	
}

int main ()
{	
	int i, k;
	int l, c;
	char simb = '*';
	int *matriz = (int)malloc(sizeof(int)*10);

	for (i=0; i<10; i++){
		matriz[i] = (int*)malloc(sizeof(int*)*10);
	}


	for (i=0; i<10; i++){
		for (k=0; k<10; k++){
			matriz[i][k] = 0;
		}
	}

	for (i=0; i<10; i++){
		scanf ("%d %d", &l, &c);
		for (k=0; k<10; k++){
			matriz[l][c] = (char) simb;
			soma(matriz, l, c);
		}
	}

	imprime_matriz(matriz);

	
	for(i=0; i<10; i++){
		free(matriz[i]);
	}
	free(matriz);
	return 0;
}
