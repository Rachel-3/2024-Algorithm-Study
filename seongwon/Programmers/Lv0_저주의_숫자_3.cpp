#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    for(int i = 0; i < n; i++){
        if(i%3 == 0)
            n++;
        string st = "";
        st = to_string(i);
        for(char c : st){
            if((c == '3')&&(i%3!=0)){
                n++;
                break;
            }
        }
    }
    int answer = n-1;
    return answer;
}
