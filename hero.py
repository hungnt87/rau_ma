import pyautogui
import time
import button
from log import logger

class HeroInfor:
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


count_buy_hero = 0


def reset_count_buy_hero():
    global count_buy_hero
    count_buy_hero = 0


def get_count_buy_hero():
    global count_buy_hero
    return count_buy_hero


# hero lv1

WinterWyvern = HeroInfor("WinterWyvern", 1)

Hoodwink = HeroInfor("Hoodwink")

# hero lv2

Luna = HeroInfor("Luna")

Windranger = HeroInfor("Windranger")

Oracle = HeroInfor("Oracle")

TrollWarlord = HeroInfor("TrollWarlord")

Dazzale = HeroInfor("Dazzale")

# hero lv3

DarkWillow = HeroInfor("DarkWillow")

Clinkz = HeroInfor("Clinkz")

# hero lv4
Sniper = HeroInfor("Sniper")

# hero lv5
DrowRanger = HeroInfor("DrowRanger")
TemplarAssassin = HeroInfor("TemplarAssassin")
Zet = HeroInfor("Zet")


def buy_hero(hero_img):
    try:
        res = pyautogui.locateOnScreen(
            hero_img, confidence=0.8, region=(0, 0, 1916, 1134))
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        pyautogui.click(res_center)
        return True
    except pyautogui.ImageNotFoundException:
        return False


def buy_hero_infor(HeroInfor, number_hero=1):
    logger.info("Bat dau tim hero {}".format(HeroInfor.name))
    global count_buy_hero
    i = 0
    while True:
        if i >= 4:
            break
        number = HeroInfor.number
        if number_hero > number:
            i = i + 1
            number_buy = number_hero - number
            if buy_hero(HeroInfor.img) is True:
                if button.check_not_money():
                    break
                else:
                    number = number + 1

                    HeroInfor.number = number
                    count_buy_hero = count_buy_hero + 1
                    logger.info("Ban da mua thanh cong 1 hero {}, ban dang co {}, ban can mua them {} ".format(
                        HeroInfor.name, HeroInfor.number, number_hero - number))
                    #logger.info("Bạn đã mua hero lần thứ {}".format(count_buy_hero))
            else:
                logger.warning("Khong tim thay hero {} lan {}".format(HeroInfor.name, i))

        else:
            #logger.info("Bạn đã đủ hero {} rồi, không cần mua nữa".format(HeroInfor.name))
            break


def check_hero(HeroInfor):
    try:
        res = pyautogui.locateOnScreen(
            HeroInfor.img, confidence=0.8, region=(0, 0, 1916, 1134))
        res_center = pyautogui.center(res)
        # pyautogui.moveTo(res_center)
        # time.sleep(0.2)
        # yautogui.click(res_center)
        # time.sleep(0.2)
        return res_center
    except pyautogui.ImageNotFoundException:
        return None


def sell_hero(HeroInfor):
    try:
        res = pyautogui.locateOnScreen(
            HeroInfor.lv1_img, confidence=0.8, region=(0, 0, 1916, 1134))
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        pyautogui.rightClick(res_center)
        time.sleep(0.2)
        new_res = (res_center.x + 25, res_center.y)
        pyautogui.moveTo(new_res)
        time.sleep(0.2)
        pyautogui.click(new_res)
        # time.sleep(0.2    )

        # time.sleep(0.2)
        return True
    except pyautogui.ImageNotFoundException:
        return False


def buy_dazzale():
    buy_hero_infor(Dazzale, 1)


def buy_oracle():
    buy_hero_infor(Oracle, 1)


def buy_sniper():
    if check_hero(Sniper):
        sell_hero(Dazzale)
        sell_hero(Oracle)
    buy_hero_infor(Sniper, 10)


def buy_dark_willow():
    buy_hero_infor(DarkWillow, 5)


def buy_clinkz():
    buy_hero_infor(Clinkz, 5)


def buy_winter_wyvern():
    buy_hero_infor(WinterWyvern, 4)


def buy_hoodwink():
    buy_hero_infor(Hoodwink, 1)


def buy_drow_ranger():
    if check_hero(DrowRanger):
        sell_hero(Hoodwink)
    buy_hero_infor(DrowRanger, 5)


def buy_templar_assassin():
    if check_hero(TemplarAssassin):
        sell_hero(WinterWyvern)
    buy_hero_infor(TemplarAssassin, 5)


def buy_zet():
    if check_hero(Zet):
        sell_hero(Clinkz)
    buy_hero_infor(Zet, 5)

def buy_all_hero(round_number):
    if round_number ==3:
        buy_dazzale()
        buy_oracle()
        buy_hoodwink()
    elif round_number<=8:
        buy_dazzale()
        buy_oracle()
        buy_hoodwink()
        buy_dark_willow()
        buy_clinkz()
    else:
        buy_dark_willow()
        buy_clinkz()
        buy_sniper()
        buy_drow_ranger()
        buy_templar_assassin()
        buy_zet()


def reset_hero():
    """
    Reset the hero number to 0
    """
    global WinterWyvern, Hoodwink, Luna, Windranger, Oracle, TrollWarlord
    global Dazzale, DarkWillow, Clinkz, Zet, DrowRanger, TemplarAssassin
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
    Zet.reset_hero_number()
    DrowRanger.reset_hero_number()
    TemplarAssassin.reset_hero_number()
    logger.info("Reset the hero number to 0")
