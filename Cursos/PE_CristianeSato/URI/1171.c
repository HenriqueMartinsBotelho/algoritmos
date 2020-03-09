#include <stdio.h>
int main()
{
   int frequencia[2010] = {0};
   int n, x;
   scanf("%d", &n);
   for(int i = 0; i < n; i++) {
      scanf("%d", &x);
      frequencia[x]++;
   }
   for (int i = 1; i <= 2000; i++){
      if(frequencia[i] > 0)
         printf("%d aparece %d vez(es)\n", i, frequencia[i]);
   }
   return 0;
}
