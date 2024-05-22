def solution(files):
    answer = []
    head, number, tail = "", "", ""
    for file in files :
        for i in range(len(file)) :
            if file[i].isdigit() == True :
                head = file[:i]
                number = file[i:]
                for j in range(len(number)) :
                    if number[j].isdigit() == False :
                        tail = number[j:]
                        number =  number[:j]
                        break
                
                answer.append([head, number, tail])
                head, number, tail = "", "", ""
                break

    answer = sorted(answer, key = lambda x : (x[0].lower(), int(x[1])))
    answer = [''.join(i) for i in answer]
    return answer