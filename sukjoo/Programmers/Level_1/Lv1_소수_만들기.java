import java.util.*;
class Lv_소수_만들기 {
    public int solution(int[] nums) {
        int answer = 0;
        Arrays.sort(nums);
        for(int i = 0; i < nums.length; i++){
            
            for(int j = i+1; j < nums.length; j++){
                
                for(int m = j+1; m < nums.length; m++){
                    int sum = nums[i] + nums[j] + nums[m];
                    boolean thisSum = true;
                    for(int n = 2; n <= sum/2; n++) {
                        if(sum%n == 0) {
                            thisSum = false;
                            break;
                        }
                    }
                    if(thisSum == true){
                        answer++;
                    }
                }
            }
        }

        return answer;
    }
}