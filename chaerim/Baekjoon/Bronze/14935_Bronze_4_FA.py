x = input()

prev = None

while True:
    fx = int(x[0]) * len(x)
    if x == str(fx):
        print("FA")
        break
    x = str(fx)