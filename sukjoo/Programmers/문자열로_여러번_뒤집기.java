public class 문자열로_여러번_뒤집기 {

    public String solution(String my_string, int[][] queries) {
        String answer = "";
        Stack<String> stack = new Stack<>();
        String[] str = my_string.split("");
        for (int i = 0; i < queries.length; i++) {
            for (int j = queries[i][0]; j <= queries[i][1]; j++) {
                stack.push(str[j]);
            }
            for (int m = queries[i][0]; m <= queries[i][1]; m++) {
                str[m] = stack.pop();
            }
        }
        for (int n = 0; n < str.length; n++) {
            answer += str[n];
        }
        return answer;

    }
    /*문자열 여러 번 뒤집기
문제 설명
문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

제한사항
my_string은 영소문자로만 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 1,000
queries의 원소는 [s, e]의 형태로 0 ≤ s ≤ e < my_string의 길이를 만족합니다.
1 ≤ queries의 길이 ≤ 1,000
입출력 예
my_string	queries	result
"rermgorpsam"	[[2, 3], [0, 7], [5, 9], [6, 10]]	"programmers"
입출력 예 설명
예제 1번의 my_string은 "rermgorpsam"이고 주어진 queries를 순서대로 처리하면 다음과 같습니다.

queries	my_string
"rermgorpsam"
[2, 3]	"remrgorpsam"
[0, 7]	"progrmersam"
[5, 9]	"prograsremm"
[6, 10]	"programmers"
따라서 "programmers"를 return 합니다.*/

}
