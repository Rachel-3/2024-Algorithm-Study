class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int w, h;
        w = (int)(4+brown+Math.sqrt(brown*brown-8*brown-16*yellow+16))/4;
		h = (int)(4+brown-Math.sqrt(brown*brown-8*brown-16*yellow+16))/4;
        answer[0] = w;
        answer[1] = h;
        return answer;
    }
}
