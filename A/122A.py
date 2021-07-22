x = int(input())
 
lucky_numbers = [4, 7, 47, 74, 447, 474, 477, 744, 747, 777]
 
i = 0
h = 0
if x in lucky_numbers:
    h = 1
else:
    while i < len(lucky_numbers):
        if x % lucky_numbers[i] == 0:
            h = 1
            break
        else:
            i += 1
 
if h ==  1:
    print("YES")
else:
    print("NO")