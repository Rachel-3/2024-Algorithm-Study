class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        int len = words.length; 
        boolean[] visited = new boolean[len];
        char lastChar = words[0].charAt(words[0].length() - 1); 
        visited[0] = true;

        for (int i = 1; i < len; i++) {
            if (visited[i]) {
                answer[0] = (i % n) + 1;
                answer[1] = (i / n) + 1;
                return answer;
            }

            if (lastChar != words[i].charAt(0)) {
                answer[0] = (i % n) + 1;
                answer[1] = (i / n) + 1;
                return answer;
            }

            if (isDuplicate(words, i)) {
                answer[0] = (i % n) + 1;
                answer[1] = (i / n) + 1;
                return answer;
            }
            
            visited[i] = true;
            lastChar = words[i].charAt(words[i].length() - 1);
        }

        answer[0] = 0;
        answer[1] = 0;
        return answer;
    }

    private boolean isDuplicate(String[] words, int index) {
        for (int i = 0; i < index; i++) {
            if (words[i].equals(words[index])) {
                return true;
            }
        }
        return false;
    }
}
