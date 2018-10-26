import pyautogui, time, random

x = 1000
y = 500
try:
	while True:
		x += random.randrange(-10, 10)
		y += random.randrange(-10, 10)
		pyautogui.moveTo(x, y)
		time.sleep(1)
except KeyboardInterrupt:
	print('Finished')