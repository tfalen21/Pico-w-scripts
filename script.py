import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize keyboard
keyboard = Keyboard(usb_hid.devices)

# Delay before execution (for safety)
time.sleep(3)

# Open Run dialog (Win + R)
keyboard.press(Keycode.WINDOWS, Keycode.R)
keyboard.release_all()
time.sleep(0.5)

# Ensure clean input
keyboard.send(Keycode.BACKSPACE)
time.sleep(0.2)

# Type "notepad" correctly
notepad_text = [Keycode.N, Keycode.O, Keycode.T, Keycode.E, Keycode.P, Keycode.A, Keycode.D]

for key in notepad_text:
    keyboard.press(key)
    time.sleep(0.05)
    keyboard.release_all()

time.sleep(0.5)

# Press Enter to open Notepad
keyboard.send(Keycode.ENTER)
time.sleep(2)  # Extended delay to allow Notepad to fully open

# Type "Hello World!" into Notepad
message = "Hello World!"  # Using a string instead of keycodes

for char in message:
    if char.isupper():
        keyboard.press(Keycode.SHIFT, getattr(Keycode, char.upper(), Keycode.SPACE))
        keyboard.release_all()
    elif char == " ":
        keyboard.send(Keycode.SPACE)
    elif char == "!":
        keyboard.press(Keycode.SHIFT, Keycode.ONE)
        keyboard.release_all()
    else:
        keyboard.send(getattr(Keycode, char.upper(), Keycode.SPACE))
    
    time.sleep(0.05)  # Delay to prevent skipping characters

# Press Enter at the end
keyboard.send(Keycode.ENTER)
