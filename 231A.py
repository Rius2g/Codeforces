x = int(input())
i = 0
k = 0
 
while i < x:
    a, b, c =  map(int, input().split())
    d = a+b+c
    if d >= 2:
        k += 1
 
    i += 1
 
 
print(k)