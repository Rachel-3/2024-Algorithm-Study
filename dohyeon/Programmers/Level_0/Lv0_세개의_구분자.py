import re
def solution(myStr):
    answer = []
    re_list = (re.split('[abc]', myStr))
    for i in re_list :
        if i != '' :
            answer.append(i)
    if len(answer) == 0 :
        return ["EMPTY"]
    return answer