n, a, b = map(int, input().split())

k = (n-a)
l = (b+1)

if k > l:
    print(l)
else:
    print(k)