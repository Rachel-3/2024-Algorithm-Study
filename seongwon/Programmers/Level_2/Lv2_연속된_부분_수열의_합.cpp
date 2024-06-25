#include <iostream>
#include <vector>
using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer;

    int start = 0, i = 0;
    int sum = 0;
    while (i < sequence.size()) {
        sum += sequence[i];
        while (sum > k && start <= i) {
            sum -= sequence[start];
            start++;
        }
        if (sum == k) {
            if (answer.empty() || (i - start < answer[1] - answer[0])) {
                answer = {start, i};
            }
        }
        i++;
    }
    return answer;
}

int main()
{
    vector<int> sequence = {1, 1, 1, 2, 3, 4, 5};
    vector<int> answer = solution(sequence, 5);
    cout << endl;
    for (int i : answer) {
        cout << i << " ";
    }
    return 0;
}

// sequence                  k        result
// [1, 2, 3, 4, 5]           7        [2, 3]
// [1, 1, 1, 2, 3, 4, 5]     5        [6, 6]
// [2, 2, 2, 2, 2]           6        [0, 2]
