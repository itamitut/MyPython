import threading
import time

print('Start of program.')


def takeANap(m, n):
    time.sleep(n)
    print('Wake up!')


for i in range(1, 6):
    threadObj = threading.Thread(target=takeANap, args= (0,i))
    threadObj.start()

print('End of program.')
