def solution(s):
    answer = []
    for i in s:
        if answer and answer[-1] == i:
            answer.pop() # 스택의 가장 위의 문자 제거
        else:
            answer.append(i)
    return 1 if not answer else 0
    # 스택이 비어있으면 1을, 아니면 0을 반환!