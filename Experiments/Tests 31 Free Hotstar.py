import time
import sys
import pyautogui

time.sleep(3)
pyautogui.FAILSAFE = False
time.sleep(0.5)
pyautogui.rightClick(922, 401)
time.sleep(0.5)
pyautogui.click(1070, 155)

free_time = 290

while True:
    for i in range(free_time):
        sys.stdout.write(f"\rTime: {free_time - i}")
        sys.stdout.flush()
        time.sleep(1)

    pyautogui.click(1353, 1)
    time.sleep(0.5)
    pyautogui.rightClick(922, 401)
    time.sleep(0.5)
    pyautogui.click(1070, 155)
