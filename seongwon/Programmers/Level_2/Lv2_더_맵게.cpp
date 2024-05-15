#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <algorithm>
using namespace std;
int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> pq(scoville.begin(), scoville.end());
    while(pq.top() < K && pq.size()>1){
        int tmp1 = pq.top();
        pq.pop();
        int tmp2 = pq.top();
        pq.pop();
        pq.push(tmp1+(tmp2*2));
        answer++;
    }
    if(pq.top() < K){
        answer = -1;
    }
    return answer;
}
