sum = 0

y = int(input())

k = 0

while k < y:
    string = input()
    if string == "X++" or string == "++X":
        sum += 1
    elif string == "X--" or string == "--X":
        sum -= 1
    k += 1

print(sum)