#include <stdio.h>

int main(){

	int i = 13, j=5;
	if (-1) putchar('A');
	if (1) putchar('B');
	if (13) putchar('C');
	if (0) putchar('D');
	if (i>j)
	{
		putchar('E');
		putchar('D');
	}
	if (i<j)
		putchar('G');
	putchar('H');
	return 0;
}
