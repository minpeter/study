#include <stdio.h>
void main()
{
	int i,j,k;
	int size=5; //The size of the rectangle
	for (i=0; i<=size; i++)
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
*       *       *       *       *
i       *       *       *       *
i       i       *       *       *
i       i       i       *       *
i       i       i       i       *
i       i       i       i       i

*/
