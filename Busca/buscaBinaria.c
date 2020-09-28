#include <iostream>
#include <vector>

using namespace std;


int binary_search(vector<int>  v, int x){
    int esquerda = 0;
    int direita = v.size() - 1;
    int meio;
    while (esquerda <= direita){
        meio = (direita - esquerda)/2;
        if (x == v[meio])
            return meio;
        if (x < v[meio])
            direita = meio - 1;
        else
            esquerda = meio + 1;
    }
    return -1;
}



int main(){
    vector<int> v;
    v = {2,3,5,7,11,13,17,19};
    cout << binary_search(v,17);
    
    return 0;
}
