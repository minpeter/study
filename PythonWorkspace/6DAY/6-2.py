gradeDict = {"S":5,"G":10,"V":15}

price = 10000
grade = "G"

def solution(price, grade):
  return int(float(price) * float(gradeDict[grade]) /100.0)

print(price - solution(price,grade))
