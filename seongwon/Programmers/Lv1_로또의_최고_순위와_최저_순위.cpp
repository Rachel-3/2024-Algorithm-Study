#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    vector<int> rank = {6,6,5,4,3,2,1};
    int max = 0, min = 0;
    //lottos 랑 win_nums 같은 번호 만큼 ++ + win_nums의 '0'개수 만큼 ++
    vector<int> inter;
    for(int i = 0; i < win_nums.size(); i++){
        if(lottos[i] == 0)
            max++;
    }
    sort(lottos.begin(), lottos.end());
    sort(win_nums.begin(), win_nums.end());
    set_intersection(lottos.begin(), lottos.end(),win_nums.begin(), win_nums.end(),back_inserter(inter));
    max += inter.size();
    min = inter.size();
    
    answer = {rank[max], rank[min]};
    return answer;
}
/* 반복문으로 풀려고 했는데 set_intersection을 사용해서 두 시퀀스에서 공통으로 존재하는 원소들로 새로운 시퀀스로 만들어주는
방법이 있길래 써봄
vector <int> intersection;
sort(lottos.begin(), lottos.end());
sort(win_nums.begin(), win_nums.end());
정렬 후 사용해야 함
set_intersection(lottos.begin(), lottos.end(), win_nums.begin(), win_nums.end(), back_inserter(intersection));
*/
