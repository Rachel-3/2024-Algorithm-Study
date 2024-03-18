def solution(board):
    answer = 0
    arr = [[0 for col in range(len(board))] for row in range(len(board))]
    mine_index = []
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            if board[i][j] == 1 :
                mine_index.append([i, j])
    for i in mine_index :
        x, y = i[0], i[1]
        
        try : arr[x][y] = 1
        except : pass
        if x-1 >= 0 and y -1 >= 0 :
            try : arr[x - 1][y - 1] = 1
            except : pass

        if x - 1 >= 0 :
            try : arr[x - 1][y] = 1
            except : pass

        try : arr[x + 1][y + 1] = 1
        except : pass

        try : arr[x + 1][y] = 1
        except : pass

        if y - 1 >= 0 :
            try : arr[x][y - 1] = 1
            except : pass

        try : arr[x][y + 1] = 1
        except : pass

        if x - 1 >= 0 :
            try : arr[x - 1][y + 1] = 1
            except : pass

        if y - 1 >= 0 :
            try : arr[x + 1][y - 1] = 1
            except : pass
        
      
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            print(arr[i][j], end = ' ')
        print()
    
    for i in arr :
        for j in i :
            if j == 0 :
                answer += 1
    
        
    return answer

print(solution([[0, 0, 1], [0, 0, 0], [0, 0, 0]]))