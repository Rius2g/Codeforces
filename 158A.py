x, y = map(int, input().split())
 
 
 
tall = list(map(int, input().split()))
ref =  tall[y-1]
 
sum = 0
 
for k in tall:
    if k >= ref and k > 0:
        sum += 1
 
print(sum)