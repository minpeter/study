#include<stdio.h>

int plus(int a,int b);
int main(){
    int num1 = 10, num2 = 5;
    printf("결과는 %d입니다\n",plus(num1,num2));
}

int plus(int a,int b){
    return a + b;
}