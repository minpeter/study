#include<stdio.h>
int main(){
    int num;
    printf("NUM: ");
    scanf("%d",&num);
    int *pointer = &num;
    printf("\n");
    printf("[POINTER VALUES: 0x%X]\n",pointer);
    printf("[POINTER PHYSICAL ADDR: 0x%X]\n",&pointer);
    printf("[POINTER VALUES LOCATED VALUE IS ADDRED: %d]\n",*pointer);
    printf("[NUM ADDR: 0x%X]\n",&num);
    printf("[NUM VALUES: %d]\n",num);
}