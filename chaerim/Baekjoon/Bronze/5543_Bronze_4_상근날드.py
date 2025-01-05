bugger = -1
drink = -1
for i in range(5):
    money = int(input())
    if i < 3:
        if bugger == -1:
            bugger = money
        elif money < bugger:
            bugger = money
    else:
        if drink == -1:
            drink = money
        elif money < drink:
            drink = money

print(bugger + drink - 50)