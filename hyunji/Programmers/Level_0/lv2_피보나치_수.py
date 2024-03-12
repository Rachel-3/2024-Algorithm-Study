def solution(n):
    fibolist = [0, 1]
    for i in range(2, n + 1):
        fibo = fibolist[i - 1] + fibolist[i - 2]
        fibolist.append(fibo)
    answer = fibolist[n]
    return answer % 1234567