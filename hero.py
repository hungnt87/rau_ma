import pyautogui
import time
import button
from log import logger
from PIL import Image
import pydirectinput

REGION_HERO = (537, 125, 1158, 406)

REGION_SELL_HERO = (662, 791, 704, 358)


# import opencv
def main():
    # time.sleep(2)
    # buy_WinterWyvern()
    # test_reset_hero()
    pass


class HeroInfor:
    HERO_IMG = None

    def __init__(self, para_name, para_number_hero=0):
        self.name = para_name
        self.img = self.get_hero_img(para_name)
        # self.img = f"data/image/hero/{para_name}.png"
        self.lv1_img = "data\\image\\hero\\" + para_name + "_lv1.png"
        self.lv2_img = "data\\image\\hero\\" + para_name + "_lv2.png"
        self.lv3_img = "data\\image\\hero\\" + para_name + "_lv3.png"
        self.lv4_img = "data\\image\\hero\\" + para_name + "_lv4.png"
        self.lv5_img = "data\\image\\hero\\" + para_name + "_lv5.png"
        self.number = para_number_hero

    def reset_hero_number(self):
        self.number = 0

    def get_hero_img(self, para_name, hero_img=None):
        # global HERO_IMG
        if self.HERO_IMG is None:
            self.HERO_IMG = Image.open(f"data/image/hero/{para_name}.png")
        return self.HERO_IMG


# def get_hero_img(para_name, hero_img=None):
#     # global HERO_IMG
#     if hero_img is None:
#         hero_img = Image.open(f"data/image/hero/{para_name}.png")
#     return hero_img


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
    global REGION_HERO
    try:
        res = pyautogui.locateOnScreen(
            hero_img, confidence=0.8, region=REGION_HERO, grayscale=True
        )
        res_center = pyautogui.center(res)
        # pydirectinput.moveTo(res_center.x, res_center.y)
        pydirectinput.click(res_center.x, res_center.y)
        pydirectinput.moveTo(201, 213)
        return res_center
    except pyautogui.ImageNotFoundException:
        # logger.debug("Khong tim thay hinh anh {}".format(hero_img))
        return False
    except Exception as e:
        logger.error(e)
        return False


# def main():
hero_status_money = True


def reset_hero_status_money():
    global hero_status_money
    hero_status_money = True


def buy_hero_infor(HeroInfor, number_hero=1):
    # logger.debug("Bat dau tim hero {}".format(HeroInfor.name))
    global count_buy_hero, hero_status_money
    i = 0
    number = HeroInfor.number
    number_buy = number_hero - number
    while True:
        if i >= 2:
            break
        i = i + 1
        # logger.debug(i)
        if number_buy > 0:
            number_buy = number_hero - number
            location = buy_hero(HeroInfor.img)
            if location is not False:
                if button.check_not_money() is True:
                    box_lock = (location.x, location.y, 267, 312)
                    button.click_lock_hero(box_lock)
                    hero_status_money = False
                    return False
                    # break
                else:
                    number = number + 1
                    number_buy = number_hero - number
                    HeroInfor.number = number
                    count_buy_hero = count_buy_hero + 1
                    logger.info(
                        f"Ban da mua thanh cong 1 hero {HeroInfor.name}, ban can mua them {number_buy}"
                    )
                    return True
            else:
                # logger.debug("Khong tim thay hinh anh {}".format(HeroInfor.name))
                time.sleep(0.2)
        else:
            break


def check_hero(HeroInfor):
    global REGION_HERO
    try:
        res = pyautogui.locateCenterOnScreen(
            HeroInfor.img, confidence=0.8, region=REGION_HERO, grayscale=True
        )
        return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception as e:
        logger.error(e)
        return False


def sell_hero(HeroInfor):
    global REGION_SELL_HERO
    try:
        res_center = pyautogui.locateCenterOnScreen(
            HeroInfor.lv1_img, confidence=0.8, region=REGION_SELL_HERO, grayscale=True
        )
        pydirectinput.rightClick(res_center.x, res_center.y)
        time.sleep(0.2)
        pydirectinput.click(res_center.x + 20, res_center.y)
        pydirectinput.moveTo(213, 201)
        logger.debug(f"Ban thanh cong hero {HeroInfor.name}")
        return True
    except pyautogui.ImageNotFoundException:
        logger.debug(f"Khong co hero  {HeroInfor.name} de ban")
        return False
    except Exception as e:
        logger.error(e)
        return False


def buy_dazzale():
    buy_hero_infor(Dazzale, 1)


def buy_oracle():
    buy_hero_infor(Oracle, 1)


def buy_WinterWyvern():
    if WinterWyvern.number == 0:
        if check_hero(WinterWyvern) is True:
            if Hoodwink.number == 0:
                Hoodwink.number = 1
            else:
                sell_hero(Hoodwink)
            buy_hero_infor(WinterWyvern, 5)
    else:
        buy_hero_infor(WinterWyvern, 5)


def buy_sniper():
    if Sniper.number == 0:
        if check_hero(Sniper) is True:
            if Dazzale.number == 0:
                Dazzale.number = 1
            else:
                sell_hero(Dazzale)
            if Oracle.number == 0:
                Oracle.number = 1
            else:
                sell_hero(Oracle)
            buy_hero_infor(Sniper, 10)
    else:
        buy_hero_infor(Sniper, 10)


def buy_dark_willow():
    buy_hero_infor(DarkWillow, 5)


def buy_clinkz():
    buy_hero_infor(Clinkz, 1)


def buy_hoodwink():
    buy_hero_infor(Hoodwink, 1)


def buy_drow_ranger():
    if DrowRanger.number == 0:
        if check_hero(DrowRanger) is True:
            if Hoodwink.number == 0:
                Hoodwink.number = 1
            else:
                sell_hero(Hoodwink)
            buy_hero_infor(DrowRanger, 5)
    else:
        buy_hero_infor(DrowRanger, 5)


def buy_templar_assassin():
    if TemplarAssassin.number == 0:
        if check_hero(TemplarAssassin) is True:
            if WinterWyvern.number == 0:
                WinterWyvern.number = 1
            else:
                sell_hero(WinterWyvern)
            buy_hero_infor(TemplarAssassin, 5)
        else:
            buy_hero_infor(TemplarAssassin, 5)


def buy_zet():
    if Zet.number == 0:
        if check_hero(Zet) is True:
            if Clinkz.number == 0:
                Clinkz.number = 1
            else:
                sell_hero(Clinkz)
            buy_hero_infor(Zet, 5)
    else:
        buy_hero_infor(Zet, 5)


def buy_all_hero(round_number):
    logger.info(f"Bat dau mua hero in round: {round_number}")
    if round_number == 3:
        buy_dazzale()
        buy_oracle()
        buy_hoodwink()
    elif round_number <= 8:
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
    try:
        logger.debug("Reset the hero number to 0")
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
    except Exception as e:
        logger.error(e)


def test_reset_hero():
    # reset_hero()
    print(f"WinterWyvern number = {WinterWyvern.number}")
    print(f"Hoodwink.number = {Hoodwink.number}")
    print(Luna.number)
    print(Windranger.number)
    print(Oracle.number)
    print(TrollWarlord.number)
    print(Dazzale.number)
    print(DarkWillow.number)
    print(Clinkz.number)
    print(Sniper.number)
    print(Zet.number)
    print(DrowRanger.number)
    print(TemplarAssassin.number)


def install_hero():
    # Clinkz=HeroInfor("Clinkz")
    if Sniper.img is None:
        logger.debug("None")
    else:
        logger.debug("da ton tai")


if __name__ == "__main__":
    main()
    pass
