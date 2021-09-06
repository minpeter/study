import hello_func, greeting_func

def main():
    print("insa_func 모듈입니다")
    print("__name__ : ", __name__) # __name__ 변수의 값은 __main__ 이라는 값이 나옴
    hello_func.hello()
    greeting_func.greeting()

main()