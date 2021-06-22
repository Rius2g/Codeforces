x = int(input())

streng = input()

i = 0
sum = 0

if len(streng) > 1:
    while i < len(streng) - 1:
        if streng[i] == streng[i+1]:
            sum += 1
        else:
            pass
        i += 1

print(sum)
