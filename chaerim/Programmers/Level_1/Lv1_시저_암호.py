def solution(s, n):
    answer = ''

    for char in s:
        if 'a' <= char <= 'z':
            answer += (chr((ord(char) - ord('a') + n) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            answer += (chr((ord(char) - ord('A') + n) % 26 + ord('A')))
        else:
            answer += char

    return answer