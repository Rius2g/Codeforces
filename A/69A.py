x = int(input())
 
i = 0
sum = 0
sum1 = 0
sum2 = 0
sum3 = 0
while i < x:
    numbers, numbers2, numbers3 = [int(x) for x in input().split()]
    sum1 += numbers
    sum2 += numbers2
    sum3 += numbers3
    i += 1
 
 
if x == 0:
    print("YES")
 
if sum1 == 0 and sum2 == 0 and sum3 == 0:
    print("YES")
else:
    print("NO")