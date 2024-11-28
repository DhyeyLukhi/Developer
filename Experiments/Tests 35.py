import pyautogui
import time

# Get the current mouse position (to calculate a coordinate manually)
print("Move your mouse to the desired position within 5 seconds...")
time.sleep(5)
x, y = pyautogui.position()
print(f"Right click position: {x}, {y}")
time.sleep(5)
x,y = pyautogui.position()
print(f"Icognito Posiion: {x} {y}")

# Example of clicking at a specific position
# Replace x, y with desired coordinates
# pyautogui.click(x, y)

