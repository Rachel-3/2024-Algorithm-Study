#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> arr;

    for (int i = 0; i < progresses.size(); i++) {
        int days = (100 - progresses[i] + speeds[i] - 1) / speeds[i]; // 며칠걸리는지 arr에 넣음
        arr.push_back(days);
    }

    int max = arr[0];
    int cnt = 0;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] <= max) {
            cnt++;
        } else {
            answer.push_back(cnt);
            max = arr[i];
            cnt = 1;
        }
    }
    answer.push_back(cnt);

    return answer;
}
