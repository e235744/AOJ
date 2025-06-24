a, b, c = map(int, input().split())
result = []

for i in range(a, b+1):
    if c % i == 0:
        result.append(i)

print(len(result))