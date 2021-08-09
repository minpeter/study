#include <stdio.h>
void main()
{
	int i,j;
	for (i=5; i>=0; i--) //loop decrease
	{
		for (j=0; j<i; j++)
		{
			printf("*\t");
		}
		printf("\n");
	}
}

/*
*	*	*	*	*
*	*	*	*
*	*	*
*	*
*

*/
