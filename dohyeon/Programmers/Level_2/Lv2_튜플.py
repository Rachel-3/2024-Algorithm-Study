def solution(s):
    answer = []
    s = s[:-2].replace("{", "").replace(",", " ").split("}")
    for i in range(len(s)) :
        s[i] = s[i].split()
    s.sort(key = lambda x : len(x))
    
    for key in s :
        for i in answer :
            key.remove(i)
        answer.append(key[0])
    print(answer)
    answer = list(map(int, answer))
    return answer