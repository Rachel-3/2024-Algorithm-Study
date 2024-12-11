for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    diff = end - start
    h = diff // 3600
    m = (diff % 3600) // 60
    s = diff % 60
    print(h, m, s)