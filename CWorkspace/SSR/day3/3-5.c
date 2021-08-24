#include <stdio.h>
int main(){
    int num[10];
    int i,j,count;

    int sm;

    for(i=0; i<10; i++){
        printf("%d번째 정수를 입력하세요: ",i+1);
        scanf("%d",&num[i]);
    }

    for(i=0; i<10; i++){
        count = 0;
        sm = 0;

        for(j=0; j<10; j++) {
            if(num[i] == num[j]) {
                count++;
            }
        }
        for(j=0; j<i; j++) {
            if(num[i] == num[j]) {
                sm = 1;
            }
        }
        if(sm == 0) {
            printf("%d\t%d\n",num[i],count);
        }

    }
    return 0;
}