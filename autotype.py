import pyautogui as pg
import time

print('Starting in 5 seconds')
time.sleep(5)

for i in range(1000):
    pg.write('I will not copy from the internet')
    pg.press('Enter')
    time.sleep(0.5)
