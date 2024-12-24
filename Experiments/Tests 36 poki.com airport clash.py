import threading
import time
from pynput.mouse import Button, Controller
import keyboard

mouse = Controller()

# Flag to keep track of whether the left mouse click should be pressed
clicking = False


def click_mouse():
    """Continuously presses the left mouse button while `clicking` is True."""
    global clicking
    while True:
        if clicking:
            mouse.click(Button.left)
        time.sleep(0.001)  # Adjust the delay to control the click frequency


def toggle_clicking():
    """Toggles the clicking state when Caps Lock is pressed."""
    global clicking
    caps_lock_pressed = False
    while True:
        if keyboard.is_pressed('caps lock'):
            if not caps_lock_pressed:
                clicking = not clicking
                caps_lock_pressed = True
        else:
            caps_lock_pressed = False
        time.sleep(0.1)  # Small delay to prevent high CPU usage


# Create threads for mouse clicking and Caps Lock toggle
click_thread = threading.Thread(target=click_mouse, daemon=True)
toggle_thread = threading.Thread(target=toggle_clicking, daemon=True)

# Start the threads
click_thread.start()
toggle_thread.start()

# Keep the main thread running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated.")