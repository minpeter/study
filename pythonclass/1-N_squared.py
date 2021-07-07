number = int(input("N의 값을 입력하세요: "))
total = 0
for i in range(1, number+1, 2):
    total += i ** 3
    print(f"{i}*{i}*{i}", end='')
    if number % 2 == 0:
        if i != number-1:
            print(" + ",end='')
    else:
        if i != number:
            print(" + ",end='')
print(f" = {total}")