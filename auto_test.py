import pyautogui
import time 
def move():
    try:
        x, y = pyautogui.locateCenterOnScreen('logo2.png')
        pyautogui.moveTo(x, y, 0.1)
        pyautogui.click()
    except TypeError:
        print("its fucked")

def toggle():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')
    pyautogui.keyUp('tab')

def paste():
    pyautogui.keyDown('ctrl')
    time.sleep(.2)
    pyautogui.keyDown('v')
    time.sleep(.2)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')