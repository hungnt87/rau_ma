import os
import threading
import time
import pyautogui
import pydirectinput
import controller.global_variables as cgv
from controller.button import Button
from controller.filelog import logger
from controller.global_variables import global_event

path = cgv.PathManager()
REGION_HERO = (537, 125, 1158, 406)

REGION_SELL_HERO: tuple[int, int, int, int] = (662, 791, 704, 358)
CONFIDENCE = 0.8
GRAYSCALE: bool = True
number_winter_wyvern: int = 0
number_hood_wink: int = 1
number_dazzale: int = 0
need_WinterWyvern: int = 1
need_Hoodwink: int = 1
need_Dazzale: int = 1
need_Luna = 1
need_Windranger = 1
need_Oracle = 1
need_TrollWarlord = 1
need_Morphling = 1
need_WitchDoctor = 1
need_DarkWillow = 1
need_Clinkz = 1
need_Sniper = 5
need_Snapfire = 5
need_DrowRanger = 5
need_TemplarAssassin = 5
need_Zet = 5

previous_hero = dict()


class Hero:
    img = None
    img_lv1 = None

    def __init__(self, name: str, number: int = 0, need_buy: int = 0):
        self.name = name
        self.img = self._get_hero_img(name)
        self.img_lv1 = self._get_hero_img_lv1(name)
        self.number = number
        self.need_buy = need_buy
        self.region = REGION_HERO
        self.region_sell = REGION_SELL_HERO
        self.confidence = CONFIDENCE
        self.grayscale = GRAYSCALE

    def _get_hero_img(self, para_name):
        # global HERO_IMG
        if self.img is None:
            file_name = para_name + ".png"
            self.img = path.get_absolute_path(os.path.join("assets", "img", "hero", file_name)
                                              )
        return self.img

    def _get_hero_img_lv1(self, para_name):
        # global HERO_IMG
        if self.img_lv1 is None:
            file_name = para_name + "_lv1.png"
            self.img_lv1 = path.get_absolute_path(os.path.join("assets", "img", "hero", file_name)
                                                  )
        return self.img_lv1

    def reset_hero_number(self):
        self.number = 0

    def buy(self):
        if global_event.check_event():
            return False
        # logger.debug("Bat dau tim hero {}".format(self.name))
        try:
            res_center = pyautogui.locateCenterOnScreen(self.img, confidence = self.confidence, region = self.region,
                                                        grayscale = self.grayscale, )
            # res_center = pyautogui.center(res)
            # pydirectinput.moveTo(res_center.x, res_center.y)
            # pydirectinput.click(res_center[0], res_center[1])
            # pydirectinput.moveTo(201, 213)
            # logger.debug("Tim thay hinh anh {}".format(self.img))
            return res_center
        except pyautogui.ImageNotFoundException:
            # logger.debug("Khong tim thay hinh anh {}".format(self.img))
            return False
        except Exception as e:
            logger.error(e)
            return None

    def buy_hero(self):
        if global_event.check_event():
            return False
        # logger.debug("Bat dau tim hero {}".format(self.name))
        i = 0
        count_buy = self.need_buy - self.number
        # logger.debug(f"Con {count_buy} {self.name} can mua")
        while i <= 2:
            if global_event.check_event():
                break
            # logger.debug(f"Tim hero {self.name} lan thu {i}")
            i = i + 1
            # logger.debug(i)
            if count_buy > 0:
                # logger.debug(f"Con {count_buy} {self.name} can mua")
                location = self.buy()
                if location:
                    # pydirectinput.moveTo(location[0], location[1])
                    previous_hero[location] = self
                    return True
                else:
                    pass
            else:
                return None

    def check_hero(self):
        if global_event.check_event():
            return False
        try:
            if global_event.check_event():
                return False
            pyautogui.locateCenterOnScreen(self.img, confidence = self.confidence, region = REGION_HERO,
                                           grayscale = self.grayscale, )
            return True
        except pyautogui.ImageNotFoundException:
            return False
        except Exception as e:
            logger.error(e)
            return False

    def sell_hero(self):
        if global_event.check_event():
            return False
        global REGION_SELL_HERO
        if self.number == 0:
            # khong mua hero nay
            self.number = 1
            return True
        else:
            try:
                res_center = pyautogui.locateCenterOnScreen(self.img_lv1, confidence = self.confidence,
                                                            region = self.region_sell, grayscale = self.grayscale, )
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
    if global_event.check_event():
        return False
    global previous_hero
    if previous_hero:
        logger.debug("Ban dang mua hero ")
        for key, value in list(previous_hero.items()):
            if check_sell_hero(value) is True:
                pydirectinput.click(key[0], key[1])
                if Button.check_money() is True:
                    logger.info(f"Ban da mua thanh cong 1 {value.name}")
                    value.number = value.number + 1
                    cgv.count_of_buy += 1
                    del previous_hero[key]
                else:
                    look_region = (key[0], key[1], 267, 312)
                    cgv.set_money(False)
                    if Button.click_lock(value.name, look_region) is True:
                        # del previous_item[key]
                        logger.debug("Khong du tien, Khoa hero")

                    else:
                        del previous_hero[key]

    else:
        logger.debug("Khong co hero khoa o round truoc")


WinterWyvern = Hero(name = "WinterWyvern", number = number_winter_wyvern, need_buy = need_WinterWyvern)

HoodWink = Hero(name = "Hoodwink", number = number_hood_wink, need_buy = need_Hoodwink)
Dazzale = Hero(name = "Dazzale", number = number_dazzale, need_buy = need_Dazzale)
# hero lv2

Luna = Hero(name = "Luna", need_buy = 1)

Windranger = Hero(name = "Windranger", need_buy = 1)

Oracle = Hero(name = "Oracle", need_buy = 1)

TrollWarlord = Hero(name = "TrollWarlord", need_buy = 1)
Morphling = Hero(name = "Morphling", need_buy = 1)
WitchDoctor = Hero(name = "WitchDoctor", need_buy = 1)

# hero lv3

DarkWillow = Hero(name = "DarkWillow", need_buy = 1)

Clinkz = Hero(name = "Clinkz", need_buy = 1)

# hero lv4
Sniper = Hero(name = "Sniper", need_buy = 5)
Snapfire = Hero(name = "Snapfire", need_buy = 1)
# hero lv5
DrowRanger = Hero(name = "DrowRanger", need_buy = 1)
TemplarAssassin = Hero(name = "TemplarAssassin", need_buy = 1)
Zet = Hero(name = "Zet", need_buy = 1)


def check_sell_hero(hero: Hero):
    if global_event.check_event():
        return False
    if hero.name == Clinkz.name:
        if TrollWarlord.sell_hero() is True:
            return True

    if hero.name == WitchDoctor.name:
        if Morphling.sell_hero() is True:
            return True
    if hero.name == DarkWillow.name:
        if Windranger.sell_hero() is True:
            return True
    if hero.name == Sniper.name:
        if Dazzale.sell_hero() is True:
            return True
        if Luna.sell_hero() is True:
            return True
    if hero.name == Snapfire.name:
        if Oracle.sell_hero() is True:
            return True
        if Morphling.sell_hero() is True:
            return True
        if WitchDoctor.sell_hero() is True:
            return True
    if hero.name == DrowRanger.name:
        if HoodWink.sell_hero() is True:
            return True
    if hero.name == TemplarAssassin.name:
        if WinterWyvern.sell_hero() is True:
            return True
    if hero.name == Zet.name:
        if Clinkz.sell_hero() is True:
            return True
        if TrollWarlord.sell_hero() is True:
            return True
    return True


def buy_all_hero(round_number):
    if global_event.check_event():
        return False
    logger.info(f"Bat dau mua hero in round: {round_number}")
    if cgv.check_money() is False:
        logger.debug("Khong du tien, next round")
        return None
    thread_buy_dazzale = threading.Thread(target = Dazzale.buy_hero, args = ())
    thread_buy_oracle = threading.Thread(target = Oracle.buy_hero, args = ())
    thread_buy_hoodwink = threading.Thread(target = HoodWink.buy_hero, args = ())
    thread_buy_winter_wyvern = threading.Thread(target = WinterWyvern.buy_hero, args = ())
    thread_buy_luna = threading.Thread(target = Luna.buy_hero, args = ())
    thread_buy_troll_warlord = threading.Thread(target = TrollWarlord.buy_hero, args = ())
    thread_buy_morphling = threading.Thread(target = Morphling.buy_hero, args = ())
    thread_buy_windranger = threading.Thread(target = Windranger.buy_hero, args = ())
    thread_buy_dark_willow = threading.Thread(target = DarkWillow.buy_hero, args = ())
    thread_buy_clinkz = threading.Thread(target = Clinkz.buy_hero, args = ())
    thread_buy_witch_doctor = threading.Thread(target = WitchDoctor.buy_hero, args = ())
    thread_buy_sniper = threading.Thread(target = Sniper.buy_hero, args = ())
    thread_buy_snapfire = threading.Thread(target = Snapfire.buy_hero, args = ())
    thread_buy_drow_ranger = threading.Thread(target = DrowRanger.buy_hero, args = ())
    thread_buy_templar_assassin = threading.Thread(target = TemplarAssassin.buy_hero, args = ())
    thread_buy_zet = threading.Thread(target = Zet.buy_hero, args = ())

    if round_number <= 3:
        thread_buy_dazzale.start()
        thread_buy_oracle.start()
        thread_buy_hoodwink.start()
        thread_buy_winter_wyvern.start()
        thread_buy_luna.start()
        thread_buy_troll_warlord.start()
        thread_buy_morphling.start()
        thread_buy_windranger.start()
        thread_buy_dazzale.join()
        thread_buy_oracle.join()
        thread_buy_hoodwink.join()
        thread_buy_winter_wyvern.join()
        thread_buy_luna.join()
        thread_buy_troll_warlord.join()
        thread_buy_morphling.join()
        thread_buy_windranger.join()
    elif round_number <= 10:
        # start
        thread_buy_dazzale.start()
        thread_buy_oracle.start()
        thread_buy_hoodwink.start()
        thread_buy_winter_wyvern.start()
        thread_buy_luna.start()
        thread_buy_troll_warlord.start()
        thread_buy_morphling.start()
        thread_buy_windranger.start()
        thread_buy_dark_willow.start()
        thread_buy_clinkz.start()
        thread_buy_witch_doctor.start()
        # join
        thread_buy_dazzale.join()
        thread_buy_oracle.join()
        thread_buy_hoodwink.join()
        thread_buy_winter_wyvern.join()
        thread_buy_luna.join()
        thread_buy_troll_warlord.join()
        thread_buy_morphling.join()
        thread_buy_windranger.join()
        thread_buy_dark_willow.join()
        thread_buy_clinkz.join()
        thread_buy_witch_doctor.join()

    else:
        # start
        thread_buy_sniper.start()
        thread_buy_snapfire.start()
        thread_buy_drow_ranger.start()
        thread_buy_templar_assassin.start()
        thread_buy_zet.start()
        # join
        thread_buy_sniper.join()
        thread_buy_snapfire.join()
        thread_buy_drow_ranger.join()
        thread_buy_templar_assassin.join()
        thread_buy_zet.join()
    buy_all_previous_hero()
    logger.info(f"Ket thuc mua hero in round: {round_number}")


def reset_hero():
    if global_event.check_event():
        return False
    WinterWyvern.reset_hero_number()
    HoodWink.reset_hero_number()
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
    buy_all_hero(5)
    # Oracle.buy()
    # Oracle.buy_hero()
    # print(Oracle.need_buy)
    pass
