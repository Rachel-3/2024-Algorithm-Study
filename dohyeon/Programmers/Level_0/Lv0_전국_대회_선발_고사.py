def solution(rank, attendance):
    answer = 0
    user = []
    for i in range(len(attendance)) :
        if attendance[i] == True :
            user.append(rank[i])
    user.sort()
    user_index = []
    for i in range(3) :
        user_index.append(rank.index(user[i]))
    return 10000 * user_index[0] + 100 * user_index[1] + user_index[2]