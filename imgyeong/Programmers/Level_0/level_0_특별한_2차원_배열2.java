public class level_0_특별한_이차원_배열2 {
	public int solution(int[][] arr) {
		int n = arr.length; // 행렬의 크기
		// 주어진 행렬의 각 원소에 대해 대칭인지 확인
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				// 대칭 조건을 만족하지 않으면 0 반환
				if (arr[i][j] != arr[j][i]) {
					return 0;
				}
			}
		}
		// 모든 원소가 대칭 조건을 만족하면 1 반환
		return 1;
	}
}