n = int(input())

shops = list(map(int, input().split()))
shops.sort()

q = int(input())

while q:
    x = int(input())
    count = 0
    for s in shops:
        if x  >= s:
            count += 1
        else:
            break
    print(count)
    q -= 1