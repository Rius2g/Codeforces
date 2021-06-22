x, y = map(int, input().split())
 
intlist = list(map(int, input().split()))
 
list.sort(intlist)
sum = 0
 
for i in intlist:
    if y > 0:
        if i >= 0:
            break
        else:
            sum += i
            y -= 1
    elif y == 0:
        break
 
sum *= -1
 
print(sum)