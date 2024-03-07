#include <string>
#include <vector>
#include <iostream> 
#include <algorithm>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    int l = numbers.size();
    sort(numbers.begin(), numbers.end());
    if(numbers[0]*numbers[1] > numbers[l-2]*numbers[l-1])
        answer = numbers[0]*numbers[1];
    else
        answer = numbers[l-2]*numbers[l-1];
    return answer;
}