#include <stdio.h>
int main()
{
	int standard = 173, height = 168;
	if (standard > height)
	{
		printf("평균이하");
	}
	else if (standard==height)
	{
		printf("평균");
	}
    else
    {
         printf("평균이상");
    }
	return 0;
}
