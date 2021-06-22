streng = input().strip()


if streng.isupper():
    streng2 = streng.lower()
    print(streng2)
elif streng[0].islower() and (not streng[1:] or streng[1:].isupper()):
    streng2 = streng.capitalize()
    print(streng2)
else:
    print(streng)

