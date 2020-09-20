#include "calculator.h"

void main(void){

	int a,b;

	printf("첫번째 값을 입력하세요:");
	scanf("%d",&a);
	
	printf("두번째 값을 입력하세요:");
	scanf("%d",&b);

	int p = plus(a,b);
	int m = minus(a,b);

	printf("더한 결과: %d\n",p);
	printf("뺀 결과: %d\n",m);
}
