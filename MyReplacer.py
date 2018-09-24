import re
with open('a.txt', 'r') as a, open('a1.txt', 'w') as a1:
    for line in a:
        line = re.sub(r'(#.*?#)', 'Новый шаблон', line)
        a1.write(line)
