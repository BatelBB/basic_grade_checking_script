import pyautogui
import time
import webbrowser

webbrowser.open("https://gezer1.bgu.ac.il/meser/login.php")
time.sleep(2)
pyautogui.moveTo(1458, 488)
time.sleep(1)
pyautogui.leftClick()
pyautogui.write("MY_ID")
time.sleep(1)
pyautogui.moveTo(1862, 566)
pyautogui.leftClick()
time.sleep(1)
pyautogui.moveTo(1837, 772)
pyautogui.leftClick()
time.sleep(8)
pyautogui.moveTo(1056, 719)
pyautogui.leftClick()



