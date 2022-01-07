import keyboard
import time
import tkinter as tk
from tkinter import simpledialog

running = True

# Set up q to quit the program loop
def quit():
    global running
    running = False
keyboard.add_hotkey('esc',quit)

# Setup tkinter root process
root = tk.Tk()
root.withdraw()

# Prompt for input to write
text_to_write = simpledialog.askstring(title="Prompt",
                                  prompt="What text would you like to write?:")

# Cut string if too long
max_text_length = 20
text_to_write = text_to_write[:max_text_length] if len(text_to_write) > max_text_length else text_to_write

# Delay before starting loop
time.sleep(3)

# Typing loop
while running:
    keyboard.write(text_to_write + "\n", delay=0)
    time.sleep(0.1)
