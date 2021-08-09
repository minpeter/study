#include<stdio.h>

void main() {
    int A[5] = {1,2,3,4,5};

    int *dd = &A;


    printf("%d",A[2]);
    printf("%d",dd);
    printf("%d",&A);

    printf("\n\n%d",*dd+3);
}