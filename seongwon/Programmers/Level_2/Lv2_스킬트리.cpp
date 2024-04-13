#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = skill_trees.size();
    for(string s : skill_trees){
        int idx = 0;
        for(char c : s){
            auto i = find(skill.begin(), skill.end(), c);
            if(i != skill.end()){
                if(skill[idx] != *i){
                    answer--;
                    break;
                }
                else {
                    idx++;
                }
            }
        }
    }
    return answer;
}
