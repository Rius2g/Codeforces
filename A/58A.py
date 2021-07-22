m = "hello"
 
def chatroom():
    x = 0
    s = input()
    for i in range(len(s)):
        if s[i] == m[x]:
            x += 1
        if x == 5:
            return "YES"
    return "NO"
print(chatroom())
 