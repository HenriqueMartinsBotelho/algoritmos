#include <stdio.h>

int main(){

	double A,B,C, x1,x2,y1,y2;
	char opcao;

	printf("1) Calcular as equacoes usando coeficiente angular e um ponto\n");
	printf("2) Calcular as equacoes usando dois pontos\n");
	scanf(" %d",&opcao);

	
	if(opcao == 1){
		printf("111");
	}

	if(opcao == 2){
		//(y1 - y2)x + (x2 - x1)y + (x1y2 - x2y1) = 0
		printf("x1:");
		scanf("%lf",&x1);
		printf("y1:");
		scanf("%lf",&y1);
		printf("x2:");
		scanf("%lf",&x2);
		printf("y2:");
		scanf("%lf",&y2);



		A = y1 - y2;
		B = x2 - x1;
		C = x1 * y2 - x2 * y1;
		printf("Uma equacao da reta que passa pelos pontos: (%.1lf,%.1lf) e (%.1lf,%.1lf)",x1,y1,x2,y2);
		printf(" eh dada por: \n\n");
		printf("      %.2lfx + %.2lfy + %.2lf = 0\n\n",A,B,C); 
		printf("Qualquer outra equacao da forma: k(%.2lfx + %.2lfy + %.2lf = 0)",A,B,C);
	        printf(" para k inteiro tambem passa pelos mesmos pontos\n");

	}


	return 0;
}
