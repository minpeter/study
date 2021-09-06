calculator : plus.o minus.o main.o
	gcc -o calculator plus.o minus.o main.o

plus.o : plus.c
	gcc -c -o plus.o plus.c

minus.o : minus.c
	gcc -c -o minus.o minus.c

main.o : main.c
	gcc -c -o main.o main.c

clean :
	rm *.o calculator
