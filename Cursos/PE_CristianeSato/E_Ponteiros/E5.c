//Certo

#include<stdio.h>
#include<stdlib.h>


int * combina(int *v, int *w, int n, int m);


int main() {
 int n, m, i;
 int *v, *w, *r;
 scanf("%d %d", &n, &m);
 v = malloc(sizeof(int) * n);
 w = malloc(sizeof(int) * m);
 for(i = 0; i < n; i++) {
 scanf("%d", &v[i]);
 }
 for(i = 0; i < m ; i++) {
 scanf("%d", &w[i]);
 }
 r = combina(v, w, n, m);
 for(i = 0; i < n+m-1; i++) {
 printf("%d ", r[i]);
 }
 printf("%d\n", r[n+m-1]);
 free(v);
 free(w);
}


int * combina(int *v, int *w, int n, int m){
    int *z = (int *)malloc(sizeof(int)*(n + m));
    for (int i = 0; i < n; i++){
        z[i] = v[i];
    }
    
    int *inverso = (int *)malloc(sizeof(int)*m);
    for (int j = 0; j < m; j++){
        inverso[j] = w[m - j - 1];
    }
    
    for (int h = n, l = 0; h < (n+m); h++, l++){
        z[h] = inverso[l];
    }
    

    return z;
}