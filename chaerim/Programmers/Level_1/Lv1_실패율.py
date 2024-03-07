def solution(N, stages):
    answer = []
    stage_count = [0]*(N+2)

    for stage in stages:
        stage_count[stage] += 1

    rate = []

    for i in range(1, N+1):
        user = (sum(stage_count[i:]))
        if user == 0:
            rate.append(0)
        else:
            rate.append(stage_count[i]/user)

    for r in range(N):
        max_rate = max(rate)
        for k in range(N):
            if rate[k] == max_rate:
                answer.append(k+1)
                rate[k] = -1
                break

    return answer