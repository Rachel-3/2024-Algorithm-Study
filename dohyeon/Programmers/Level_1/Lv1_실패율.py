def solution(N, stages):
    cnt = []
    answer = []
    stage_user = len(stages)
    for i in range(1, N + 1) :
        current_stage_user = 0
        for j in stages :
            if i == j :
                current_stage_user += 1
        try :
            percent = (current_stage_user / stage_user)
        except :
            percent = 0
        stage_user -= current_stage_user
        cnt.append(percent)
    temp = cnt.copy()
    (temp.sort(reverse=True))
    for i in range(len(temp)) :
        for j in range(len(cnt)) :
            if temp[i] == cnt[j] : 
                answer.append(j + 1)
                cnt[j] = -1
    return (answer)