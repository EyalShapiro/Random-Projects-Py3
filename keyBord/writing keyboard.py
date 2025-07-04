"""
הקלד אוטומטי
ולחץ על המקלדת באופן אוטומטי
"""

import keyboard
import time

time.sleep(2)  # wait for 2 seconds before starting to type
keyboard.write("eyal\n")


keyboard.press_and_release("shift + r, shift + k, \n")
keyboard.press_and_release("R, e5444")

# it blocks until ctrl is pressed
keyboard.wait("Ctrl")
