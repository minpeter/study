#include<stdio.h>
int main(){
    int NUM = 4;
    int *POINT;
    POINT = &NUM;
    printf("POINT의 값을 주소로 하는 곳의 값: %d \n POINT의 값을 주소로 하는 곳의 값: %d \n",*POINT,POINT);
    return 0;
}