def vf(*x):
    temp = 0
    for i in x:
        temp += i
    return temp


print(f"가변인자를 전부 더한 값: {vf(1,2,3,4,5,6,7)}")