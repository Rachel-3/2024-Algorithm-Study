def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    
    max_cctv = routes[0][1]
    answer += 1
    for i in routes :
        if max_cctv < i[0] :
            max_cctv = i[1]
            answer += 1
    return answer