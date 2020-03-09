#include <stdio.h>
#include <math.h>
#define size 3


//Calcula a distância Euclidiana entre dois pontos.
double distEuclid(double p1[], double p2[]){
    double x1,x2,y1,y2;
    x1 = p1[0];
    x2 = p2[0];
    y1 = p1[1];
    y2 = p2[1];

    double dist = sqrt(pow((x1 - x2),2) + pow((y1 - y2),2));
    return dist;
}

int main(){
    //int menor = 10000;
    int maior = 0;
    int vec[3] = {2,30,4};
    int vec2[4] = {5,6,70,8};
   
    for(size_t i = 0; i < 3; i++){    
        for(size_t j = 0; j < 4; j++){
            printf("vec[%d] = %d e vev2[%d] = %d\n",i,vec[i],j,vec[j]);
            if( (vec[i] + vec2[j]) > maior )
                maior = (vec[i] + vec2[j]);
        }  
    }
    //double v1[2] = {2,30};
    //double v2[2] = {4,5};
    //printf("%f",distEuclid(v1,v2));
    printf("%d",maior);
}
