import time
import sys
import keyboard
import pyautogui

time.sleep(3)
pyautogui.FAILSAFE = False
time.sleep(0.5)
pyautogui.rightClick(922, 401)
time.sleep(0.5)
pyautogui.click(1070, 155)
#
# free_time = 290
# print("GO")

while True:
    key = keyboard.read_event()
    if key.event_type == keyboard.KEY_DOWN:
        if key.name == 'p':
            time.sleep(0.3)
            pyautogui.click(1353, 1)
            time.sleep(0.5)
            pyautogui.rightClick(922, 401)
            time.sleep(0.5)
            pyautogui.click(1070, 155)
            # print("Key Pressed")

    # sys.stdout.write(f"\rTime: {free_time - i}")
    # sys.stdout.flush()
    # time.sleep(1)


