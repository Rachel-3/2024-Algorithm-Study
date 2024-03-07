def solution(keymap, targets):
    answer = []

    index = {}
    for key in keymap:
        for key_index, key_char in enumerate(key):
            if key_char not in index or key_index < index[key_char]:
                index[key_char] = key_index + 1

    for target in targets:
        count = 0
        for target_char in target:
            if target_char in index:
                count += index[target_char]
            else:
                count = 0
                break
            
        if count == 0:
            answer.append(-1)
        else:
            answer.append(count)

    return answer