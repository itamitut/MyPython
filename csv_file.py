import csv

villains = [['Doctor', 'No'],
            ['Rosa', 'Klebb'],
            ['Mister', 'Big'],
            ['Auric', 'Goldfinger']]
with open('villains.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)
with open('villains.csv', 'rt') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin if row]
print(villains)
