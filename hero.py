import pyautogui
import time


# hero lv1
WinterWyvern_hero = r"data\image\hero\lv1\WinterWyvern.png"
WinterWyvern_lv1 = r"data\image\hero\lv1\WinterWyvern_lv1.png"
number_hero_WinterWyvern = 0

# hero lv2
Luna = r"data\image\hero\lv2\Luna.png"
Luna_lv1 = r"data\image\hero\lv2\Luna_lv1.png"
number_hero_Luna = 0

Windranger=r"data\image\hero\lv2\Windranger.png"
Windranger_lv1="data\image\hero\lv2\Windranger.png"
number_hero_Windranger=0

PriestArcane = r"data\image\hero\lv2\PriestArcane.png"




def get_hero_level(hero_img):
    try:
        res = pyautogui.locateOnScreen(
            hero_img, confidence=0.8, region=(0, 0, 1916, 1134))        
        return True
    except pyautogui.ImageNotFoundException:
        return None

def buy_hero(hero_img):
    try:
        res = pyautogui.locateOnScreen(
            hero_img, confidence=0.8, region=(0, 0, 1916, 1134))
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        pyautogui.click(res_center)
        return True
    except pyautogui.ImageNotFoundException:
        return None

def buy_hero_Luna(luna_number):
    global number_hero_Luna
    while True:
        if get_hero_level(Luna_lv1) is True:
            number_hero_Luna = 1
            break
        break
    if luna_number > number_hero_Luna:
        for n in range(0, 4):
            buy = buy_hero(Luna)
            if buy is True:
                number_hero_Luna = number_hero_Luna+1
                print("mua: ", number_hero_Luna)
                if luna_number <= number_hero_Luna:
                    break
def buy_hero_Windranger(hero_number):
    global number_hero_Windranger
    print("Windranger: ",number_hero_Windranger)
    while True:
        if get_hero_level(Windranger) is True:
            number_hero_Windranger = 1
            break
        break
    if hero_number > number_hero_Windranger:
        for n in range(0, 4):
            buy = buy_hero(Windranger)
            if buy is True:
                number_hero_Windranger = number_hero_Windranger+1
                print("mua: ", number_hero_Windranger)
                if hero_number <= number_hero_Windranger:
                    break

