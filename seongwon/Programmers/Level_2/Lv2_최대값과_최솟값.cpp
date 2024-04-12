#include <string>
#include <vector>
#include <sstream>
#include <string>
#include <limits>
#include <vector>
using namespace std;

string solution(string s) {
    istringstream iss(s);
    string token;
    vector<int> numbers;
    int num, max= - 99999, min = 99999;
    while(iss >> token){
        num = stoi(token);
        numbers.push_back(num);
    }
    for(int i : numbers){
        if(i < min) min = i;
        if(i > max) max = i;
    }
    ostringstream oss;
    oss << min << " " << max;
    return oss.str();
}
