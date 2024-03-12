def solution(s):
    answer = 0
    stack = []
    for i in s :
        if len(stack) >= 1 and stack[-1] == i :
            stack.pop()
        else :
            stack.append(i)
    if len(stack) == 0 :
        answer = 1
    return answer

'''
문제 자체는 lv1에서 풀었던 크레인 인형뽑기 게임과 비슷하다. 스택의 개념만 안다면 쉽게 접근 할 수 있다.
문제 풀이 로직으로 스택을 사용하였으며, 스택 길이가 1이상이고, 스택의 마지막 값이 들어가는 값과 같다면, 
스택에서 팝 시킨다. 전체적인 흐름은 baabaa 라고 가정하면 스택의 모습은 다음과 같다.
Stack, ()는 팝되는 모습을 나타낸다.
-> b
-> b -> a
-> b -> (a -> a)
-> (b -> b)
-> a
-> (a -> a)
->
'''