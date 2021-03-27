#include<stdio.h>

int squaredSub(int n1, int n2);
int main(){

    int num1, num2;

    printf("첫번째 값을 입력하세요: ");
    scanf("%d",&num1);
    printf("두번째 값을 입력하세요: ");
    scanf("%d",&num2);
    
    if (num1 < 0 || num2 <0){
        printf("모든값을 양수로 입력해주세요\n");
    }
    else{
        squaredSub(num1,num2);
    }

    return 0;
}

int squaredSub(int n1,int n2){
    int result;

    return result;
}