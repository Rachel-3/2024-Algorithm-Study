# 백준 1715 - 카드 정렬하기
# 분류 : 우선순위 큐

from queue import PriorityQueue
N = int(input())
cards = []
for i in range(N) :
    cards.append(int(input()))

pq = PriorityQueue()

for i in range(N) :
    pq.put(cards[i])

score = 0
while pq.qsize() > 1 :
    min_value_1 = pq.get()
    min_value_2 = pq.get()
    pq.put(min_value_1 + min_value_2)
    score += min_value_1 + min_value_2

print(score)

