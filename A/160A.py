x = int(input())
 
tall = list(map(int, input().split()))
 
sum1 = sum(tall)
 
tall.sort(reverse=True)
 
i = 0
sum2 = 0
 
while i <= len(tall) - 1 :
    if sum2 > sum1 // 2:
        break
    else:
        sum2 += tall[i]
        i += 1
 
 
print(i)