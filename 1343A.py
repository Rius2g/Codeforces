x = int(input())
 
i = 0
 
while i < x:
    n = int(input())
    k = 4
    while k <= n+1:
        if n % (k-1) == 0:
            m = n / (k-1)
            print(int(m))
            break
        k *= 2
    i += 1