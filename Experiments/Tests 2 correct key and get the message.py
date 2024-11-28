from pynput import keyboard


def printmessage():
    print("The printmessage function is called")
    return 0


key = '<alt>+c'


with keyboard.GlobalHotKeys({
    key: printmessage
}) as l:
    l.join()
