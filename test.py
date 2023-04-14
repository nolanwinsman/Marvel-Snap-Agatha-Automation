import pyautogui
import time
import random

# set the coordinates of the three locations where the mouse will drag
locations = [(1025, 850), (1300, 850), (1530, 850)]

# set the starting x-coordinate of the mouse movement
x_start, y_start = 1000, 1150

# set the increment of the x-coordinate movement
x_increment = 50

# set the delay between each mouse movement
delay = 0.3

# loop through the x-coordinates, clicking and dragging to one of the locations every 25 pixels
for x in range(x_start, x_start + 650, x_increment):
    # move the mouse to the current x-coordinate
    pyautogui.moveTo(x, y_start)

    # click and hold the mouse
    pyautogui.mouseDown()

    # drag the mouse to one of the locations
    random_location = random.choice(locations)
    pyautogui.moveTo(random_location, duration=0.4)

    # release the mouse
    pyautogui.mouseUp()

    # add a delay before moving to the next x-coordinate
    time.sleep(delay)
