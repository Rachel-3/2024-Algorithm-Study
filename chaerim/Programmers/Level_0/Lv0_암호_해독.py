def solution(cipher, code):
    answer = ''

    for char in range(code-1, len(cipher), code):
        answer += cipher[char]

    return answer