#include<stdio.h>
int main(){
    int a,b,c,d,e;
    a =1;
    b=2;
    c=3;
    d=4;
    e=5;


    int *POINT[5];
    
    POINT[0] = &a;
    POINT[1] = &b;
    printf("%x:%d\n",POINT[0],*POINT[0]);
    printf("%x:%d\n",POINT[1],*POINT[1]);
    return 0;
}