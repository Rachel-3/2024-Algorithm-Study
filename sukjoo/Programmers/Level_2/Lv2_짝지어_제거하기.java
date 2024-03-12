import java.util.*;
class Solution{
    public int solution(String s){
        // 문자를 아스키코드상태로 배열에 넣기
        int[] num = new int[s.length()];
        for(int k = 0 ; k < s.length();k++){
            num[k] = (int)s.charAt(k);
        }
        //스택
        Stack<Integer> stack = new Stack<>();
        for(int i = 0 ; i < num.length ; i++){
        //비어있지 않으면 스택 제일 위에 있는 수와 i번째 수랑 비교해서 같으면 제일 위에 수 빼기
            if(!stack.empty()&&stack.peek() == num[i]){
                stack.pop();
            }
            // 같지않을경우, i번째수 집어넣기
            else{
                stack.push(num[i]);
            }
        }
        // 모두 끝냈을때 비어있으면 1로 리턴.
        if(stack.empty()){
                    return 1;
                }
        // 모두 끝냈을때 비어있지않으면 0으로 리턴
        return 0;
    }
}