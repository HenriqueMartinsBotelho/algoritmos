#include <stdio.h>

int main(){
    int a,b,c, pa, pb, pc;

    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&c);

    if (a < b && a < c){
        pa = 1;
        if (b < c){
            pb = 2;
            pc = 3;
        }
        else{
            pb = 3;
            pc = 2;
        }
    }
    else{
        if (b < a && b  < c){
            pb = 1;
            if (a < c){
                pa = 2;
                pc = 3;
            }
            else{
                pc = 2;
                pb = 3;
            }
        }
        else{
            pc = 1;
            if (b < a){
                pb = 2;
                pa = 3;
            }
            else{
                pb = 3;
                pa = 2;
            }
        }
        
    }

    printf("%d\n",pa);
    printf("%d\n",pb);
    printf("%d\n",pc);

}