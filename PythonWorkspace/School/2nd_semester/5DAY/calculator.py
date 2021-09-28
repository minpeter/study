import cakulator

a = int(input("첫번째 숫자를 입력하세요: "))

b = int(input("첫번째 숫자를 입력하세요: "))

print(f"{a} + {b} = {cakulator.add(a,b)}")
print(f"{a} - {b} = {cakulator.sub(a,b)}")
print(f"{a} * {b} = {cakulator.mul(a,b)}")
print(f"{a} / {b} = {cakulator.div(a,b)}")