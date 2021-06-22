i = 1

sum = 0

while i < 6:
    tall = list(map(int, input().split()))
    if 1 in tall: #is in that row, need to find position
        l = 0
        while l < 5:
            if tall[l] == 1:
                sum += abs(l-2) + abs(i-3)
                break
            l += 1

    i += 1


print(sum)