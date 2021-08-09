#include<stdio.h>

int plus(int in1, int in2);
int sub(int in1, int in2);
int mul(int in1, int in2);
int div(int in1, int in2);

int main(){
    int num1=7, num2=13;
    printf("더한값: %d\n",plus(num1,num2));
    printf("뺀값: %d\n",sub(num1,num2));
    printf("곱한값: %d\n",mul(num1,num2));
    printf("나눈값: %d\n",div(num1,num2));
}

int plus(int in1, int in2){
    return in1 + in2;
}
int sub(int in1, int in2){
    return in1 - in2;
}
int mul(int in1, int in2){
    return in1 * in2;
}
int div(int in1, int in2){
    return in1 / in2;
}