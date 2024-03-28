def solution(elements):
    answer = []
    double_elements = elements + elements
    n = len(elements)
    elements.sort()
    
    for i in range(1, n + 1) :
        for j in range(len(elements)) :
            answer.append(sum(double_elements[j:j+i]))
    answer = list(set(answer))
    return len(answer)