def solution(N, stages):
    answer = []
    stage_count = [0]*(N+2)
    
    for stage in stages:
        stage_count[stage] += 1

    rate = []

    for i in range(1, N+1):
        user = (sum(stage_count[i:]))
        if user == 0:
            failure_rate = 0
        else:
            failure_rate = stage_count[i] / user
        rate.append((failure_rate, i))

    sorted_rates = sorted(rate, key=lambda x: (-x[0], x[1]))    # 실패율 내림차순, 스테이지 번호 오름차순 정렬 **정렬 매개변수 [인덱스]**

    answer = [stage for _, stage in sorted_rates]

    return answer