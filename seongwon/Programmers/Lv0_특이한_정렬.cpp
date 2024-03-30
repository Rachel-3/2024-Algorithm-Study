#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

bool cmp(int a, int b) {     //절대값일때 조건 추가
    if (abs(a) == abs(b)) {
        return a > b;
    }
    return abs(a) < abs(b); 
}

vector<int> solution(vector<int> numlist, int n) {
    vector<int> answer;
    for(int i : numlist){
        answer.push_back(i-n);  //n과의 거리차이 넣음
    }
    sort(answer.begin(), answer.end(), cmp);
    for(int& i : answer){
        i +=n;
    }
    return answer;
}
