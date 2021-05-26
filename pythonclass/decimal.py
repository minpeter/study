number =  int(input("소수인지 판별할 숫자를 입력하세요: "))

cont = 0

for i in range(1, number+1):
    if number%i==0:
        cont+=1
    
if cont==2:
    print("소수입니다")

else:
    print("소수가 아닙니다.")