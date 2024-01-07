import os
import sys
import threading
import pyautogui
import time
import pydirectinput
import controller.global_variables as cgv
from controller.button import Button
from controller.filelog import logger


event = cgv.Event()
path = cgv.PathManager()
REGION_HERO = (537, 125, 1158, 406)

REGION_SELL_HERO = (662, 791, 704, 358)
CONFIDENCE = 0.8
GRAYSCALE = True
count_WinterWyvern = 0
count_Hoodwink = 1
previous_hero = dict()


class Hero:
    name = ""
    img = None
    img_lv1 = None

    def __init__(self, para_name, para_number_hero=0):
        self.name = para_name
        self.img = self._get_hero_img(para_name)
        self.img_lv1 = self._get_hero_img_lv1(para_name)
        self.number = para_number_hero
        self.region = REGION_HERO
        self.region_sell = REGION_SELL_HERO
        self.confidence = CONFIDENCE
        self.grayscale = True
        self.count_buy_hero = 0

    def _get_hero_img(self, para_name):
        # global HERO_IMG
        if self.img is None:
            file_name = para_name + ".png"
            self.img = path.get_absolute_path(
                os.path.join("assets", "img", "hero", file_name)
            )
        return self.img

    def _get_hero_img_lv1(self, para_name):
        # global HERO_IMG
        if self.img_lv1 is None:
            file_name = para_name + "_lv1.png"
            self.img_lv1 = path.get_absolute_path(
                os.path.join("assets", "img", "hero", file_name)
            )
        return self.img_lv1

    def reset_hero_number(self):
        self.number = 0

    def buy(self):
        if event.check_event():
            return False
        logger.debug("Bat dau tim hero {}".format(self.name))
        try:
            res_center = pyautogui.locateCenterOnScreen(
                self.img,
                confidence=self.confidence,
                region=self.region,
                grayscale=self.grayscale,
            )
            # res_center = pyautogui.center(res)
            # pydirectinput.moveTo(res_center.x, res_center.y)
            pydirectinput.click(res_center[0], res_center[1])
            pydirectinput.moveTo(201, 213)
            return res_center
        except pyautogui.ImageNotFoundException:
            # logger.debug("Khong tim thay hinh anh {}".format(hero_img))
            return None
        except Exception as e:
            logger.error(e)
            return

    def buy_hero(self, number_hero=1):
        if event.check_event():
            return False
        # logger.debug("Bat dau tim hero {}".format(Hero.name))

        i = 0
        number = self.number
        if number_hero == None:
            number_buy = 1
            pass
        else:
            number_buy = number_hero - number
        while True:
            if event.check_event():
                break
            if i >= 2:
                break
            i = i + 1
            # logger.debug(i)
            if number_buy > 0:
                if number_hero == None:
                    number_buy = 0
                    pass
                else:
                    number_buy = number_hero - number
                location = self.buy()
                if location:
                    if Button.check_money() is False:
                        cgv.set_money(False)
                        box_lock = (location.x, location.y, 267, 312)
                        if Button.click_lock_hero(box_lock) is True:
                            previous_hero[location] = self
                        return False
                        # break
                    else:
                        number = number + 1
                        if number_hero == None:
                            number_buy = 0
                        else:
                            number_buy = number_hero - number
                        self.number = number
                        cgv.add_count_of_buy(number=1)
                        if number_hero == None:
                            logger.info(
                                f"Ban da mua thanh cong 1 hero {self.name} da khoa round truoc"
                            )
                        else:
                            logger.info(
                                f"Ban da mua thanh cong 1 hero {self.name}, ban can mua them {number_buy}"
                            )
                        return True
                else:
                    # logger.debug("Khong tim thay hinh anh {}".format(Hero.name))
                    time.sleep(0.2)
            else:
                break

    def check_hero(self):
        if event.check_event():
            return False

        try:
            if event.check_event():
                return False
            res = pyautogui.locateCenterOnScreen(
                self.img,
                confidence=self.confidence,
                region=REGION_HERO,
                grayscale=self.grayscale,
            )
            return True
        except pyautogui.ImageNotFoundException:
            return False
        except Exception as e:
            logger.error(e)
            return False

    def sell_hero(self):
        if event.check_event():
            return
        global REGION_SELL_HERO
        try:
            res_center = pyautogui.locateCenterOnScreen(
                self.img_lv1,
                confidence=self.confidence,
                region=self.region_sell,
                grayscale=self.grayscale,
            )
            pydirectinput.rightClick(res_center.x, res_center.y)
            time.sleep(1)
            pydirectinput.click(res_center.x + 20, res_center.y)
            pydirectinput.moveTo(213, 201)
            logger.debug(f"Ban thanh cong hero {self.name}")
            return True
        except pyautogui.ImageNotFoundException:
            logger.debug(f"Khong co hero  {self.name} de ban")
            return False
        except Exception as e:
            logger.error(e)
            return False


def buy_all_previous_hero():
    if event.check_event():
        return False

    if previous_hero:
        logger.debug("Ban dang mua hero khoa o round truoc")
        for key, value in list(previous_hero.items()):
            pydirectinput.click(key[0], key[1])
            if Button.check_money() is False:
                return False
            else:
                logger.info(f"Ban da mua thanh cong 1 {value.name}")
                value.number = value.number + 1
                cgv.add_count_of_buy(number=1)
                del previous_hero[key]

    else:
        logger.debug("Khong co hero khoa o round truoc")


WinterWyvern = Hero("WinterWyvern", count_WinterWyvern)

Hoodwink = Hero("Hoodwink", count_Hoodwink)
Dazzale = Hero("Dazzale")
# hero lv2

Luna = Hero("Luna")

Windranger = Hero("Windranger")

Oracle = Hero("Oracle")

TrollWarlord = Hero("TrollWarlord")
Morphling = Hero("Morphling")
WitchDoctor = Hero("WitchDoctor")

# hero lv3

DarkWillow = Hero("DarkWillow")

Clinkz = Hero("Clinkz")

# hero lv4
Sniper = Hero("Sniper")
Snapfire = Hero("Snapfire")
# hero lv5
DrowRanger = Hero("DrowRanger")
TemplarAssassin = Hero("TemplarAssassin")
Zet = Hero("Zet")


def buy_hood_wink():
    Hoodwink.buy_hero(1)


def buy_winter_wyvern():
    WinterWyvern.buy_hero(1)


def buy_dazzale():
    Dazzale.buy_hero(1)


def buy_oracle():
    Hero("Oracle", 1)


def buy_morphling():
    Morphling.buy_hero(1)


def buy_troll_warlord():
    TrollWarlord.buy_hero(1)


def buy_luna():
    Luna.buy_hero(1)


def buy_wind_ranger():
    Windranger.buy_hero(1)


def buy_clinkz():
    if Clinkz.number == 0:
        if Clinkz.check_hero() is True:
            if TrollWarlord.number == 0:
                TrollWarlord.number = 1
            else:
                TrollWarlord.sell_hero()
            Clinkz.buy_hero(1)


def buy_witch_doctor():
    if WitchDoctor.number == 0:
        if WitchDoctor.check_hero() is True:
            if Morphling.number == 0:
                Morphling.number = 1
            else:
                Morphling.sell_hero()
            WitchDoctor.buy_hero(1)


def buy_dark_willow():
    if DarkWillow.number == 0:
        if DarkWillow.check_hero() is True:
            if Windranger.number == 0:
                Windranger.number = 1
            else:
                Windranger.sell_hero()
            DarkWillow.buy_hero(5)
    else:
        DarkWillow.buy_hero(5)


def buy_sniper():
    if Sniper.number == 0:
        if Sniper.check_hero() is True:
            if Dazzale.number == 0:
                Dazzale.number = 1
            else:
                Dazzale.sell_hero()
            Sniper.buy_hero(5)
    else:
        Sniper.buy_hero(5)


def buy_snapfire():
    if Snapfire.number == 0:
        if Snapfire.check_hero() is True:
            if Oracle.number == 0:
                Oracle.number = 1
            else:
                Oracle.sell_hero()
            if Morphling.number == 0:
                Morphling.number = 1
            else:
                Morphling.sell_hero()
            Snapfire.buy_hero(5)
    else:
        Snapfire.buy_hero(5)


def buy_drow_ranger():
    if DrowRanger.number == 0:
        if DrowRanger.check_hero() is True:
            if Hoodwink.number == 0:
                Hoodwink.number = 1
            else:
                Hoodwink.sell_hero()
            DrowRanger.buy_hero(5)
    else:
        DrowRanger.buy_hero(5)


def buy_templar_assassin():
    if TemplarAssassin.number == 0:
        if TemplarAssassin.check_hero() is True:
            if WinterWyvern.number == 0:
                WinterWyvern.number = 1
            else:
                WinterWyvern.sell_hero()
            TemplarAssassin.sell_hero()
    else:
        TemplarAssassin.buy_hero(5)


def buy_zet():
    if Zet.number == 0:
        if Zet.check_hero() is True:
            if Clinkz.number == 0:
                Clinkz.number = 1
            else:
                Clinkz.sell_hero()
            if TrollWarlord.number == 0:
                TrollWarlord.number = 1
            else:
                TrollWarlord.sell_hero()
            Zet.buy_hero(5)
    else:
        Zet.buy_hero(5)


def buy_all_hero(round_number):
    if event.check_event():
        return False
    logger.info(f"Bat dau mua hero in round: {round_number}")
    if cgv.check_money() is False:
        logger.debug("Khong du tien, next round")
        return False
    if round_number <= 3:
        buy_dazzale()
        buy_oracle()
        buy_hood_wink()
        buy_winter_wyvern()
        buy_luna()
        buy_troll_warlord()
        buy_morphling()
        buy_wind_ranger()
    elif round_number <= 8:
        buy_dazzale()
        buy_oracle()
        buy_hood_wink()
        buy_winter_wyvern()
        buy_luna()
        buy_troll_warlord()
        buy_morphling()
        buy_wind_ranger()
        buy_dark_willow()
        buy_clinkz()
        buy_witch_doctor()
        buy_sniper()
        buy_snapfire()
        buy_drow_ranger()
        buy_templar_assassin()
        buy_zet()


def reset_hero():
    # global Windranger, Luna, TrollWarlord, Morphling, DarkWillow, Clinkz, Sniper, Snapfire, DrowRanger, TemplarAssassin, Zet
    WinterWyvern.reset_hero_number()
    Hoodwink.reset_hero_number()
    Dazzale.reset_hero_number()
    Oracle.reset_hero_number()
    TrollWarlord.reset_hero_number()
    Luna.reset_hero_number()
    Windranger.reset_hero_number()
    Morphling.reset_hero_number()
    DarkWillow.reset_hero_number()
    Clinkz.reset_hero_number()
    Sniper.reset_hero_number()
    Snapfire.reset_hero_number()
    DrowRanger.reset_hero_number()
    TemplarAssassin.reset_hero_number()
    Zet.reset_hero_number()


def reset_previous_hero():
    global previous_hero
    previous_hero.clear()


if __name__ == "__main__":
    time.sleep(2)
    # reset_hero()
    # print(Hoodwink.number)
    Hoodwink.buy_hero(1)
    Windranger.buy_hero(1)
    WinterWyvern.buy_hero(1)
    pass
