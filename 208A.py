import re

print(re.sub('^\ *|\ *$', '', re.sub('\ +', ' ', re.sub('WUB', ' ', input()))))