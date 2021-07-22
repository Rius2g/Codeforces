import re
 
key = input()
key = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), key, 1)
 
print(key)