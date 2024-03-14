public class Lv2_영어_끝말잇기 {
    public int[] solution(int n, String[] words) {
        int[] answer = new int [2];
        
        for (int i = 0 ; i < words.length; i++){
            for(int j = 0 ; j < i ; j++){
                if (words[j].equals(words[i])&& i != j ){
                    answer[0] = (i % n) + 1;
                    answer[1] = (i / n) + 1;
                    return answer;
                }
            }
            
            if(i>0&&words[i-1].charAt(words[i-1].length()-1) != words[i].charAt(0)){
                answer[0] = (i % n) +1 ;
                answer[1] = (i / n) +1 ;
                break;
            }
            else {
                answer[0] = 0;
                answer[1] = 0;
            }
            
        }
        System.out.println();

        return answer;
    }
    
}
