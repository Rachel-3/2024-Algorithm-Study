import re
def solution(skill, skill_trees):
    answer = 0
    re_skill_tree = []
    pattern = r"[^{}]".format(skill)
    for i in skill_trees :
        result = re.sub(pattern, "", i)
        re_skill_tree.append(result)
    for skills in re_skill_tree:
        idx = 0
        possible = True
        for s in skills:
            if s in skill:
                if s != skill[idx]:
                    possible = False
                    break
                idx += 1
        if possible:
            answer += 1
    return answer