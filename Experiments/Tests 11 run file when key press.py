# import keyboard
#
#
# def on_key_event(event):
#     print("Key:", event.name)
#
#
# keyboard.on_press(on_key_event)
# keyboard.wait("esc")  # Waits until you press the 'esc' key

from pynput import keyboard


def on_press(key):
    try:
        if key.char == 'y':
            # Call your specific function here
            print("Function called because 'y' is pressed")
        else:
            print('Key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

