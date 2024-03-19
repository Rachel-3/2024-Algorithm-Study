import java.util.Arrays;

class level_0_약수_구하기 {
	public int[] solution(int n) {
		int a = 0;

		for(int i = 1; i <= n; i++){
			if(n % i == 0){
				a++;
			}
		}
		int[] answer = new int[a];

		int k = 0; // k 변수 선언 및 초기화

		for (int i = 1; i <= n; i++){
			if(n % i == 0){
				answer[k] = i;
				k++;
			}
		}

		Arrays.sort(answer);
		return answer;
	}
}