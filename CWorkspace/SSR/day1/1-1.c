#include<stdio.h>

int main(){
	int num1, num2;
	
	printf("첫번째 정수값 입력값: ");
	scanf("%d", &num1);
	printf("두번째 정수값 입력값: ");
	scanf("%d", &num2);
	printf("각각 자료형의 크기는 %d와 %d 입니다.\n", sizeof(num1), sizeof(num2));

	return 0;
}