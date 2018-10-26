import csv

'''
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for line in list(exampleReader):
    print(*line)
'''

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'egg', 'ham'])
outputWriter.writerow(['Hello', 12, 'ham'])
outputFile.close()
