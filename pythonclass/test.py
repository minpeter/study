x = input("주민번호를 ******-******* 형식으로 입력하세요: ")
if x[7] == "3":
    print("남자")
elif x[7] == "4":
    print("여자")
else:
    print("주민번호를 확인해주세요")
