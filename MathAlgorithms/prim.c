#include <stdio.h>
#include <math.h>
#define size 3

// Criar uma listas para armazenar os vértices escolhidos
// Criar a funcao de prim que recebe as coordenadas de todos os vértices pega um primeiro vértice V
// qualquer acha qual o vértice M da listas 'restantes' mais próximo desse vértice e armazena M em escolhidos.
// a segunda interação vai achar o vértice mais próximo de V ou de M. Seja K esse vértice a próxima interação var achar
// o vértice mais próximo de V,M ou K. Lembremo-nos de remover os vértices que vão para escolhidos da 'restantes'.

typedef struct Point{
    double x;
    double y;
}Point;



//Imprime elementos de um array
void printArray(double arr[], double tamanho){
    int i;
    for (i=0; i < tamanho; i++)
        printf("%f ", arr[i]);
    printf("\n");
}
//Imprime elementos de um array struct
void printStructArray(struct Point vec[], double tamanho){
    int i;
    for (i=0; i < tamanho; i++)
        printf("{ %f %f}", vec[i].x, vec[i].y);
    printf("\n");
}
//Imprime matriz
void printMatrix (size_t rows, size_t columns, double matrix[rows][columns]){
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns ; ++j) {
            printf(" %f",matrix[i][j]);
        }
        printf("\n");
    }
}


//Calcula a distância Euclidiana entre dois pontos.
double distEuclid(double p1[1][2], double p2[1][2]){
    double x1,x2,y1,y2;
    x1 = p1[0][0];
    x2 = p2[0][0];
    y1 = p1[0][1];
    y2 = p2[0][1];

    double dist = sqrt(pow((x1 - x2),2) + pow((y1 - y2),2));
    return dist;
}

//Calcula a distância Euclidiana entre dois Points
double ndistEuclid(struct Point* a, struct Point* b ){
    double x1,x2,y1,y2;
    x1 = a->x;
    x2 = b->x;
    y1 = a->y;
    y2 = b->y;

    double dist = sqrt(pow((x1 - x2),2) + pow((y1 - y2),2));
    return dist;
}

int prim(struct Point todos[]){

    struct Point restantes[size];
    struct Point escolhidos[size];

    // fazendo uma copia de todos para restantes
    for (int i = 0; i < size ; ++i) {
        restantes[i] = todos[i];
    }

    escolhidos[0] = todos[1];
    //printf("escol = (%f, %f)\n",escolhidos[0].x,escolhidos[0].y);

    double menor = 100000;
    double distancia = 20;

    for(size_t k = 0; k < size; k++){        
        for(size_t l = 0; l < size; l++){    
            //if ( ndistEuclid(&escolhidos[k],&restantes[l]) < menor ) {
                //printf("Distância entre o ponto")
            //}
           distancia = ndistEuclid(&escolhidos[k],&restantes[l]);
           printf("Distancia entre o ponto (%f,%f) e (%f,%f) eh de %f\n",
           escolhidos[k].x,
           escolhidos[k].y,
           restantes[l].x,
           restantes[l].y,
           distancia);
        }   
    }
    



    printStructArray(todos,size);
    printStructArray(restantes,size);
    printStructArray(escolhidos,size);

    return 0;
};



int main(){

    double v1[1][2] = {2,3};
    double v2[1][2] = {4,5};
    double v3[3][2] = {1,2,3,4,5,6};

     Point pontos[size] = {{2,3},{4,5},{50,60}};
    //printf("ponto 0 = %f\n", pontos[0].y);
    prim(pontos);

    //double ndistancia = ndistEuclid(&pontos[0],&pontos[1]);
    //printf("%f\n",ndistancia);

}


