def solution(priorities, location):
    answer = 0

    array1 = [c for c in range(len(priorities))]
    print(array1)
    array2 = priorities.copy()
    print(array2)
    
    i = 0
    
    while True:
        if array2[i] < max(array2[i+1:]) :
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        else:
            i += 1

        if array2 == sorted(array2, reverse=True) :
            break

    return array1.index(location) + 1