import pyautogui

element=input('Enter comment')
query='testing'
# pyautogui.sleep(10)
# this for query
pyautogui.click(1890,86)
pyautogui.sleep(1)
# enter text
pyautogui.typewrite(query)
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.sleep(20)
# 1229 719
# click on video
pyautogui.click(1282,712)
pyautogui.sleep(10)
# for commenting
# click on comment
pyautogui.click(1893,699)
pyautogui.sleep(5)
# click on field text
pyautogui.click(1538,915)
pyautogui.sleep(5)
pyautogui.typewrite(element)
pyautogui.sleep(5)
# click on send
pyautogui.click(1887,627)
pyautogui.sleep(5)
# close comment section
pyautogui.click(1898,347)
pyautogui.sleep(1)

# scroll down
# pyautogui.scroll(-10)