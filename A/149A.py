x = int(input())
 
numbers = list(map(int, input().split()))
 
list.sort(numbers, reverse=True)
 
sum1 = 0
sum = 0
 
for i in numbers:
    if sum >= x:
        break
    else:
        sum += i
        sum1 += 1
 
 
if sum >= x:
    print(sum1)
else:
    print("-1")