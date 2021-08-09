def solution(number):
    count = 0
    for i in range(1,number+1):
        ic = i
        while ic != 0:
            if(ic%10==3 or ic%10==6 or ic%10==9):
                count += 1
            ic = ic // 10
    return count
        

print(solution(int(input("369게임 횟수: "))))