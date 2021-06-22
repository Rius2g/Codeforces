x, y = map(int, input().split())

i = 0

if x < y:
    i = x
else:
    i = y


if i % 2 == 0:
    print("Malvika")
else:
    print("Akshat")