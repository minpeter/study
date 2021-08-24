#include<stdio.h>

int square(int n);
int main(){

    int num;

    printf("숫자 사각형을 출력할 값을 입력하세요: ");
    scanf("%d",&num);
    
    if (num <= 99){
        square(num);
    }
    else{
        printf("100 미만의 숫자만 입력해주세요\n");
    }

    return 0;
}

int square(int n){
    int i,j,count = 1;
    for(i=0; i<n; i++){
        for(j=0; j<n; j++){
            printf("%d ",count);
            count += 1;
        }
        printf("\n");
    }

    return 0;
}