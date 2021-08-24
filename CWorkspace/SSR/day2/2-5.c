#include <stdio.h>
int main()
{
    int i, j;
    int result=0;
    for(i=3; i<7; i++)
    {
        for(j=1; j<10; j++)
        {
            result = i*j;
            printf("%d * %d = %d\n",i,j,result);
        }
        printf("-------------\n");
    }
	return 0;
}
