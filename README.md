# Makefile-Practice
makefile 생성 연습용으로 만든 계산기


파일 의존성
  
 calculator
  ▷ main.o
    ▶ main.c (calculator.h)
  ▷ plus.o
    ▶ plus.c (calculator.h)
  ▷ minus.o
    ▶ minus.c (calculator.h)
    
    
    
    
    
사용법
1. git clone https://github.com/minpeter/Makefile-Practice.git
2. cd Makefile-Practice
3. make
3. ./calculator
