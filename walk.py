import os

for folderName, subfolders, fileNames in os.walk('C:\dell'):
    print('Текущая папка' + folderName)
    for subfolder in subfolders:
        print('Подпапка папки ' + folderName + "subfolder")
    for filename in fileNames:
        print('Файл в папке: ' + subfolder + ' ' + filename)
