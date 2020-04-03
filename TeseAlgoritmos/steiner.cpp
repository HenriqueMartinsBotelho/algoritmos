#include <iostream>
#include <vector>    



using namespace std;


typedef double T;
struct pt {
    T x, y;
    pt operator+(pt p) {return {x+p.x, y+p.y};}
    pt operator-(pt p) {return {x-p.x, y-p.y};}
    pt operator*(T d) {return {x*d, y*d};}
    pt operator/(T d) {return {x/d, y/d};} // only for floatingpoint
};
  
void prim(Point points[], int n){
    
}


int main(){

    /*
    vector<double> V[7] = {{78.0, 75.0},{30.0, 76.0}, {38.0, 21.0}, {70.0, 26.0}, {72.0, 68.0},{36.0, 66.0}, {49.0, 46.0}};



    struct Point{
        int x;
        int y;
        struct Point* p;
    };

    struct Point* pontos[7];
    for (int i = 0; i < 7; ++i) {
        pontos[i] = (struct Point*)malloc(sizeof(struct Point));
        pontos[i]->x = V[i][0];
        pontos[i]->y = V[i][1];
    }

    
    for (int i = 0; i < 7; i++){
        printf("%d %d \n", pontos[i]->x, pontos[i]->y);
    }*/
    
 Point points[] = {{0, 3}, {1, 1}, {2, 2}, {4, 4}, {0, 0}, {1, 2}, {3, 1}, {3, 3}};
 int n = sizeof(points)/sizeof(points[0]);  
 void prim(Point points[], int n); 


// Algoritmo de Prim









}

