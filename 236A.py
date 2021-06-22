streng = input()

liste = []

for k in streng:
    if k not in liste:
        liste.append(k)

if len(liste) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")