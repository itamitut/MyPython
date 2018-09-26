from datetime import date

f = open('today.txt', 'w')
this_day = date.today()
f.write(str(this_day))
f.close()
