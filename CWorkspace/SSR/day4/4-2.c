#include<stdio.h>

int totalScore(int grade[]);
int main(){
    int stScore1[5] = {87,92,95,91,0};
    int stScore2[5] = {67,95,76,88,0};
    int stScore3[5] = {77,88,81,87,0};
    int stScore4[5] = {78,81,96,76,0};

    stScore1[4] = totalScore(stScore1);
    printf("1번 학생의 총점은 %d",stScore1[4]);
    return 0;

}


int totalScore(int grade[]){

    int countSubject, sum = 0;
    for (countSubject = 0; countSubject <4; countSubject++){
        sum = sum + grade[countSubject];
    }
    return sum;
}
