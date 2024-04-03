import java.util.Stack;

class Solution {
    public int solution(String s) {
        if (s.isEmpty()) // 입력 문자열이 비어 있는 경우
            return 1; // 스택에 아무것도 추가하지 않았으므로 올바른 문자열이 됨

        Stack<Character> st = new Stack<>();
        st.push(s.charAt(0));
        for(int i = 1; i < s.length(); i++) {
            if (!st.empty() && s.charAt(i) == st.peek()) {
                st.pop();
            } else {
                st.push(s.charAt(i));
            }
        }
        
        if (st.empty()) {
            return 1;
        } else {
            return 0;
        }
    }
}
