def solution(before, after):
    answer = 0
    before_word = {}
    after_word = {}
    for i in before:
        before_word[i] = before.count(i)
    for i in after:
        after_word[i] = after.count(i)
    if after_word == before_word :
        return 1
    return answer