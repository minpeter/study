#include <stdio.h>
void main()
{
	int i,j,k;
	int size=5;
	for (i=size; i>=0; i--) //loop decrease
	{
		for (j=0; j<i; j++)
		{
			printf("i\t");
		}
		for (k=0; k<size-j; k++)
		{
			printf("*\t");
		}
		printf("\n");
	}
}

/*
i       i       i       i       i
i       i       i       i       *
i       i       i       *       *
i       i       *       *       *
i       *       *       *       *
*       *       *       *       *

*/
