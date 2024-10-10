def solution(wallpaper):
    answer = []

    x, y = [], []

    wallpaper_len = len(wallpaper)
    wallpaper_0_len = len(wallpaper[0])

    for i in range(wallpaper_len):
        for j in range(wallpaper_0_len):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)

    lux = min(x)
    luy = min(y)
    rdx = max(x)
    rdy = max(y)

    answer = [lux, luy, rdx+1, rdy+1]

    return answer