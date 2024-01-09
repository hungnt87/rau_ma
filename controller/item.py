import os
import threading
import time

import pyautogui
import pydirectinput

import controller.global_variables as cgv
from controller.button import Button
from controller.filelog import logger
from controller.global_variables import global_event, path

previous_item = dict()
REGION_BUY_ITEM = (394, 321, 1384, 692)
CONFIDENCE_BUY_ITEM = 0.8
GRAYSCALE_BUY_ITEM = True


class Item:
    img = None

    def __init__(self, name, number_need_buy=5):
        self.name = name
        self.number = 0
        self.number_need_buy = number_need_buy
        self.img = self.get_item_img(name)

    def reset_item_number(self):
        self.number = 0

    def get_item_img(self, name):
        # global HERO_IMG
        if self.img is None:
            file_name = name + ".png"

            self.img = self.img = path.get_absolute_path(
                os.path.join("assets", "img", "item", file_name)
            )
        return self.img

    def buy(self):
        # logger.info("Ban dang tim item {}".format(ItemInfo.name))
        if global_event.check_event():
            return False
        # global previous_item, REGION_BUY_ITEM, CONFIDENCE_BUY_ITEM, GRAYSCALE_BUY_ITEM
        number = self.number
        count_of_buy = self.number_need_buy - self.number
        if count_of_buy > 0:
            try:
                location = pyautogui.locateCenterOnScreen(
                    self.img, confidence=CONFIDENCE_BUY_ITEM, region=REGION_BUY_ITEM, grayscale=GRAYSCALE_BUY_ITEM, )
                previous_item[
                    location] = self  # pydirectinput.click(location[0], location[1])  # pydirectinput.moveTo(222, 213)  # if Button.check_money():  #     self.number += 1  #     cgv.add_count_of_buy(1)  #     logger.info(f"Ban da mua thanh cong 1 cai {self.name}")  #     return True  # else:  #     look_region = (location.x, location.y, 267, 312)  #     cgv.set_money(False)  #     if Button.click_lock(self.name, look_region) is True:  #         previous_item[location] = self  #     return False

            except pyautogui.ImageNotFoundException:
                return False
            except Exception as e:
                logger.error(e)
                return False
        else:
            pass  # logger.debug(  #     f"Ban da co {ItemInfo.number} item {ItemInfo.name} , du so luong roi"  # )


Attack10EveryBuyPlus5_lv2 = Item("Attack10EveryBuyPlus5_lv2")
Attack12_Kill1000_Unique_lv2 = Item("Attack12_Kill1000_Unique_lv2", number_need_buy=1)
Attack16_Arcane16_lv3 = Item("Attack16_Arcane16_lv3")
Attack16_Strike16_lv3 = Item("Attack16_Strike16_lv3")
Attack35_Kill1000_Unique_lv5 = Item("Attack35_Kill1000_Unique_lv5", number_need_buy=1)
Bicycle_lv3 = Item("Bicycle_lv3",number_need_buy = 0)
Cooldown16_Kill1000_Unique_lv2 = Item("Cooldown16_Kill1000_Unique_lv2", number_need_buy=1)
Cooldown21_lv5 = Item("Cooldown21_lv5",number_need_buy = 1)
Cooldown45_Speed15_lv6 = Item("Cooldown45_Speed15_lv6",number_need_buy = 1)
Critical9_Luck_lv3 = Item("Critical9_Luck_lv3",number_need_buy = 1)
Critical16_Kill1000_Unique_lv2 = Item("Critical16_Kill1000_Unique_lv2", number_need_buy=1)
Critical20_Defense_lv3 = Item("Critical20_Defense_lv3", number_need_buy=1)
Critical30_Defense10_lv5 = Item("Critical30_Defense10_lv5", number_need_buy=1)
Critical40_Kill1000_Unique_lv5 = Item("Critical40_Kill1000_Unique_lv5", number_need_buy=1)
Defense20_Speed10_lv2 = Item("Defense20_Speed10_lv2", number_need_buy=0)
Critical21_For_Precise_lv3 = Item("Critical21_For_Precise_lv3")
EnemyCount10_lv6 = Item("EnemyCount10_lv6")
Evasion6_For_Precise_lv1 = Item("Evasion6_For_Precise_lv1", number_need_buy=2)
Evasion8_Speed5_lv1 = Item("Evasion8_Speed5_lv1", number_need_buy=2)
Evasion12_Strike6_lv2 = Item("Evasion12_Strike6_lv2", number_need_buy=2)
Evasion13_Health13_lv2 = Item("Evasion13_Health13_lv2", number_need_buy=2)
Evasion16_Investment16_lv3 = Item("Evasion16_Investment16_lv3", number_need_buy=2)
Evasion21_Attack5_lv4 = Item("Evasion21_Attack5_lv4", number_need_buy=2)
Exp20_Range5_lv1 = Item("Exp20_Range5_lv1")
Exp40_Luck6_lv2 = Item("Exp40_Luck6_lv2")
Exp45_Attack4_lv2 = Item("Exp45_Attack4_lv2")
ExtraDamage10_lv3 = Item("ExtraDamage10_lv3")
ExtraDamage13_For_Precise_lv2 = Item("ExtraDamage13_For_Precise_lv2")
ExtraDamage14_Kill1000_Unique_lv2 = Item("ExtraDamage14_Kill1000_Unique_lv2", number_need_buy=1)
ExtraDamage30_Luck30_lv5 = Item("ExtraDamage30_Luck30_lv5")
ExtraDamage30_lv6 = Item("ExtraDamage30_lv6")
ExtraDamage40_Kill100_Unique_lv5 = Item("ExtraDamage40_Kill100_Unique_lv5", number_need_buy=1)
Health30_Speed20_lv4 = Item("Health30_Speed20_lv4")
Health48_For_Precise_lv3 = Item("Health48_For_Precise_lv3")
Health88_lv5 = Item("Health88_lv5")
HealthRegen10_For_Precise_lv1 = Item("HealthRegen10_For_Precise_lv1")
HealthRegen12_HitRecovery15_lv2 = Item("HealthRegen12_HitRecovery15_lv2")
HealthRegen18_Mango50_lv2 = Item("HealthRegen18_Mango50_lv2")
HealthRegen20_Strike20_lv2 = Item("HealthRegen20_Strike20_lv2")
HealthRegen45_Invest99_lv5 = Item("HealthRegen45_Invest99_lv5")
Holding_Plus_Cooldown35_lv4 = Item("Holding_Plus_Cooldown35_lv4", number_need_buy=0)
Holding_Plus_Def32_lv4 = Item("Holding_Plus_Def32_lv4", number_need_buy=0)
Holding_Plus_HealthRegen30_lv4 = Item("Holding_Plus_HealthRegen30_lv4", number_need_buy=0)
Immunity_Unique_lv5 = Item("Immunity_Unique_lv5", number_need_buy=1)
Immunity6_lv3 = Item("Immunity6_lv3")
Immunity10_lv5 = Item("Immunity10_lv5")
ImmunityCount4_lv4 = Item("ImmunityCount4_lv4")
Investment88_For_Precise_lv1 = Item("Investment88_For_Precise_lv1")
Investment138_Defense3_lv2 = Item("Investment138_Defense3_lv2")
Investment198_Speed7_lv3 = Item("Investment198_Speed7_lv3")
Investment218_Evasion8_lv3 = Item("Investment218_Evasion8_lv3")
Investment368_HitRecovery18_lv5 = Item("Investment368_HitRecovery18_lv5")
Locomotive_lv2 = Item("Locomotive_lv2")
Luck13_lv1 = Item("Luck13_lv1", number_need_buy=1)
Luck32ForPrecise_lv2 = Item("Luck32ForPrecise_lv2", number_need_buy=1)
Luck45_HitRecovery25_lv3 = Item("Luck45_HitRecovery25_lv3", number_need_buy=1)
Luck54_Arcane27_lv4 = Item("Luck54_Arcane27_lv4", number_need_buy=1)
Luck60_Speed25_lv4 = Item("Luck60_Speed25_lv4", number_need_buy=1)
MasterChefHat_lv2 = Item("MasterChefHat_lv2")
Minazuki_lv4 = Item("Minazuki_lv4")
MultishotDamage20_lv3 = Item("MultishotDamage20_lv3")
MultishotDamage20_lv3 = Item("MultishotDamage20_lv3")
PantyMask_lv6 = Item("PantyMask_lv6")
PickupRange100_lv1 = Item("PickupRange100_lv1", number_need_buy=3)
Pillager_lv4 = Item("Pillager_lv4")
PreciseDamage12_Every1s_Plus1_lv6 = Item("PreciseDamage12_Every1s_Plus1_lv6")
PreciseDamage12_Speed12_lv2 = Item("PreciseDamage12_Speed12_lv2")
PreciseDamage16_Strike16_lv3 = Item("PreciseDamage16_Strike16_lv3")
Random_10_28_Evasion_lv4 = Item("Random_10_28_Evasion_lv4", number_need_buy=1)
Random_10_28_HealthRegen_lv3 = Item("Random_10_28_HealthRegen_lv3")
Random_16_36_Defense_lv4 = Item("Random_16_36_Defense_lv4")
Range15_Invest55_lv5 = Item("Range15_Invest55_lv5",number_need_buy = 1)
Range16_Def16_lv5 = Item("Range16_Def16_lv5", number_need_buy=0)
Range24_ExtraDamage14_lv6 = Item("Range24_ExtraDamage14_lv6",number_need_buy = 0)
RevivalCount1_CriticalRate5_lv3 = Item("RevivalCount1_CriticalRate5_lv3")
RevivalCount1_Health5_lv4 = Item("RevivalCount1_Health5_lv4")
Set_Defense8_lv2 = Item("Set_Defense8_lv2", number_need_buy=1)
Set_Defense188_lv3 = Item("Set_Defense188_lv3", number_need_buy=1)
Set_ExtraDamage17_lv4 = Item("Set_ExtraDamage17_lv4", number_need_buy=1)
Set_Investment108_lv2 = Item("Set_Investment108_lv2", number_need_buy=1)
Set_Speed_lv1 = Item("Set_Speed_lv1", number_need_buy=1)
Set_Speed22_lv2 = Item("Set_Speed22_lv2", number_need_buy=1)
ShopDiscount_lv1 = Item("ShopDiscount_lv1")
ShopPlus1_lv4 = Item("ShopPlus1_lv4", number_need_buy=1)
SoulCrystalsPlus35EveryMango_lv3 = Item("SoulCrystalsPlus35EveryMango_lv3", number_need_buy=1)
SplitTheVoid_lv2 = Item("SplitTheVoid_lv2")
TomeOfKnowledge_lv3 = Item("TomeOfKnowledge_lv3")


def buy_all_previous_item():
    if global_event.check_event():
        return False
    global previous_item
    if previous_item:
        logger.debug("Ban dang mua item")
        for key, value in list(previous_item.items()):
            pydirectinput.click(key[0], key[1])
            if Button.check_money():
                logger.info(f"Ban da mua thanh cong 1 cai {value.name}")
                value.number += 1
                cgv.count_of_buy += 1
                del previous_item[key]
                pydirectinput.moveTo(222, 213)
            else:
                look_region = (key[0], key[1], 267, 312)
                cgv.set_money(False)
                if Button.click_lock(value.name, look_region) is True:
                    # del previous_item[key]
                    logger.debug("Khong du tien, Khoa item")

                else:
                    del previous_item[key]

                # return False
    else:
        logger.debug("Khong co item khoa o round truoc")


def buy_all_set_item(round_number):
    if global_event.check_event():
        return False
    logger.debug("Ban dang mua set item")
    if round_number > 3:
        PickupRange100_lv1.buy()
        Set_Speed_lv1.buy()
        Set_Defense8_lv2.buy()
        Set_Investment108_lv2.buy()
        Set_Defense188_lv3.buy()
        Set_ExtraDamage17_lv4.buy()
        Attack10EveryBuyPlus5_lv2.buy()
        SplitTheVoid_lv2.buy()
    if round_number < 18:
        Attack12_Kill1000_Unique_lv2.buy()
        Cooldown16_Kill1000_Unique_lv2.buy()
        Critical16_Kill1000_Unique_lv2.buy()
        ExtraDamage14_Kill1000_Unique_lv2.buy()
        ExtraDamage40_Kill100_Unique_lv5.buy()
        Critical40_Kill1000_Unique_lv5.buy()
        Attack35_Kill1000_Unique_lv5.buy()


def buy_all_item_investments(round_number):
    if global_event.check_event():
        return False
    logger.debug("Ban dang mua item investments")
    if round_number <= 9:
        Investment88_For_Precise_lv1.buy()
    if 3 <= round_number <= 13:
        Investment138_Defense3_lv2.buy()
    if 6 <= round_number <= 15:
        Investment198_Speed7_lv3.buy()
        Investment218_Evasion8_lv3.buy()
        Investment368_HitRecovery18_lv5.buy()


def buy_all_item_lv1():
    if global_event.check_event():
        return
    logger.debug("Ban dang mua item lv1")

    ShopDiscount_lv1.buy()
    Evasion8_Speed5_lv1.buy()
    Exp20_Range5_lv1.buy()
    Evasion6_For_Precise_lv1.buy()
    HealthRegen10_For_Precise_lv1.buy()


def buy_all_item_lv2():
    if global_event.check_event():
        return
    logger.debug("Ban dang mua item lv2")
    PreciseDamage12_Speed12_lv2.buy()
    Exp40_Luck6_lv2.buy()
    Exp45_Attack4_lv2.buy()
    Locomotive_lv2.buy()
    Luck32ForPrecise_lv2.buy()
    SplitTheVoid_lv2.buy()
    MasterChefHat_lv2.buy()
    ExtraDamage13_For_Precise_lv2.buy()
    Defense20_Speed10_lv2.buy()
    Evasion12_Strike6_lv2.buy()
    Evasion13_Health13_lv2.buy()
    HealthRegen18_Mango50_lv2.buy()
    HealthRegen20_Strike20_lv2.buy()
    HealthRegen12_HitRecovery15_lv2.buy()


def buy_all_item_lv3():
    if global_event.check_event():
        return
    logger.debug("Ban dang mua item lv3")
    # buy_item_info(Investment198_Speed7_lv3)
    # buy_item_info(Investment218_Evasion8_lv3)
    Critical20_Defense_lv3.buy()
    Immunity6_lv3.buy()
    ExtraDamage10_lv3.buy()
    PreciseDamage16_Strike16_lv3.buy()
    TomeOfKnowledge_lv3.buy()
    Attack16_Arcane16_lv3.buy()
    Attack16_Strike16_lv3.buy()
    MultishotDamage20_lv3.buy()
    Random_10_28_HealthRegen_lv3.buy()
    Health48_For_Precise_lv3.buy()
    Bicycle_lv3.buy()
    Critical9_Luck_lv3.buy()
    Evasion16_Investment16_lv3.buy()
    Luck45_HitRecovery25_lv3.buy()
    Critical21_For_Precise_lv3.buy()
    RevivalCount1_CriticalRate5_lv3.buy()


def buy_all_item_lv4():
    if global_event.check_event():
        return
    logger.debug("Ban dang mua item lv4")
    Pillager_lv4.buy()
    ImmunityCount4_lv4.buy()
    Minazuki_lv4.buy()
    Luck60_Speed25_lv4.buy()
    Luck54_Arcane27_lv4.buy()
    Health30_Speed20_lv4.buy()
    Evasion21_Attack5_lv4.buy()
    Holding_Plus_Def32_lv4.buy()
    Random_10_28_Evasion_lv4.buy()
    Random_16_36_Defense_lv4.buy()
    Holding_Plus_Cooldown35_lv4.buy()
    Holding_Plus_HealthRegen30_lv4.buy()
    RevivalCount1_Health5_lv4.buy()


def buy_all_item_lv5():
    if global_event.check_event():
        return
    logger.debug("Ban dang mua item lv5")
    Immunity10_lv5.buy()
    Immunity_Unique_lv5.buy()
    Health88_lv5.buy()
    # buy_item_info(Range16_Def16_lv5, 1)
    Range15_Invest55_lv5.buy()
    Critical30_Defense10_lv5.buy()
    ExtraDamage30_Luck30_lv5.buy()
    HealthRegen45_Invest99_lv5.buy()
    Cooldown21_lv5.buy()


def buy_all_item_lv6():

    if global_event.check_event():
        return
    logger.info("Ban dang mua item lv6")
    PantyMask_lv6.buy()
    ExtraDamage30_lv6.buy()
    Cooldown45_Speed15_lv6.buy()
    # buy_item_info(Range24_ExtraDamage14_lv6, 1)
    PreciseDamage12_Every1s_Plus1_lv6.buy()
    EnemyCount10_lv6.buy()


def buy_all_item(round_number):
    if global_event.check_event():
        return False
    logger.info(f"Ban dang mua item round {round_number}")
    if cgv.check_money() is False:
        logger.debug("Khong du tien, next round")
        return False
    # if round_number == 2:
    #     buy_all_item_round2()
    # if round_number == 3:
    #     buy_all_item_round3()
    t1 = threading.Thread(target=buy_all_item_lv1, args=())
    t2 = threading.Thread(target=buy_all_item_lv2, args=())
    t3 = threading.Thread(target=buy_all_item_lv3, args=())
    t4 = threading.Thread(target=buy_all_item_lv4, args=())
    t5 = threading.Thread(target=buy_all_item_lv5, args=())
    t6 = threading.Thread(target=buy_all_item_lv6, args=())

    if 3 < round_number <= 6:
        t1.start()

        t2.start()
        t1.join()
        t2.join()

        # buy_all_item_lv1()

    elif round_number <= 9:

        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()  # buy_all_item_lv1()  # buy_all_item_lv2()  # buy_all_item_lv3()
    elif round_number <= 12:

        t2.start()
        t3.start()
        t4.start()
        t2.join()
        t3.join()
        t4.join()

        # buy_all_item_lv2()  # buy_all_item_lv3()  # buy_all_item_lv4()
    elif round_number <= 15:

        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t2.join()
        t3.join()
        t4.join()
        t5.join()  # buy_all_item_lv2()  # buy_all_item_lv3()  # buy_all_item_lv4()  # buy_all_item_lv5()
    elif round_number <= 20:

        t3.start()
        t4.start()
        t5.start()
        t6.start()

        t3.join()
        t4.join()
        t5.join()
        t6.join()
    buy_all_previous_item()  # buy_all_item_lv3()  # buy_all_item_lv4()  # buy_all_item_lv5()  # buy_all_item_lv6()


def reset_item():
    # global Attack10EveryBuyPlus5_lv2, Attack12_Kill1000_Unique_lv2, Attack16_Arcane16_lv3, Attack16_Arcane16_lv3,
    # Attack35_Kill1000_Unique_lv5, Bicycle_lv3, Cooldown16_Kill1000_Unique_lv2
    # global Cooldown45_Speed15_lv6, Critical16_Kill1000_Unique_lv2, Critical20_Defense_lv3,
    # Critical21_For_Precise_lv3, Critical30_Defense10_lv5, Critical40_Kill1000_Unique_lv5, Defense20_Speed10_lv2,
    # EnemyCount10_lv6, Evasion6_For_Precise_lv1, Evasion8_Speed5_lv1, Evasion12_Strike6_lv2
    # global Evasion13_Health13_lv2, Evasion16_Investment16_lv3, Evasion21_Attack5_lv4, ExtraDamage10_lv3,
    # ExtraDamage13_For_Precise_lv2, ExtraDamage14_Kill1000_Unique_lv2
    # global ExtraDamage30_Luck30_lv5, Evasion21_Attack5_lv4, Exp20_Range5_lv1, Exp40_Luck6_lv2, Exp45_Attack4_lv2
    # global ExtraDamage30_lv6, ExtraDamage40_Kill100_Unique_lv5
    # global Health30_Speed20_lv4, Health48_For_Precise_lv3, Health88_lv5, HealthRegen10_For_Precise_lv1
    # global HealthRegen12_HitRecovery15_lv2, HealthRegen12_HitRecovery15_lv2
    # global HealthRegen18_Mango50_lv2, HealthRegen20_Strike20_lv2, HealthRegen45_Invest99_lv5,
    # Holding_Plus_Cooldown35_lv4
    # global Holding_Plus_Def32_lv4, Holding_Plus_HealthRegen30_lv4, Immunity_Unique_lv5, Immunity6_lv3,
    # Immunity10_lv5, ImmunityCount4_lv4
    # global Investment88_For_Precise_lv1, Investment138_Defense3_lv2, Investment198_Speed7_lv3
    # global Investment218_Evasion8_lv3, Investment368_HitRecovery18_lv5, Locomotive_lv2, Luck13_lv1,
    # Luck32ForPrecise_lv2, Luck45_HitRecovery25_lv3
    # global Luck54_Arcane27_lv4, Luck60_Speed25_lv4
    # global MasterChefHat_lv2, Minazuki_lv4, MultishotDamage20_lv3, PantyMask_lv6, PickupRange100_lv1, Pillager_lv4
    # global PreciseDamage12_Every1s_Plus1_lv6, PreciseDamage12_Speed12_lv2, PreciseDamage16_Strike16_lv3,
    # Random_10_28_Evasion_lv4, Random_10_28_HealthRegen_lv3
    # global Random_16_36_Defense_lv4, Range15_Invest55_lv5, Range16_Def16_lv5, Range24_ExtraDamage14_lv6,
    # RevivalCount1_CriticalRate5_lv3, RevivalCount1_Health5_lv4
    # global Set_Defense8_lv2, Set_Defense188_lv3, Set_ExtraDamage17_lv4, Set_Investment108_lv2, ShopDiscount_lv1,
    # SplitTheVoid_lv2, TomeOfKnowledge_lv3
    if global_event.check_event():
        return False
    Attack10EveryBuyPlus5_lv2.reset_item_number()
    Attack12_Kill1000_Unique_lv2.reset_item_number()
    Attack16_Arcane16_lv3.reset_item_number()
    Attack16_Strike16_lv3.reset_item_number()
    Attack35_Kill1000_Unique_lv5.reset_item_number()
    Bicycle_lv3.reset_item_number()
    Cooldown16_Kill1000_Unique_lv2.reset_item_number()
    Cooldown21_lv5.reset_item_number()
    Cooldown45_Speed15_lv6.reset_item_number()
    Critical9_Luck_lv3.reset_item_number()
    Critical16_Kill1000_Unique_lv2.reset_item_number()
    Critical20_Defense_lv3.reset_item_number()
    Critical21_For_Precise_lv3.reset_item_number()
    Critical30_Defense10_lv5.reset_item_number()
    Critical40_Kill1000_Unique_lv5.reset_item_number()
    Defense20_Speed10_lv2.reset_item_number()
    EnemyCount10_lv6.reset_item_number()
    Evasion6_For_Precise_lv1.reset_item_number()
    Evasion8_Speed5_lv1.reset_item_number()
    Evasion13_Health13_lv2.reset_item_number()
    Evasion13_Health13_lv2.reset_item_number()
    Evasion16_Investment16_lv3.reset_item_number()
    Evasion21_Attack5_lv4.reset_item_number()
    Exp20_Range5_lv1.reset_item_number()
    Exp40_Luck6_lv2.reset_item_number()
    Exp45_Attack4_lv2.reset_item_number()
    ExtraDamage10_lv3.reset_item_number()
    ExtraDamage13_For_Precise_lv2.reset_item_number()
    ExtraDamage14_Kill1000_Unique_lv2.reset_item_number()
    Random_10_28_HealthRegen_lv3.reset_item_number()
    ExtraDamage30_Luck30_lv5.reset_item_number()
    ExtraDamage30_lv6.reset_item_number()
    ExtraDamage40_Kill100_Unique_lv5.reset_item_number()
    Health30_Speed20_lv4.reset_item_number()
    Health48_For_Precise_lv3.reset_item_number()
    Health88_lv5.reset_item_number()
    HealthRegen10_For_Precise_lv1.reset_item_number()
    HealthRegen12_HitRecovery15_lv2.reset_item_number()
    HealthRegen18_Mango50_lv2.reset_item_number()
    HealthRegen20_Strike20_lv2.reset_item_number()
    HealthRegen45_Invest99_lv5.reset_item_number()
    Holding_Plus_Cooldown35_lv4.reset_item_number()
    Holding_Plus_Def32_lv4.reset_item_number()
    Holding_Plus_HealthRegen30_lv4.reset_item_number()
    Immunity_Unique_lv5.reset_item_number()
    Immunity6_lv3.reset_item_number()
    Immunity10_lv5.reset_item_number()
    ImmunityCount4_lv4.reset_item_number()
    Investment88_For_Precise_lv1.reset_item_number()
    Investment138_Defense3_lv2.reset_item_number()
    Investment198_Speed7_lv3.reset_item_number()
    Investment218_Evasion8_lv3.reset_item_number()
    Investment368_HitRecovery18_lv5.reset_item_number()
    Locomotive_lv2.reset_item_number()
    Luck13_lv1.reset_item_number()
    Luck32ForPrecise_lv2.reset_item_number()
    Luck45_HitRecovery25_lv3.reset_item_number()
    Luck54_Arcane27_lv4.reset_item_number()
    Luck60_Speed25_lv4.reset_item_number()
    MasterChefHat_lv2.reset_item_number()
    Minazuki_lv4.reset_item_number()
    MultishotDamage20_lv3.reset_item_number()
    PantyMask_lv6.reset_item_number()
    PickupRange100_lv1.reset_item_number()
    Pillager_lv4.reset_item_number()
    PreciseDamage12_Every1s_Plus1_lv6.reset_item_number()
    PreciseDamage12_Speed12_lv2.reset_item_number()
    PreciseDamage16_Strike16_lv3.reset_item_number()
    Random_10_28_Evasion_lv4.reset_item_number()
    Random_10_28_HealthRegen_lv3.reset_item_number()
    Random_16_36_Defense_lv4.reset_item_number()
    Range15_Invest55_lv5.reset_item_number()
    Range16_Def16_lv5.reset_item_number()
    Range24_ExtraDamage14_lv6.reset_item_number()
    RevivalCount1_CriticalRate5_lv3.reset_item_number()
    RevivalCount1_Health5_lv4.reset_item_number()
    Set_Defense8_lv2.reset_item_number()
    Set_Defense188_lv3.reset_item_number()
    Set_ExtraDamage17_lv4.reset_item_number()
    Set_Investment108_lv2.reset_item_number()
    Set_Speed22_lv2.reset_item_number()
    Set_Speed_lv1.reset_item_number()
    ShopDiscount_lv1.reset_item_number()
    ShopPlus1_lv4.reset_item_number()
    SoulCrystalsPlus35EveryMango_lv3.reset_item_number()
    SplitTheVoid_lv2.reset_item_number()
    TomeOfKnowledge_lv3.reset_item_number()


def reset_previous_item():
    global previous_item
    previous_item.clear()


if __name__ == "__main__":
    time.sleep(3)
    buy_all_item(4)
