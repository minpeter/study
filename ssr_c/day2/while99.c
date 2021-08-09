#include <stdio.h>
int main()
{
    int i=2, j;
    int result=0;
    while(i<10)
    {
        
        while(j<10)
        {
            result = i*j;
            printf("%d * %d = %d\n",i,j,result);
            j++;
        }
        printf("-------------\n");
        j = 1;
        i++;
    }
	return 0;
}
