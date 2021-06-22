streng = input()


liste = ["H", "Q", "9"]

yes = 0

for k in streng:
    if k in liste:
        yes = 1
        break

if yes == 1:
    print("YES")
else:
    print("NO")