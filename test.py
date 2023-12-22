import pyautogui
import time
import random 
count = 0
v = 0.55
    
movementTime = random.uniform(0.24, 1.88)
timeToSleep = random.uniform(25.32, 62.5)    
success = False

for count in range(6):
   
    try:
        print("Try:", count, " Sample:", count, " Image:", count)
        pictureOfShaftsX, pictureOfShaftsY = pyautogui.locateCenterOnScreen('data\\image\\StartGame.png'.format(count), confidence=v)
    except TypeError:
        continue
    except pyautogui.ImageNotFoundException:
        continue
    
print("Found shafts at: ", pictureOfShaftsX, pictureOfShaftsY)