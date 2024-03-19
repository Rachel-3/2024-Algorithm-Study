import java.util.*;

class Lv2_기능개발 {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> daysQueue = new LinkedList<>();
        Stack<Integer> taskCountStack = new Stack<>();

        // 각 작업에 필요한 날 수 계산
        for (int i = 0; i < progresses.length; i++) {
            int days = (int) Math.ceil((double) (100 - progresses[i]) / speeds[i]);
            daysQueue.offer(days);
        }

        int count = 1;
        int maxDays = daysQueue.poll();

        // 스택을 업데이트하고 함께 완료할 수 있는 작업을 찾음
        while (!daysQueue.isEmpty()) {
            int currentDays = daysQueue.poll();

            if (currentDays <= maxDays) {
                count++;
            } else {
                taskCountStack.push(count);
                count = 1;
                maxDays = currentDays;
            }
        }

        taskCountStack.push(count);

        // 스택을 최종 답변 배열로 변환
        int[] answer = new int[taskCountStack.size()];
        int index = taskCountStack.size() - 1;

        while (!taskCountStack.isEmpty()) {
            answer[index--] = taskCountStack.pop();
        }

        return answer;
    }
}
