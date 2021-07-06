n, m = map(int, input().split())

x =(n+1)/2

result = ((x+m-1)/m)*m

if int(result) > n:
    result = -1

print(int(result))

