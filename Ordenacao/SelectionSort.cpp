#include <iostream>

using namespace std;

void SelectionSort(int n, int v[]);

int main(int argc, const char** argv){
    
    int v[10] = {2,3,5,4,1,9,8,7,6,0};
    SelectionSort(10, v);

    for (size_t i = 0; i < 10; i++){
      cout << v[i] << endl;
    }
    
    return 0;
}

void SelectionSort(int n, int v[]){
  int i, j, min, aux;
  for (i = 0; i < (n-1); i++){
     min = i;
     for (j = (i+1); j < n; j++){
       if(v[j] < v[min]) 
         min = j;
     }
     if (v[i] != v[min]) {
       aux = v[i];
       v[i] = v[min];
       v[min] = aux;
     }
  }
}

