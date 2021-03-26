#include<stdio.h>

int plusprint(int input_number);
int main(){
    int num;
    printf("1부터 입력한값까지 더함:");
    scanf("%d",&num);
    plusprint(num);
}

int plusprint(int input_number){
    int sum = 0, i;

	for(i=1; i<=input_number; i++){
		sum += i;
	}

	printf("1부터 %d까지의 합 : %d\n", input_number, sum);
}