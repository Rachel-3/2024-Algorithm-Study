def solution(board, moves):
    answer = 0
    pick_up_list = []
    reversed_list = list(map(list, zip(*board)))
    # for i in range(len(board)) :
    #     for j in range(len(board[i])) :
    #         print(board[i][j], end=" ")
    #     print()
    # print()
    
    # for i in range(len(reversed_list)) :
    #     for j in range(len(reversed_list[i])) :
    #         print(reversed_list[i][j], end=" ")
    #     print()
    # print()
    for i in moves :
        for j in range(len(reversed_list[i - 1])) :
            if reversed_list[i - 1][j] != 0 :
                pick_up_list.append(reversed_list[i - 1][j])
                reversed_list[i - 1][j] = 0
                break
        
        if len(pick_up_list) >= 2 and pick_up_list[-1] == pick_up_list[-2] :
            answer += 2
            pick_up_list.pop()
            pick_up_list.pop()
    
    # 실패 메서드 -> 동작하면서 바로 검사로 방법 변경
    # i = 0
    # while i < len(pick_up_list) - 1:
    #     if pick_up_list[i] != 1 and pick_up_list[i+1] != 1:
    #         answer += 2
    #         i += 2
    #     else:
    #         i += 1
            
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])) # 4
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 2], [5, 5, 5, 5, 5], [2, 2, 2, 2, 2]], [5, 1, 2, 3, 4, 1])) # 6