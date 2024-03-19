import java.util.Arrays;

class 최댓값_만들기(2) {
	public int solution(int[] numbers) {
		int answer = 0;
		int min , max;
		Arrays.sort(numbers);

		min = numbers[0] * numbers[1];
		max = numbers[numbers.length -1] * numbers[numbers.length -2];

		answer = Math.max(min, max);
		return answer;


	}

}