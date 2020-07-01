def bmi(height, weight):
	result = weight/height
	if(result < 18.5):
		return "저체중"
	elif(result >= 18.5 and result <= 22.9):
		return "정상체중"
	else:
		return "과체중"



H = int(input("키를 입력하세요:"))
W = int(input("몸무게를 입력하세요:"))

print(bmi(H,W))
