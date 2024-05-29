def solution(word):
    answer = 0

    dic = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    increase = [781, 156, 31, 6, 1]

    for i in range(len(word)):
        answer += dic[word[i]] * increase[i] + 1

    return answer

'''
통과 코드지만 자리수 별로 증가하는 수를 계산해서 더 간략하게 작성 할 수 있을 거 같아 위에 새로 코드 작성..

def solution(word):
    answer = 0

    for i in range(0, len(word)):
        if i == 0:
            if word[i] == 'A':
                answer += 1
            elif word[i] == 'E':
                answer += 782
            elif word[i] == 'I':
                answer += 1563
            elif word[i] == 'O':
                answer += 2344
            elif word[i] == 'U':
                answer += 3125
        elif i == 1:
            if word[i] == 'A':
                answer += 1
            elif word[i] == 'E':
                answer += 157
            elif word[i] == 'I':
                answer += 313
            elif word[i] == 'O':
                answer += 469
            elif word[i] == 'U':
                answer += 625
        elif i == 2:
            if word[i] == 'A':
                answer += 1
            elif word[i] == 'E':
                answer += 32
            elif word[i] == 'I':
                answer += 63
            elif word[i] == 'O':
                answer += 94
            elif word[i] == 'U':
                answer += 125
        elif i == 3:
            if word[i] == 'A':
                answer += 1
            elif word[i] == 'E':
                answer += 7
            elif word[i] == 'I':
                answer += 13
            elif word[i] == 'O':
                answer += 19
            elif word[i] == 'U':
                answer += 25
        elif i == 4:
            if word[i] == 'A':
                answer += 1
            elif word[i] == 'E':
                answer += 2
            elif word[i] == 'I':
                answer += 3
            elif word[i] == 'O':
                answer += 4
            elif word[i] == 'U':
                answer += 5

    return answer
    '''