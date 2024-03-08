#include <string>
#include <vector>
#include <sstream>
using namespace std;

int solution(string binomial) {
    int answer = 0;
    int a, b;
    char op;
    stringstream st(binomial);
    st >> a >> op >> b;
    switch(op){
        case '+':
            answer = a+b;
            break;
        case '-':
            answer = a-b;
            break;
        case '*':
            answer = a*b;
            break;
        }
    
    return answer;
}