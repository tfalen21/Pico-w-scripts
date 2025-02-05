import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#This script requires you to install CircuitPython onto your Pico and the adafruit_hid library.

# Initialize keyboard
keyboard = Keyboard(usb_hid.devices)

# Delay before execution (for safety)
time.sleep(3)

# Example payload: Open Notepad and type a message (Windows)
keyboard.send(Keycode.WINDOWS, Keycode.R)  # Open Run dialog
time.sleep(0.5)
keyboard.send(Keycode.BACKSPACE)  # Ensure clean input
time.sleep(0.2)
keyboard.send(Keycode.N, Keycode.O, Keycode.T, Keycode.E, Keycode.P, Keycode.A, Keycode.D)
time.sleep(0.5)
keyboard.send(Keycode.ENTER)  # Open Notepad
time.sleep(1)
keyboard.send(Keycode.H, Keycode.E, Keycode.L, Keycode.L, Keycode.O)
time.sleep(0.2)
keyboard.send(Keycode.SPACE)
keyboard.send(Keycode.W, Keycode.O, Keycode.R, Keycode.L, Keycode.D, Keycode.EXCLAMATION)
keyboard.send(Keycode.ENTER)
