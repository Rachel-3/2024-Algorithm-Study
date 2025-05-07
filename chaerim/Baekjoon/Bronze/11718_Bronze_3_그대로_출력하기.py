while True:
    try:
        a = input()
        print(a)
    except EOFError:
        break