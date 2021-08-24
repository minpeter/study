total = 0
for i in range(1, int(input("N의 값을 입력하세요: "))+1, 2):
    print(f"{' + ' if i!=1 else ''}", end='')
    total += i ** 3
    print(f"{i}*{i}*{i}", end='')
print(f" = {total}")