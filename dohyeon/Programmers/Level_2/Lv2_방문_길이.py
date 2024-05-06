''' 역방향도 고려해야함! '''
def ispath(x, y) :
    if x > 5 or x < -5 :
        return False
    elif y > 5 or y <- 5 :
        return False
    return True
def solution(dirs):
    answer = 0
    x, y = 0, 0
    paths = []
    for i in dirs :
        pre_x, pre_y = x, y
        if i == "U" :
            y += 1
            if ispath(x, y) :
                paths.append([[pre_x, pre_y], [x, y]])
            else :
                y -= 1
        elif i == "D" :
            y -= 1
            if ispath(x, y) :
                paths.append([[pre_x, pre_y], [x, y]])
            else :
                y += 1
        elif i == "R" :
            x += 1
            if ispath(x, y) :
                paths.append([[pre_x, pre_y], [x, y]])
            else :
                x -= 1
        elif i == "L" :
            x -= 1
            if ispath(x, y) :
                paths.append([[pre_x, pre_y], [x, y]])
            else :
                x += 1
    sorted_paths = [sorted([tuple(p1), tuple(p2)]) for p1, p2 in paths]
    unique_paths_set = set(map(tuple, sorted_paths))
    unique_paths = [list(map(list, path)) for path in unique_paths_set]
    return len(unique_paths)