def solution(before, after):
    answer = 1

    sorted_before = ''.join(sorted(before))
    sorted_after = ''.join(sorted(after))

    if sorted_before != sorted_after:
        answer = 0

    return answer

'''
위, 아래 둘다 가능 

sorted() 는 병합 정렬을 기반으로 만들어졌는데, 병합 정렬은 일반적으로 퀵 정렬보다 느리지만 
최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다는 특징이 있다. 
sorted() 함수는 정렬된 결과를 리스트 자료형으로 반환한다.

-> 위에가 시간복잡도를 따지면 더 효율적

def solution(before, after):
    answer = 1

    for be in before:
        if be not in after:
            answer = 0
        elif before.count(be) != after.count(be):
            answer = 0

    return answer
'''