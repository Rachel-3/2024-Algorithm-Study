#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    int len = citations.size();
    vector<int> cnt(len + 1, 0);
    int h = 0;
    
    for(int i = 0; i < len; i++){   //논문의 수 카운트
        if(citations[i] >= len) cnt[len]++;
        else cnt[citations[i]]++;
    }

    for(int i = len; i >= 0; i--){
        h += cnt[i]; // 현재 인용 횟수 이상인 논문의 수 +
        if(h >= i){ // 인용 횟수가 현재 논문의 수 이상이면 h업데이트하고 종료
            answer = i;
            break;
        }
    }

    return answer;
}
