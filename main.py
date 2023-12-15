import pyautogui
import time
import button
from pynput.keyboard import HotKey, Key, KeyCode, Listener


def click_image(image):
    #while True:
    time.sleep(2)
    i = 0
    while True:
        try:            
            res = pyautogui.locateOnScreen(image,confidence=0.8,region=(0,0,1916,1134))
            res_center=pyautogui.center(res)
            pyautogui.moveTo(res_center)
            pyautogui.click(res_center)
            print ("I can see it")
            break
        except pyautogui.ImageNotFoundException:
            i=i+1
            print( i)
  
       
        #break
    
click_image(button.bt_ServerLocaltion)
click_image(button.bt_ServerLocaltion_Singapore)
click_image(button.bt_CreatePassLobby)
click_image(button.bt_CreateGame)
time.sleep(4)
click_image(button.bt_StartGame)