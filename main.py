import keyboard
import time
import tkinter as tk
from tkinter import simpledialog

running = True

# Set up q to quit the program loop
def quit():
    global running
    running = False
    print("Terminating Program")
keyboard.add_hotkey('esc',quit)

# Setup tkinter root process
root = tk.Tk()
root.withdraw()

# Prompt for input to write
text_to_write = simpledialog.askstring(title="Prompt",
                                  prompt="What text would you like to write?:")

# Delay before starting loop
time.sleep(3)

# Typing loop
while running:
    for character in text_to_write:
        keyboard.write(character, delay=0.0001)
        if not running:
            break
    
    # Write a new line
    keyboard.write("\n", delay=0)