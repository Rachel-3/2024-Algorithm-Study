import java.util.*;

class level_0_문자열_잘라서_정렬하기 {
	public String[] solution(String myString) {
		String[] answer = myString.split("x");
		Arrays.sort(answer, (a, b) -> a.compareTo(b)); // 문자열을 사전순으로 정렬

		// 빈 문자열 제거
		List<String> resultList = new ArrayList<>();
		for (String str : answer) {
			if (!str.isEmpty()) {
				resultList.add(str);
			}
		}

		// List를 배열로 변환
		return resultList.toArray(new String[0]);
	}
}
