#include <stdio.h>
#include <string.h>

int verifica(char A[], char B[]){

int ok = 0;
        for (int j = (strlen(A) - strlen(B)), i = 0; j < strlen(A), i < strlen(B); j++, i++)
        {
            if (A[j] == B[i])
            {
                ok = 1;
            }
            else
            {
                ok = 0;
                return ok;
            }
            
            
        }
    
    return ok;

}

int main(){
    char A[1001], B[1001];
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%s %s", A, B);
        if (verifica(A,B) == 1)
            printf("encaixa\n");
        else
            printf("nao encaixa\n");
    }
    
    return 0;
    
}