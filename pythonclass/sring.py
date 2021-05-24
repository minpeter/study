a = input("-을 포함한 전화번호 입력: ")

print("-를 제외한 전화번호: ", end="")
for i in a:
    if i != '-' and i != ' ':
        print(i, end="")
