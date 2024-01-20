def solution(tickets):
    answer = ["ICN"]
    visited = [False] * len(tickets)

    def DFS(start, path) :
        if len(path) == len(tickets) + 1 :
            answer.append(path)
            return

        for index, data in enumerate(tickets) :
            if data[0] == start and visited[index] == False :
                visited[index] = True
                DFS(data[1], path + [data[1]])
                visited[index] = False

    DFS("ICN", ["ICN"])
    answer = answer[1:]
    answer.sort()
    return answer[0]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))