import keyboard
import time
running = True
def quit():
    global running
    running = False

keyboard.add_hotkey('q',quit)
time.sleep(3)

while running:
    keyboard.write("Ganesh's Favourite word\n",delay=0)
    time.sleep(0.1)

