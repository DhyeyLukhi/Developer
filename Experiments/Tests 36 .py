import time
import sys
import pyautogui
import keyboard

# time.sleep(3)
# pyautogui.FAILSAFE = False
# time.sleep(0.5)
# pyautogui.rightClick(922, 401)
# time.sleep(0.5)
# pyautogui.click(1070, 155)

free_time = 290

while True:
    key_press = keyboard.read_event()
    if key_press.event_type == keyboard.KEY_DOWN:
        if key_press.name == 'p':
            time.sleep(0.5)
            print(f"{key_press.name}")
    # sys.stdout.write(f"\rTime: {free_time - i}")
    # sys.stdout.flush()
    # time.sleep(1)


# pyautogui.click(1353, 1)
# time.sleep(0.5)
# pyautogui.rightClick(922, 401)
# time.sleep(0.5)
# pyautogui.click(1070, 155)
