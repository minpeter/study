#include<stdio.h>

int factorial(int n);
int main(){

    int num;

    printf("팩토리얼을 구할 값을 입력하세요: ");
    scanf("%d",&num);
    printf("%d 의 팩토리얼 값은 %d 입니다.\n", num, factorial(num));
    return 0;
}

int factorial(int n){
    if (n == 1)
        return 1;
    
    return n * factorial(n - 1);
}