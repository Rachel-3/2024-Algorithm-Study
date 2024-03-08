import java.util.*;
class Lv2_다음_큰_숫자 {
    public int solution(int n) {
        int count = 0;
        int count2 = 0;
        int k = 1;
        String a = Integer.toBinaryString(n);
        for(int i = 0 ; i < a.length() ; i++ ){
            if(a.charAt(i) == '1'){
                count++;
                }
        }
        while (n+k < 1000000){
            count2 = 0;
            String b = Integer.toBinaryString(n+k);
            for(int j = 0 ; j < b.length() ; j++ ){
            if(b.charAt(j) == '1'){
                count2++;
                }
            }
            if(count == count2){
                return n+k;
            }
            k++;
        }
        return 0;
    }
}