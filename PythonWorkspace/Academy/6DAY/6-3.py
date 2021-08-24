arr1 = [1,2,3,4]

def solution(arr1):
    arr2 = []
    for i in range(len(arr1)):
        arr2.append(arr1[len(arr1)-i-1])
    return arr2
    
print(solution(arr1))