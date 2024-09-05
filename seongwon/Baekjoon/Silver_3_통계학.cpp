#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include<math.h>
#include <limits.h>
using namespace std;
int n;
double GetAvg(vector<int> arr){
     double sum = 0;
    for(int a : arr){
        sum += a;
    }
    return round(sum/n)+ 0.0;
}

int GetMid(vector<int> arr){
    sort(arr.begin(), arr.end());
    return arr[n/2];
}

int GetFrequent(vector<int> arr){
    map<int, int> m;
    for(int key : arr){
        auto finder = m.find(key);
        if(finder != m.end()){    //key가 이미 들어가 있으면
            finder -> second ++;    //finder는 이터레이터 이미 때문에 finder.second가 아닌 finder->로 접근해야함
        }
        else{
            m[key] = 1; //key가 없다면 새로 넣어줌
        }
    }
    vector<pair<int,int>> cnts_pair(m.begin(), m.end());
    sort(cnts_pair.begin(), cnts_pair.end(),[](const pair<int,int> a, const pair<int,int> b){  //cnt기준 내림차순 정렬
        if (a.second == b.second)
            return a.first < b.first;
        return a.second > b.second;
    });
    int max_cnt = cnts_pair[0].second;  //cnt 가장 높은 거
    vector<int> frequents;
    for(const auto cnt : cnts_pair){
        if(cnt.second == max_cnt){
            frequents.push_back(cnt.first);
        }
        else{
            break;
        }
    }
    if(frequents.size() == 1)
        return frequents[0];
    else{
        sort(frequents.begin(), frequents.end());
        return frequents[1];
    }
}

int GetRange(vector<int> arr){
    int min = INT_MAX;
    int max = INT_MIN;
    for(auto a : arr){
        if(min>a)
            min = a;
        if(max<a)
            max = a;
    }
    int range = max - min;
    return range;
}
int main()
{
    cin >> n;
    vector<int> arr;
    for(int i = 0; i < n; i++){
        int data;
        cin >> data;
        arr.push_back(data);
    }
    cout << GetAvg(arr) << "\n" << GetMid(arr) << "\n" << GetFrequent(arr) << "\n" << GetRange(arr);
    return 0;
}
