import itertools
def solution(clothes):
    answer = 1
    my_clothes = {}
    for i in clothes :
        if i[1] in my_clothes :
            my_clothes[i[1]].append(i[0])
        else :
            my_clothes[i[1]] = [i[0]]
    for key, value in my_clothes.items() :
        answer *= (len(value) + 1)
    return answer - 1

'''
각 부위 의류를 입느냐 안 입느냐 로 생각합니다.
그러면 (각 부위의 배열의 길이 + 1) 이 해당 부위가 가지는 경우의 수일 것입니다.
예시) headgear: yellow hat, green turban 일 때 가지는 경우의 수는
1) 노란 모자를 쓰는 경우 2) 초록 터번을 쓰는 경우 3) 아무것도 안쓰는 경우 총 3가지
(각 부위의 배열의 길이 + 1) 을 모두 곱하면 옷을 입거나 입지 않는 모든 경우의 수가 나옵니다.
하지만 적어도 하나의 부위의 옷은 입어야 합니다.
아무 것도 입지 않은 경우의 수는 1 입니다.
따라서 다 곱한뒤 1 을 빼면 정답입니다.
'''