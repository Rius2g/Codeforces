x = int(input())
 
i = 0
while i < x:
    string = str(input())
 
    if len(string) > 10:
        print(string[0], end ="")
        print(len(string) - 2, end = "")
        print(string[len(string) - 1])
    else:
        print(string)
    i += 1