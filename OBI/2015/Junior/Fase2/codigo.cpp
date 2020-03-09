#include <iostream>

using namespace std;

int main(){

    int n, x;
    cin >> n;
    int v[n];
    
    for (int i = 0; i < n; i++){
        cin >> x;
        v[i] = x;
    }
    
    int c = 0;
    for (int i = 0; i < n-2; i++){
        if(v[i] == 1 & v[i+1] == 0 & v[i+2] == 0)
            c++;
    }
    
    cout << c << "\n";


    return 0;
}