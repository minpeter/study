#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[])
{
	int i;
	
	printf("argc = %d개 \n", argc);
	
	for (i=0; i<argc; i++){
		printf("argv[%d] = %s\n", i, argv[i]);
		if (argv[i] == 3) {
			printf("you use option");
		}
	}
	exit(0);
}

