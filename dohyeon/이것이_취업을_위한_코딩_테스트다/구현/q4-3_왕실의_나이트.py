location = input()
x = int(ord(location[0])) - int(ord('a')) + 1
y = int(location[1])

answer = 0

directions = [
    (-2, -1), (-1, -2),
    (1, -2), (2, -1),
    (2, 1), (1, 2),
    (-1, 2), (-2, 1) 
]

def isvalid(x, y) :
    if x > 8 or y > 8 or x < 1 or y < 1 :
        return False
    else :
        return True

for i in directions :
    if isvalid(x + i[0], y + i[1]) :
        answer += 1
        
print(answer)