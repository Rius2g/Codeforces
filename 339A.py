sekvens = input()
sek2 = []

for k in sekvens:
    if k != '+':
        sek2.append(k)


sek2.sort()


i = 0

sek3 = ''

while i <= len(sek2) -1:
    sek3 += sek2[i]
    if i < len(sek2) -1:
        sek3 += '+'
    else:
        pass
    i +=1

print(sek3) 
