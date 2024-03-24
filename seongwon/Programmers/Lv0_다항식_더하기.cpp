#include <iostream>
#include <string>
#include <vector>
#include <cctype>
using namespace std;

string solution(string polynomial) {
    string answer = "";
    vector<string> str;
    int index = 0;
    for(int i = 0; i<polynomial.size(); i++){
        if(polynomial[i] == ' '){
            str.push_back(polynomial.substr(index, i-index));
            index = i+1;
        }
    }
    str.push_back(polynomial.substr(index, polynomial.size()));
    int x = 0;
    int c = 0;
    
   for(string s : str){
    if(s == "+" || s.empty()){ // "+" 문자열 , 공백 무시
        continue; 
    }
    else if(s == "x"){
        x++;    
    }
    else if(s.back() == 'x'){
        x += stoi(s);
    }
    else{
        c += stoi(s);
    }
}


    
    if(x!=0){
        if(x==1)    answer += "x";  //x가 1이면 "1x"가 아닌 "x"를 반환해야함
        else answer += to_string(x)+"x";
        if(c!=0){
            answer += " + ";
            answer += to_string(c);
        }
    }
    else{
        answer += to_string(c);
    }
    
    return answer;
}

/*
stoi => 문자열을 정수로 반환 "234b" -> 234
.back() => 가장 뒤쪽원소 반환
*/
