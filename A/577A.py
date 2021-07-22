n, x = map(int, input().split())


i = 1
sum = 0

while i <= n:
    if x % i == 0 and x / i <= n:
            sum += 1
    i += 1


print(sum)