import pyautogui

class ScreenCapture:
    def __init__(self, x, y, width, height, save_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.save_path = save_path

    def capture(self):
        # Take a screenshot of the specified region
        screenshot = pyautogui.screenshot(region=(self.x, self.y, self.width, self.height))

        # Save the screenshot as an image
        screenshot.save(self.save_path)
