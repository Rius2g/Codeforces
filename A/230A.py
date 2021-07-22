power, dragons = map(int, input().split())
fl = 1
list1 = []
 
i = 0 
for i in range(dragons):
    drage, xpgain = map(int, input().split())
    list1.append([drage, xpgain])
 
 
list1 = sorted(list1)
 
 
for i in range(dragons):
    if power > list1[i][0]:
        power += list1[i][1]
    else:
        fl = 0
    
if fl:
    print("YES")
else:
    print("NO")