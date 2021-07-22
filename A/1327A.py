x = int(input())
 
for t in range(x):
    n, k = map(int, input().split())
    if (n%2) != (k%2):
        print("NO")
    else:
        if (n >= k*k):
            print("YES")
        else:
            print("NO")
 