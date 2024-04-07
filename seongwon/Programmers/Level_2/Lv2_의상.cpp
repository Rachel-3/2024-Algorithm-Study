#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> clothes_dic;
    for(auto& cloth : clothes){
        if(clothes_dic.find(cloth[1]) != clothes_dic.end()){    //cloth[1] 의상 종류가 있다면
            clothes_dic[cloth[1]]++;    //의상 개수 추가
        }
        else{   //의상 종류가 없던거라면
            clothes_dic[cloth[1]] = 1;  //의상 종류 추가
        }
    }
    for(auto& a : clothes_dic){
        answer *= (a.second+1);
    }
    answer--;
    return answer;
}
