#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
bool comp(vector<string>v1 , vector<string>v2){ //시작시간으로 정렬 
    return v1[1] < v2[1]; 
}

vector<string> solution(vector<vector<string>> plans) {
    vector<string> answer;
    sort(plans.begin(), plans.end(), comp);
    vector<pair<string,int>> p; //과제이름, 걸리는 시간
    int curtime = 0;
    for(vector<string> plan : plans){
        int newtime = 60*stoi(plan[1].substr(0,2))+stoi(plan[1].substr(3,5));   //새로운 과제 시작시간
        while(curtime < newtime){
            if(p.size() > 0){
                p.back().second--;
                if(p.back().second == 0){  //작업 완료
                    answer.push_back(p.back().first);
                    p.pop_back();
                }
            }
            curtime++;
        }
        p.push_back(make_pair(plan[0],stoi(plan[2])));
    }
    while(p.size()>0){
        answer.push_back(p.back().first);
        p.pop_back();
    }
    return answer;
}
/*
시작 시간으로 정렬하고, 시간 ++하면서 과제하다가 새로운 과제 나오면 새로운거 시작.
과제 끝나면 멈춰둔과제 다시시작.
*/
int main()
{
    vector<vector<string>> plans = {{"korean", "11:40", "30"}, {"english", "12:10", "20"}, {"math", "12:30", "40"}};
    vector<string> answer = solution(plans);
    for(string a : answer){
        cout << a << "  ";
    }
    return 0;
}

