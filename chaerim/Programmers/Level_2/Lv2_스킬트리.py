def solution(skill, skill_trees):
    answer = 0

    for word in skill_trees:
        skill_str = ''
        for char in word:
            if char in skill:
                skill_str += char

        if skill_str == skill[:len(skill_str)]:
            answer += 1

    return answer