n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list :
    if i in n_list :
        print("yes", end = " ")
    else :
        print("no", end = " ")