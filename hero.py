import pyautogui
import time


class infor_hero:
    def __init__(self, para_name, para_number_hero):
        self.name = para_name
        self.img = "data\\image\\hero\\"+para_name+".png"
        self.lv1_img = "data\\image\\hero\\"+para_name+"lv1.png"
        self.lv2_img = "data\\image\\hero\\"+para_name+"lv2.png"
        self.lv3_img = "data\\image\\hero\\"+para_name+"lv3.png"
        self.lv4_img = "data\\image\\hero\\"+para_name+"lv4.png"
        self.lv5_img = "data\\image\\hero\\"+para_name+"lv5.png"
        self.number = para_number_hero

#hero lv1
WinterWyvern_number = 1
WinterWyvern = infor_hero("WinterWyvern", WinterWyvern_number)
Hoodwink_number=0
Hoodwink=infor_hero("Hoodwink",Hoodwink_number)

# hero lv2
Luna_number = 0
Luna = infor_hero("Luna", Luna_number)
Windranger_number = 0
Windranger = infor_hero("Windranger", Windranger_number)
PriestArcane_number = 0
PriestArcane = infor_hero("PriestArcane", PriestArcane_number)
TrollWarlord_number=0
TrollWarlord=infor_hero("TrollWarlord",TrollWarlord_number)

# def get_hero_level(infor_hero):
#     try:
        
#         res = pyautogui.locateOnScreen(
#             infor_hero.lv1_img, confidence=0.8, region=(0, 0, 1916, 1134))
#         return 1
#     except pyautogui.ImageNotFoundException:
#         return 0


def buy_hero(hero_img):
    try:
        res = pyautogui.locateOnScreen(
            hero_img, confidence=0.8, region=(0, 0, 1916, 1134))
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        time.sleep(0.2)
        pyautogui.click(res_center)
        time.sleep(0.2)
        return True
    except pyautogui.ImageNotFoundException:
        return None


def buy_hero_infor(infor_hero, number_hero):
    number = infor_hero.number

    if number_hero > number:
        number_buy=number_hero-number
        for n in range(0, number_buy):
            buy = buy_hero(infor_hero.img)
            if buy is True:
                number=number+1
                print("mua: ", number)
        infor_hero.number=number              



# def buy_hero_Windranger(hero_number):
#     global number_hero_Windranger
#     print("Windranger: ", number_hero_Windranger)
#     while True:
#         if get_hero_level(Windranger) is True:
#             number_hero_Windranger = 1
#             break
#         break
#     if hero_number > number_hero_Windranger:
#         for n in range(0, 4):
#             buy = buy_hero(Windranger)
#             if buy is True:
#                 number_hero_Windranger = number_hero_Windranger+1
#                 print("mua: ", number_hero_Windranger)
#                 if hero_number <= number_hero_Windranger:
#                     break
