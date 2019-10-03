from pyautogui import *
import webbrowser
import time
import threading



passcode = prompt('Please enter your PIN.')
print(passcode) # in the future use this to inform the prog of ur passcode to type in


url = 'cis.usma.edu/cis/main.cfm'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
x=lambda: webbrowser.get(chrome_path).open(url)
t=threading.Thread(target=x)
t.start()

print("moving")
moveTo(1025, 274) #location of cert
print("done moving")
time.sleep(8)
print("sleep 3")
click() #click on correct cert
print('clicked')
press('enter')
time.sleep(5)
print("sleep 2")
moveTo(889,573)#click in pin box
click()
print("should be in box")

press(['3','7','6','2','9','0','4','3','enter'], interval=0.1)
print("pressed numbers")

moveTo(980,1023) #click "I agree"
time.sleep(5)
click()
print("should be on main page")

moveTo(255,723) #click "Signout Book"
time.sleep(3)
click()
print("should be in signout book")

moveTo(594,496) #click "In Room (Taps)"
time.sleep(3)
click()
print("should have clicked button")

moveTo(47,533) #click "Sign Out"
#click()
print("should be hovering over \"Sign Out\"")




