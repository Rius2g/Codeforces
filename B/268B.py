n = int(input())

sum = n
i = 1
j = n -1

while j:
    sum += i * j
    i += 1 
    j -= 1

print(sum)