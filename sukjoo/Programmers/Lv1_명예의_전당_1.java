import java.util.*;
class Lv1_명예의_전당_1 {
    public int[] solution(int k, int[] score) {
        List<Integer> list = new ArrayList<>();
        int[] answer = new int [score.length];
        
        for(int i = 0; i < score.length;i++){
            list.add(score[i]);
            Collections.sort(list, Collections.reverseOrder());
            if(i < k){
                answer[i] = list.get(list.size() - 1);
            }
            else{
                answer[i] = list.get(k-1);
            }
        }
        
        return answer;
    }
}