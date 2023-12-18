import pyautogui
import time

import button


class infor_hero:
    def __init__(self, para_name, para_number_hero=0):
        self.name = para_name
        self.img = "data\\image\\hero\\" + para_name + ".png"
        self.lv1_img = "data\\image\\hero\\" + para_name + "_lv1.png"
        self.lv2_img = "data\\image\\hero\\" + para_name + "_lv2.png"
        self.lv3_img = "data\\image\\hero\\" + para_name + "_lv3.png"
        self.lv4_img = "data\\image\\hero\\" + para_name + "_lv4.png"
        self.lv5_img = "data\\image\\hero\\" + para_name + "_lv5.png"
        self.number = para_number_hero

    def reset_hero_number(self):
        self.number = 0


# hero lv1

WinterWyvern = infor_hero("WinterWyvern", 1)

Hoodwink = infor_hero("Hoodwink")

# hero lv2

Luna = infor_hero("Luna")

Windranger = infor_hero("Windranger")

Oracle = infor_hero("Oracle")

TrollWarlord = infor_hero("TrollWarlord")

Dazzale = infor_hero("Dazzale")

# hero lv3

DarkWillow = infor_hero("DarkWillow")

Clinkz = infor_hero("Clinkz")

# hero lv4
Sniper=infor_hero("Sniper")

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
    i = 0
    while True:
        if i >= 4:
            break
        number = infor_hero.number
        if number_hero > number:
            i = i + 1
            number_buy = number_hero - number
            if buy_hero(infor_hero.img) is True:
                if button.check_not_money():
                    break
                else:
                    number = number + 1

                    infor_hero.number = number
                    print("Bạn đã mua thành công 1 hero {}, bạn đang có {}, bạn cần mua thêm {} nữa".format(
                        infor_hero.name, infor_hero.number, number_hero - number))

        else:
            print("ban da du hero {} roi, ko can mua nua".format(infor_hero.name))
            break

def buy_Sniper():
    buy_hero_infor(Sniper,10)
def buy_DarkWillow():
    buy_hero_infor(DarkWillow,5)
def buy_Clinkz():
    buy_hero_infor(Clinkz,5)
def buy_WinterWyvern():
    buy_hero_infor(WinterWyvern,4)
def buy_Hoodwink():
    buy_hero_infor(Hoodwink,5)
def reset_hero():
    """
    Reset the hero number to 0
    """
    global WinterWyvern, Hoodwink, Luna, Windranger, Oracle, TrollWarlord, Dazzale, DarkWillow, Clinkz
    WinterWyvern.reset_hero_number()
    Hoodwink.reset_hero_number()
    Luna.reset_hero_number()
    Windranger.reset_hero_number()
    Oracle.reset_hero_number()
    TrollWarlord.reset_hero_number()
    Dazzale.reset_hero_number()
    DarkWillow.reset_hero_number()
    Clinkz.reset_hero_number()
    Sniper.reset_hero_number()
