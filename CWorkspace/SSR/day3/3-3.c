#include <stdio.h>
void main(){
    int b, m;
    int a[6] = {10, 20, 30, 40, 5, 60};
    m=a[0];
    for(b=1; b<=5; b++)
        if(a[b]<m) m=a[b];
    printf("%d \n", m);
}

//결과는 5 따라서 2번이 정답