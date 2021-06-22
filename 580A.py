x = int(input())
 
tall = list(map(int, input().split()))
res = []
 
count = 0
 
sub = 0
for k in tall:
    if k < sub:
        count = 1
    elif k >= sub:
        count += 1
 
    sub = k
    res.append(count)
 
 
res.sort(reverse=True)
 
print(res[0])