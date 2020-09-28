#include <iostream>
#include <vector>

using namespace std;


int insertionSort(vector<int> v){
    for (int i = 1; i < v.size(); i++){
        int key = v[i];
        int j = i - 1;
        while (j >= 0 && v[j] > key){
            v[j+1] = v[j];
            j-=1;
        }
        v[j+1] = key;
    }
     for (int i = 0; i < v.size(); i++){
        cout << v[i] << endl;
    }
}


int main(){
    vector<int> v;
    v = {2,5,11,7,1,13,19,17};
    cout << insertionSort(v);

    return 0;
}
