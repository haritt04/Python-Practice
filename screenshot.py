import time
import pyautogui

def screenshot():
    time.sleep(5)  # Wait for 5 seconds before taking a screenshot
    img = pyautogui.screenshot()
    img.save(r"D:\Python\test.png")  # Save the screenshot in D:\Python
    img.show()  # Open the screenshot

screenshot()
