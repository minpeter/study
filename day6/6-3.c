#include<stdio.h>
int main(){
   int arr[10] = {1,2,3,4,5,6,7,8,9,10};
   int i;

   int *p =arr;
   printf("ARR: [ ");
   for(i=0; i<10; i++){
       printf("%d ", *(p+i));
   }
   printf("]\n");
}