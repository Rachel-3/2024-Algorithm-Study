public class Lv2_카펫 {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int [2];
        int a = (brown - 4)/2;
        for(int i = 0 ; i < a; i++){
            if(i*(a-i) == yellow){
                answer[0] = i+2;
                answer[1] = a-i+2;
            }
        }
        
        
        return answer;
    }
}
