#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    vector<int> arr(10000001,0);
    for(int i = 0; i < tangerine.size(); i++){
        arr[tangerine[i]]++;
    }
    sort(arr.begin(), arr.end());
    reverse(arr.begin(), arr.end());  //내림차순으로 뒤집음
    int a = 0;
    for(int i : arr){
        a += i;
        answer++;
        if(a >= k){
            break;
        }
    }
    return answer;
}
