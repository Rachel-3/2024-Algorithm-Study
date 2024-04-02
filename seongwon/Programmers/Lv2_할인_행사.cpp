#include <string>
#include <vector>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    for(int i = 0; i < discount.size()-9; i++){
        vector<int>cnt = number;
        for(int j = i; j < i+10; j++){
            for(int k = 0; k < want.size(); k++){
                if(want[k] == discount[j]){
                    cnt[k]--;
                }
            }
        }
        vector<int> t(number.size(), 0);
        if(t == cnt)
            answer++;
    }
    return answer;
}
