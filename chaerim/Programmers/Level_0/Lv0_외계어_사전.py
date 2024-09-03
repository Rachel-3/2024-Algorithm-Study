def solution(spell, dic):
    answer = 2

    spell_sorted = ''.join(sorted(spell))

    for i in dic:
        if ''.join(sorted(i)) == spell_sorted:
            answer = 1

    return answer