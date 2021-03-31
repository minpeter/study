#include <stdio.h>
int ascend(int* Pointer, int count);

int main(){
    int Arr[] = {4, 2, 6, 1, 8, 10, 7, 9, 5, 3};
    int count = sizeof(Arr)/sizeof(int);

    ascend(Arr, count);
    return 0;
}


int ascend(int* Pointer, int count){
    int i,j;
    int tmp;
    
    for(i=0; i<count; i++){         
        for(j=i+1; j<count; j++){  
            if(*(Pointer+i)>*(Pointer+j)){     
                tmp = *(Pointer+i);    
                *(Pointer+i) = *(Pointer+j);
                *(Pointer+j) = tmp;
            }
        }
    }
    int num;
    
    for(num=0; num<count; num++)      
        printf("array[%d]: %d \n", num, *(Pointer+num));   
    return 0;    
}