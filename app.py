#Import the modules
import time
import keyboard

#Define a function to press Ctrl+s
def save():
    keyboard.press_and_release('ctrl+s')
while True:
    save()
    print('ctrl+s has been pressed')
    time.sleep(10)

    