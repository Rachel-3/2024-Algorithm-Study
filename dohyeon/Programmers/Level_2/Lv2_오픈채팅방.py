def solution(record):
    answer = []
    user_dict = {}
    for i in record :
        split_data = i.split(" ")
        if len(split_data) == 3 :
            user_dict[split_data[1]] = split_data[2]
    for i in record :
        split_data = i.split(" ")
        if split_data[0] == "Enter" : 
            answer.append("{}님이 들어왔습니다.".format(user_dict[split_data[1]]))
        elif split_data[0] == "Leave" :
            answer.append("{}님이 나갔습니다.".format(user_dict[split_data[1]]))
    return answer