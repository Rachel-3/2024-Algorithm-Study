def solution(keymap, targets):
    answer = []
    for i in targets :
        indexs = []
        for j in keymap :
            each_index = []
            for k in i :
                index = j.find(k) + 1
                if index == 0 :
                    each_index.append(-1)
                    
                else : each_index.append(index)
            indexs.append(each_index)
            # print(indexs)
        result = []
        check = 0
        for temp in range(len(indexs[0])):
            values = [sublist[temp] for sublist in indexs if sublist[temp] != -1]
            if len(values) == 0 :
                result.append(-1)
                check = 1
            min_value = -1
            if values:
                min_value = min(values)
            result.append(min_value)
        if check ==1 :
            answer.append(-1)
        else :
            answer.append(sum(result))
    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"])) # 9, 4
print(solution(["AA"], ["B"])) # -1
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"])) # 4, 6
print(solution(["BC", "CDB"], ["BB"])) # 2
print(solution(["ABCE"], ["ABDE"])) # -1