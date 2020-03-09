#include <iostream>

using namespace std;

void BubbleSort(int n, int v[]){
    int i, continua, aux, fim = n;
    do{
        continua = 0;
        for (size_t i = 0; i < fim-1; i++){
            if (v[i] > v[i+1]){
                aux = v[i];
                v[i] = v[i+1];
                v[i+1] = aux;
                continua = 1;
            }
        }
        fim--;
    } while (continua != 0);
}

int main(int argc, char const *argv[]){
    
    int v[10] = {2,3,5,4,1,9,8,7,6,0};
    BubbleSort(10, v);
    for (size_t i = 0; i < 10; i++){
      cout << v[i] << endl;
    }

    return 0;
}
