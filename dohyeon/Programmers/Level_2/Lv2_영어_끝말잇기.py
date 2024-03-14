def solution(n, words):
    answer = []
    stack = []
    user = {}
    words_index = 0
    for i in range(len(words)) :
        try :
            user[(i % n) + 1].append(words[i])
        except :
            user[(i % n) + 1] = [words[i]]
        if words[i] in stack :
            words_index = i
            break
        stack.append(words[i])
        if (len(stack) >= 2 and stack[-2][-1] != words[i][0]):
            words_index = i
            break
    if words_index != 0 :
        answer.append((words_index % n) + 1)
        answer.append(user[(words_index % n) + 1].index(words[words_index]) + 1)
    elif words_index == 0 :
        answer = [0, 0]
        
    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])) #	[3,3]
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) # [0,0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])) # [1,3]