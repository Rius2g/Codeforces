i = input()
 
k = 0
x = 0
 
while x < len(i):
    if i[x] == i[x -1]:
        k += 1
        x += 1
        if k >= 7:
            print("YES")
            break
    else:
        k = 1
        x += 1
 
if k < 7:
    print("NO")