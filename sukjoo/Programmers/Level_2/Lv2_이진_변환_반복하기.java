package Level_2;
class Lv2_이진_변환_반복하기 {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int count0 = 0;
        int length = 0;
        int answer2 = 0;
        while(s.length() > 1){
            length = 0;
            answer2++;
            System.out.println(s );
            for(int i = 0 ; i < s.length(); i++){
                if(s.charAt(i)=='0'){
                    count0++;
                    
                }
                else{
                    length++;
                }
            }
            s = Integer.toBinaryString(length);
        }
        answer[1] = count0;
        answer[0] = answer2;
        return answer;
    }
}