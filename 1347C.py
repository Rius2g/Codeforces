x = int(input())

while x:
    y = int(input())
    streng = input()
    x -= 1
    i = 0
    count = 0
    while i < y:
        if streng[i] == "(":
            count += 1
        elif streng[i] == ")" and count > 0:
            count -= 1
        i += 1
    print(count)
