import pyautogui
import time
import button
import hero
number_hero_Luna=0
number_hero_WinterWyvern=0
def click_image(image):
    i = 0
    while True:
        try:
            res = pyautogui.locateOnScreen(
                image, confidence=0.8, region=(0, 0, 1916, 1134))
            res_center = pyautogui.center(res)
            time.sleep(1)
            pyautogui.moveTo(res_center)
            pyautogui.click(res_center)
            pyautogui.moveTo(0, 0)
            print("I can see it")

            break
        except pyautogui.ImageNotFoundException:
            i = i+1
            if i > 120:
                break
            print(i)
            time.sleep(0.5)
def get_round(image):
    i = 0
    while True:
        try:
            res = pyautogui.locateOnScreen(
                image, confidence=0.8, region=(0, 0, 1916, 1134))
            res_center = pyautogui.center(res)
            # time.sleep(1)
            # pyautogui.moveTo(res_center)
           # pyautogui.click(res_center)
            print("I can see it")

            break
        except pyautogui.ImageNotFoundException:
            i = i+1
            if i > 120:
                break
            print(i)
            time.sleep(0.5)
def get_hero_level(image):
    try:
        res = pyautogui.locateOnScreen(
            image, confidence=0.8, region=(0, 0, 1916, 1134))
        #res_center = pyautogui.center(res)
        #pyautogui.moveTo(res_center)
        return True
    except pyautogui.ImageNotFoundException:
        return None
    # pyautogui.click(res_center)
    # pyautogui.moveTo(0,0)
def buy_hero(hero):
    try:
        res = pyautogui.locateOnScreen(
            hero, confidence=0.8, region=(0, 0, 1916, 1134))
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        return True
    except pyautogui.ImageNotFoundException:
        return None
    
def buy_hero_Luna(hero_Level):
    global number_hero_Luna
    while True:
        if get_hero_level(hero.Luna_lv1) is True:
            number_hero_Luna=1
            break        
        break    
    if hero_Level > number_hero_Luna:
        for n in range(0, 4):
            buy = buy_hero(hero.Luna)
            if buy is True:
                number_hero_Luna = number_hero_Luna+1
                print("mua: ", number_hero_Luna)
                if hero_Level <= number_hero_Luna:
                    break


def round_1():
    click_image(button.bt_CreateCustomLobby)
    click_image(button.bt_ServerLocaltion)
    click_image(button.bt_ServerLocaltion_Singapore)
    click_image(button.bt_CreatePassLobby)
    pyautogui.write("as")
    click_image(button.bt_CreateGame)
    # time.sleep(4)
    click_image(button.bt_StartGame)
    click_image(button.bt_Accept)  # start game
