import pyautogui
import time

time.sleep(1)
count = 0
while count <= 500:
    pyautogui.typewrite("send \n")
    pyautogui.typewrite("I am waiting")
    pyautogui.press("enter")
    count = count + 1
