x, y = map(int, input().split())
 
sum = x * y
 
if sum % 2 == 0:
    sum /= 2
else:
    sum -= 1
    sum /= 2
 
 
print("%.0f" %  sum)