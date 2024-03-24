#include <iostream>
using namespace std;

int solution(int n, int a, int b)
{
    int answer = 0;
    while(a!=b){    //a==b==1일때 만남
        a = (a+1) >> 1; // 홀수일 수 있으니 +1 후 나누기 2
        b = (b+1) >> 1;
        answer++;
    }
    return answer;
}
