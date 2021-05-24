s = "hansei is the best, but he is not the principal."

vowel=["a","e","i","o","u","A","E","I","O","U"]

cont = 0

for i in vowel:
    for j in s:
        if i==j:
            cont += 1


print(f"모음의 갯수: {cont}개")