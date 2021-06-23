x, y = map(int, input().split())

sum = 0
while x:
    if x >= y:
        sum += y
        x += 1
        x -= y
    else:
        sum += x
        x = 0

print(sum) 