def gugudan(n):
    print(n, "단을 출력합니다.")
    for i in range(1, 10):
        print(n, " X ", i, " = ", n*i)

    if __name__ == "__main__": # 이 파일이 직접 실행된 경우에만 실행
        gugudan(3)