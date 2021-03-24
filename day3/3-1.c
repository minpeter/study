#include <stdio.h>
int main(){

    int a[10] = {11,22,33,44,55,66,77,88,99,110};
    int i;

    for (i=0; i<sizeof(a)/sizeof(int); i++)
    {
        a[i] *= 2;
    }

    for (i=0; i<sizeof(a)/sizeof(int); i++)
    {
        printf("%d\n", a[i]);
    }

    return 0;
}