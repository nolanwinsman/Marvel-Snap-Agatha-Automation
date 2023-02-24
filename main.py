import time
import pydirectinput
from image_comparator import ImageComparator
from screen_capture import ScreenCapture

# Create an instance of the ImageComparator class
comparator = ImageComparator('news.png', 'frame.png')

# Create an instance of the ScreenCapture class
# x, y, width, height, filename
capture = ScreenCapture(1600, 1230, 140, 100, 'frame.png')

TOTAL_MATCHES = 0

def match():
    print(f"Starting Match {TOTAL_MATCHES}")
    pydirectinput.moveTo(1660, 1275) # Move the mouse to the x, y coordinates to the "end turn" button
    score = 0.0
    while score < 0.5: 
        time.sleep(0.5)
        pydirectinput.click()
        time.sleep(0.5)
        # Call the capture() method to take a screenshot and save it as an image
        capture.capture()
        time.sleep(0.5)
        score = comparator.compare_images()
        print(f"Score: {score}")



def loop():
        while True:
            pydirectinput.moveTo(1300, 1100) # Moves the mouse to the play button
            pydirectinput.click()
            # Searching for a Match
            time.sleep(8)
            match()
            time.sleep(1)
            pydirectinput.moveTo(1300, 1275) # Moves the mouse to the "Main" button
            pydirectinput.click() 
            global TOTAL_MATCHES
            TOTAL_MATCHES += 1
            time.sleep(1)
            # exit()



def main():
    loop()



if __name__ == "__main__":
    main()
    #match()