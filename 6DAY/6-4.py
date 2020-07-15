def solution(number):
    c = 0
    for i in range(number):
        if i % 3 == 0:
            c = c + 1
    return c

print(solution(40))