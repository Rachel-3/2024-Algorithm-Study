#include <string>
#include <vector>
#include <cctype>
using namespace std;
string solution(string s) {
    string answer = "";
    int cnt = 0;
    for(int i = 0; i < s.size(); i++){
        if(islower(s[i])&&cnt == 0){    //첫 글자인데 소문자면 대문자로 바꿈
            answer += (s[i]-32);
        }
        else if(isupper(s[i])&&cnt != 0){   //첫 글자 아닌데 대문자면 소문자로
            answer += (s[i]+32);
        }
        else
            answer += s[i];
        if(s[i]==' ') cnt = 0;
        else    cnt++;
    }
    return answer;
}
//islower(문자열) //소문자 판별 (소문자가 아니라면 0이 반환)
