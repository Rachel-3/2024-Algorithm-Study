def solution(plans):
    sort_list = []
    ''' Transporm Time '''
    for item in plans :
        temp = item[1].split(":")
        times = int(temp[0]) * 60 + int(temp[1])
        item[1] = times
        sort_list.append(item)
    sort_list.sort(key = lambda x: x[1], reverse=True)
    print(sort_list)
    
    answer = []
    while sort_list:
        temp = sort_list.pop()
        for index, item in enumerate(answer):
            if item[0] > temp[1]:
                answer[index][0] += int(temp[2])
        answer.append([temp[1]+int(temp[2]), temp[0]])
    answer.sort()
    return [i for k in answer for i in k if type(i) is str]