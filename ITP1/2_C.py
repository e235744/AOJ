a, b, c = map(int, input().split())
MyList = []
MyList.append(a)
MyList.append(b)
MyList.append(c)

x = MyList[0]

for j in range(len(MyList)):
    for i in range(len(MyList) - 1):
        if MyList[i] > MyList[i + 1]:
            x = MyList[i + 1]
            MyList[i + 1] = MyList[i]
            MyList[i] = x

print(MyList)
