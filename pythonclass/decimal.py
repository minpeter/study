number =  int(input("소수인지 판별할 숫자를 입력하세요: "))

cont = 0

for i in range(2, number):
    if number%i==0:
        cont==1
    
if cont==0:
    print("소수입니다")

else:
    print("소수가 아닙니다.")