class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
              
                if (board[i][j] == 1) {  // 1인지역 찾음
                  
                    for (int a = i - 1; a <= i + 1; a++) {  //현재위치에서 {-1,-1} 부터 {+1,+1} 까지 위험지역
                        for (int b = j - 1; b <= j + 1; b++) {
                          
                            if (a >= 0 && a < board.length && b >= 0 && b < board[i].length) {  // 배열 벗어나면 안댕
                                if(board[a][b] != 1)  //지뢰가 있는곳은 1
                                board[a][b] = 2;   //지뢰 주위 위험지역은 2
                            }
                        }
                    }
                }
            }
        }
        for (int[] row : board) {
            for (int num : row) {
                if (num == 0) {
                    answer++;
                }
            }
        }
        return answer;
    }
}
