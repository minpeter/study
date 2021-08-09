shirt_size = ["xs","xs","s"]
shirtSizedict = {
    "xs":0,"s":0,"m":0,"l":0,"xl":0,"xxl":0
    }
    
def solution(shirtSize):
    for item in shirtSize:
        shirtSizedict[item] = shirtSizedict[item] + 1
    print(shirtSizedict)
    return list(shirtSizedict.values())

print(solution(shirt_size))