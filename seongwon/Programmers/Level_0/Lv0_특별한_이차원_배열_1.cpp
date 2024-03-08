#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(int n) {
    vector<vector<int>> answer(n,vector<int>(n));
    int i = 0;
    int j = 0;
    while(i<n){
        answer[i][j] = 1;
        i++;
        j++;
    }
    return answer;
}