while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    elif x > y:
        print(f"{y} {x}")
    else:
        print(f"{x} {y}")