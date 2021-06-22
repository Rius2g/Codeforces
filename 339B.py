x, y = map(int, input().split())
 
l = list(map(int, input().split()))
 
cnt = l[0]-1
 
for i in range(1,y):
    if l[i] >= l[i-1]:
        cnt += l[i]-l[i-1]
    else:
        cnt += x+l[i]-l[i-1]
 
 
print(cnt)