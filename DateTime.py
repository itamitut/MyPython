from datetime import datetime
import re
#Создаем файл и записываем в него текущую дату:
f = open('today.txt', 'w')
now = datetime.now()
f.write(str(now))
f.close()
# Cчитываем строку и ищем в ней соответствие по шаблону:
with open('today.txt', 'r') as f:
    today_string = f.readline()
match = re.findall(r'-(.*)-', today_string)
print(match)

