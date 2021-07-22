x = input()
 
string = []
nostring = ["A", "O", "Y", "E", "U", "I", "a", "o", "y", "e", "u", "i"]
 
i = 0
string.append(".")
 
while i < len(x):
    if x[i] in nostring:
        pass     
    elif ord(x[i]) < 97:
        nyttord = ord(x[i]) + 32
        if string[len(string)-1] == ".":
            string.append(chr(nyttord))
        else:
            string.append(".")
            string.append(chr(nyttord))
    else:
        if string[len(string)-1] == ".":
            string.append(x[i])
        else:
            string.append(".")
            string.append(x[i])
    i += 1
    
 
k = "".join(string)
 
print(k)