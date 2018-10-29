import pyautogui
import time
time.sleep(5)
counter = 0
x = 123
limit = 1058
while counter < 80:
    if x < limit:
        pyautogui.keyDown('ctrl')
        pyautogui.moveTo(760, x)
        pyautogui.click()
        x += 45
        counter += 1
    else:
        pyautogui.keyUp('ctrl')
        pyautogui.scroll(-1040)
        x = 123
