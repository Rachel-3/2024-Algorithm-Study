N = int(input())
routes = list(map(str,  input().split(" ")))

def isvalid(x, y) :
    if x > N or x < 1 :
        return False
    elif y > N or y < 1 :
        return False
    else :
        return True

x, y = 1, 1
for i in routes :
    if i == "R" :
        y += 1
        if isvalid(x, y) == False :
            y -= 1
    elif i == "L" :
        y -= 1
        if isvalid(x, y) == False :
            y += 1
    elif i == "U" :
        x -= 1
        if isvalid(x, y) == False :
            x += 1
    elif i == "D" :
        x += 1
        if isvalid(x, y) == False :
            x -= 1
print(x, y)

