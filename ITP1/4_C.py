while True:
    a_str, op, b_str = input().split()
    a = int(a_str)
    b = int(b_str)

    if op == '?':
        break

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = int(a / b)

    print(result)
