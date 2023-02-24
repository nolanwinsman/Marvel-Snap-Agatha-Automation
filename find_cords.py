
from screen_capture import ScreenCapture


# Create an instance of the ScreenCapture class
# x, y, width, height, filename
capture = ScreenCapture(1600, 1230, 140, 100, 'test.png')
capture.capture()
print("test.png created")
