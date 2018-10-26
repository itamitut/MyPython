import pyautogui
import time, os, datetime

os.chdir('C:\\Tools')
os.makedirs('Screenshots', exist_ok=True)
os.chdir('Screenshots')
for i in range(1, 10):
    im = pyautogui.screenshot()
    t = datetime.datetime.now()
    dateMask = t.strftime('%d%m_%H_%M_%S')
    fileName = 'Screenshot#' + dateMask + '.png'
    im.save(fileName)
    time.sleep(3)
