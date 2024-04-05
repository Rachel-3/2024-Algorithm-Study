#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    
    for(int i = 0; i < arr1.size(); i++){ 
        vector<int> row;
        for(int j = 0; j < arr2[0].size(); j++){
            int tmp = 0;
            for(int k = 0; k < arr2.size(); k++){
                tmp+=arr1[i][k]*arr2[k][j];
            }
            row.push_back(tmp); // tmp를 포함한 행을 추가
        }  
        answer.push_back(row); // 새로운 행을 answer 벡터에 추가
    }
    
    return answer;
}
