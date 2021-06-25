k = int(input())

while k:
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    sum = 0
    if x > y: #swap the two
        m = x
        x = y
        y = m  
    ans1 = 0 
    ans2 = 0 
    ans1 = x*a + y*a
    z = y - x
    ans2 = z*a + x * b 
    if ans1 < ans2:
        print(ans1)
    else:
        print(ans2)
    k -= 1

