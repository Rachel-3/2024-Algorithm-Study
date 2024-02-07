def solution(s, skip, index):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip :
        alphabet = alphabet.replace(i, "")
    for i in s :
        idx = (alphabet.index(i) + index) % len(alphabet)
        answer += alphabet[idx]
    return answer

s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))