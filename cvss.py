import csv

villains = [['Doctor', 'No'],
     ['Rosa', 'Klebb'],
     ['Mister', 'Big'],
     ['Auric', 'Goldfinger']]
with open('villains.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

