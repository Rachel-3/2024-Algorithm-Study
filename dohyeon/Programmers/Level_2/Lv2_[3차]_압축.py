def solution(msg):
    dict = {}
    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(str)) :
        dict[str[i]] = i + 1
    answer = [0]
    value = 26
    base = ""
    for i in range(len(msg)):
        base += msg[i]
        if not base in dict:
            value += 1
            dict[base] = value
            base = msg[i]
            answer.append(dict[base])
        else:
            answer[-1] = dict[base]
    return answer