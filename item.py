import pyautogui
import time
from controller.filelog import logger
import pydirectinput
import os
import sys
import threading
import controller.global_variables as cgv
from controller.button import Button


event = cgv.Event()
event_stop = cgv.event_stop
event_pause = cgv.event_pause


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


path_data = "data"
path_image = "image"
path_item = "item"

count_buy_item = 0
item_status_money = True
previous_item = dict()
REGION_BUY_ITEM = (394, 321, 1384, 692)
CONFIDENCE_BUY_ITEM = 0.8
GRAYSCALE_BUY_ITEM = True


def reset_previous_item():
    global previous_item
    previous_item.clear()


class ItemInfo:
    name = None
    img = None
    number = 0

    def __init__(self, para_name, para_item_number=0):
        self.name = para_name
        # self.img = "data\\image\\item\\" + para_name + ".png"
        self.img = self.get_item_img(para_name)
        self.number = para_item_number

    def reset_item_number(self):
        self.number = 0

    def get_item_img(self, para_name):
        # global HERO_IMG
        if self.img is None:
            file_name = para_name + ".png"
            relative_path = os.path.join(path_data, path_image, path_item, file_name)
            self.img = resource_path(relative_path)
        return self.img


def reset_count_buy_item():
    global count_buy_item
    count_buy_item = 0


def get_count_buy_item():
    global count_buy_item
    return count_buy_item


def reset_status_money():
    global item_status_money
    item_status_money = True


def buy_item_info(
        ItemInfo, number_item=3, stop_event=event_stop, pause_event=event_pause
):
    # logger.info("Ban dang tim item {}".format(ItemInfo.name))
    if event.check_event():
        return False
    global count_buy_item, item_status_money, previous_item, REGION_BUY_ITEM, CONFIDENCE_BUY_ITEM, GRAYSCALE_BUY_ITEM
    number = ItemInfo.number
    number_buy = number_item - number
    if number_buy > 0:
        try:
            location = pyautogui.locateCenterOnScreen(
                ItemInfo.img,
                confidence=CONFIDENCE_BUY_ITEM,
                region=REGION_BUY_ITEM,
                grayscale=GRAYSCALE_BUY_ITEM,
            )
            pydirectinput.click(location[0], location[1])
            pydirectinput.moveTo(222, 213)
            if Button.check_money() is False:
                LOOK_REGION = (location.x, location.y, 267, 312)
                cgv.set_money(False)
                if Button.click_lock(ItemInfo.name, LOOK_REGION) is True:
                    previous_item[location] = ItemInfo
                return False
            else:
                number = number + 1
                number_buy = number_item - number
                logger.info(f"Ban da mua thanh cong 1 cai {ItemInfo.name}")
                ItemInfo.number = number
                count_buy_item = count_buy_item + 1
                cgv.add_count_of_buy(1)
                return True
        except pyautogui.ImageNotFoundException:
            return False
        except Exception as e:
            logger.error(e)
            return False
    else:
        pass
        # logger.debug(
        #     f"Ban da co {ItemInfo.number} item {ItemInfo.name} , du so luong roi"
        # )


Attack10EveryBuyPlus5_lv2 = ItemInfo("Attack10EveryBuyPlus5_lv2")
Attack12_Kill1000_Unique_lv2 = ItemInfo("Attack12_Kill1000_Unique_lv2")
Attack16_Arcane16_lv3 = ItemInfo("Attack16_Arcane16_lv3")
Attack16_Strike16_lv3 = ItemInfo("Attack16_Strike16_lv3")
Attack35_Kill1000_Unique_lv5 = ItemInfo("Attack35_Kill1000_Unique_lv5")
Bicycle_lv3 = ItemInfo("Bicycle_lv3")
Cooldown16_Kill1000_Unique_lv2 = ItemInfo("Cooldown16_Kill1000_Unique_lv2")
Cooldown21_lv5 = ItemInfo("Cooldown21_lv5")
Cooldown45_Speed15_lv6 = ItemInfo("Cooldown45_Speed15_lv6")
Critical9_Luck_lv3 = ItemInfo("Critical9_Luck_lv3")
Critical16_Kill1000_Unique_lv2 = ItemInfo("Critical16_Kill1000_Unique_lv2")
Critical20_Defense_lv3 = ItemInfo("Critical20_Defense_lv3")
Critical30_Defense10_lv5 = ItemInfo("Critical30_Defense10_lv5")
Critical40_Kill1000_Unique_lv5 = ItemInfo("Critical40_Kill1000_Unique_lv5")
Defense20_Speed10_lv2 = ItemInfo("Defense20_Speed10_lv2")
Critical21_For_Precise_lv3 = ItemInfo("Critical21_For_Precise_lv3")
EnemyCount10_lv6 = ItemInfo("EnemyCount10_lv6")
Evasion6_For_Precise_lv1 = ItemInfo("Evasion6_For_Precise_lv1")
Evasion8_Speed5_lv1 = ItemInfo("Evasion8_Speed5_lv1")
Evasion12_Strike6_lv2 = ItemInfo("Evasion12_Strike6_lv2")
Evasion13_Health13_lv2 = ItemInfo("Evasion13_Health13_lv2")
Evasion16_Investment16_lv3 = ItemInfo("Evasion16_Investment16_lv3")
Evasion21_Attack5_lv4 = ItemInfo("Evasion21_Attack5_lv4")
# Evasion6_For_Precise_lv1 = ItemInfo("Evasion6_For_Precise_lv1")
Exp20_Range5_lv1 = ItemInfo("Exp20_Range5_lv1")
Exp40_Luck6_lv2 = ItemInfo("Exp40_Luck6_lv2")
Exp45_Attack4_lv2 = ItemInfo("Exp45_Attack4_lv2")
ExtraDamage10_lv3 = ItemInfo("ExtraDamage10_lv3")
ExtraDamage13_For_Precise_lv2 = ItemInfo("ExtraDamage13_For_Precise_lv2")
ExtraDamage14_Kill1000_Unique_lv2 = ItemInfo("ExtraDamage14_Kill1000_Unique_lv2")
ExtraDamage30_Luck30_lv5 = ItemInfo("ExtraDamage30_Luck30_lv5")
ExtraDamage30_lv6 = ItemInfo("ExtraDamage30_lv6")
ExtraDamage40_Kill100_Unique_lv5 = ItemInfo("ExtraDamage40_Kill100_Unique_lv5")
Health30_Speed20_lv4 = ItemInfo("Health30_Speed20_lv4")
Health48_For_Precise_lv3 = ItemInfo("Health48_For_Precise_lv3")
Health88_lv5 = ItemInfo("Health88_lv5")
HealthRegen10_For_Precise_lv1 = ItemInfo("HealthRegen10_For_Precise_lv1")
HealthRegen12_HitRecovery15_lv2 = ItemInfo("HealthRegen12_HitRecovery15_lv2")
HealthRegen18_Mango50_lv2 = ItemInfo("HealthRegen18_Mango50_lv2")
HealthRegen20_Strike20_lv2 = ItemInfo("HealthRegen20_Strike20_lv2")
HealthRegen45_Invest99_lv5 = ItemInfo("HealthRegen45_Invest99_lv5")
Holding_Plus_Cooldown35_lv4 = ItemInfo("Holding_Plus_Cooldown35_lv4")
Holding_Plus_Def32_lv4 = ItemInfo("Holding_Plus_Def32_lv4")
Holding_Plus_HealthRegen30_lv4 = ItemInfo("Holding_Plus_HealthRegen30_lv4")
Immunity_Unique_lv5 = ItemInfo("Immunity_Unique_lv5")
Immunity6_lv3 = ItemInfo("Immunity6_lv3")
Immunity10_lv5 = ItemInfo("Immunity10_lv5")
ImmunityCount4_lv4 = ItemInfo("ImmunityCount4_lv4")
Investment88_For_Precise_lv1 = ItemInfo("Investment88_For_Precise_lv1")
Investment138_Defense3_lv2 = ItemInfo("Investment138_Defense3_lv2")
Investment198_Speed7_lv3 = ItemInfo("Investment198_Speed7_lv3")
Investment218_Evasion8_lv3 = ItemInfo("Investment218_Evasion8_lv3")
Investment368_HitRecovery18_lv5 = ItemInfo("Investment368_HitRecovery18_lv5")
Locomotive_lv2 = ItemInfo("Locomotive_lv2")
Luck13_lv1 = ItemInfo("Luck13_lv1")
Luck32ForPrecise_lv2 = ItemInfo("Luck32ForPrecise_lv2")
Luck45_HitRecovery25_lv3 = ItemInfo("Luck45_HitRecovery25_lv3")
Luck54_Arcane27_lv4 = ItemInfo("Luck54_Arcane27_lv4")
Luck60_Speed25_lv4 = ItemInfo("Luck60_Speed25_lv4")
MasterChefHat_lv2 = ItemInfo("MasterChefHat_lv2")
Minazuki_lv4 = ItemInfo("Minazuki_lv4")
MultishotDamage20_lv3 = ItemInfo("MultishotDamage20_lv3")
PantyMask_lv6 = ItemInfo("PantyMask_lv6")
PickupRange100_lv1 = ItemInfo("PickupRange100_lv1")
Pillager_lv4 = ItemInfo("Pillager_lv4")
PreciseDamage12_Every1s_Plus1_lv6 = ItemInfo("PreciseDamage12_Every1s_Plus1_lv6")
PreciseDamage12_Speed12_lv2 = ItemInfo("PreciseDamage12_Speed12_lv2")
PreciseDamage16_Strike16_lv3 = ItemInfo("PreciseDamage16_Strike16_lv3")
Random_10_28_Evasion_lv4 = ItemInfo("Random_10_28_Evasion_lv4")
Random_10_28_HealthRegen_lv3 = ItemInfo("Random_10_28_HealthRegen_lv3")
Random_16_36_Defense_lv4 = ItemInfo("Random_16_36_Defense_lv4")
Range15_Invest55_lv5 = ItemInfo("Range15_Invest55_lv5")
Range16_Def16_lv5 = ItemInfo("Range16_Def16_lv5")
Range24_ExtraDamage14_lv6 = ItemInfo("Range24_ExtraDamage14_lv6")
RevivalCount1_CriticalRate5_lv3 = ItemInfo("RevivalCount1_CriticalRate5_lv3")
RevivalCount1_Health5_lv4 = ItemInfo("RevivalCount1_Health5_lv4")
Set_Defense8_lv2 = ItemInfo("Set_Defense8_lv2")
Set_Defense188_lv3 = ItemInfo("Set_Defense188_lv3")
Set_ExtraDamage17_lv4 = ItemInfo("Set_ExtraDamage17_lv4")
Set_Investment108_lv2 = ItemInfo("Set_Investment108_lv2")
Set_Speed_lv1 = ItemInfo("Set_Speed_lv1")
# PantyMask_lv6 = ItemInfo("PantyMask_lv6")
ShopDiscount_lv1 = ItemInfo("ShopDiscount_lv1")
SplitTheVoid_lv2 = ItemInfo("SplitTheVoid_lv2")
TomeOfKnowledge_lv3 = ItemInfo("TomeOfKnowledge_lv3", 1)


def buy_all_previous_item():
    if event.check_event():
        return False
    global previous_item, count_buy_item
    if previous_item:
        logger.debug("Ban dang mua item khoa o round truoc")
        for key, value in list(previous_item.items()):
            pydirectinput.click(key[0], key[1])
            if Button.check_money() is False:
                return False
            else:
                logger.info(f"Ban da mua thanh cong 1 cai {value.name}")
                value.number = value.number + 1
                count_buy_item = count_buy_item + 1
                del previous_item[key]
    else:
        logger.debug("Khong co item khoa o round truoc")


def buy_all_set_item(round_number):
    if event.check_event():
        return False
    logger.debug("Ban dang mua set item")
    buy_item_info(PickupRange100_lv1, 1)
    buy_item_info(Set_Speed_lv1, 1)
    buy_item_info(Set_Defense8_lv2, 1)
    buy_item_info(Set_Investment108_lv2, 1)
    buy_item_info(Set_Defense188_lv3, 1)
    buy_item_info(Set_ExtraDamage17_lv4, 1)
    buy_item_info(Attack10EveryBuyPlus5_lv2, 5)
    if round_number < 18:
        buy_item_info(Attack12_Kill1000_Unique_lv2, 1)
        buy_item_info(Cooldown16_Kill1000_Unique_lv2, 1)
        buy_item_info(Critical16_Kill1000_Unique_lv2, 1)
        buy_item_info(ExtraDamage14_Kill1000_Unique_lv2, 1)
        buy_item_info(ExtraDamage40_Kill100_Unique_lv5, 1)
        buy_item_info(Critical40_Kill1000_Unique_lv5, 1)
        buy_item_info(Attack35_Kill1000_Unique_lv5, 1)


def buy_all_item_investments(round_number):
    if event.check_event():
        return False
    logger.debug("Ban dang mua item investments")
    if round_number <= 9:
        buy_item_info(Investment88_For_Precise_lv1, 5)
    if 3 <= round_number <= 13:
        buy_item_info(Investment138_Defense3_lv2, 5)
    if 6 <= round_number <= 15:
        buy_item_info(Investment198_Speed7_lv3, 3)
        buy_item_info(Investment218_Evasion8_lv3, 1)
        buy_item_info(Investment368_HitRecovery18_lv5, 1)


def buy_all_item_round2():
    buy_item_info(ShopDiscount_lv1)


def buy_all_item_round3():
    buy_item_info(ShopDiscount_lv1)
    buy_item_info(PickupRange100_lv1)


def buy_all_item_lv1():
    if event.check_event():
        return
    logger.debug("Ban dang mua item lv1")

    buy_item_info(ShopDiscount_lv1, 5)
    buy_item_info(Evasion8_Speed5_lv1)
    buy_item_info(Exp20_Range5_lv1)
    buy_item_info(Evasion6_For_Precise_lv1)
    buy_item_info(HealthRegen10_For_Precise_lv1)


def buy_all_item_lv2():
    if event.check_event():
        return
    logger.debug("Ban dang mua item lv2")
    buy_item_info(PreciseDamage12_Speed12_lv2)
    buy_item_info(Exp40_Luck6_lv2)
    buy_item_info(Exp45_Attack4_lv2)
    buy_item_info(Locomotive_lv2)
    buy_item_info(Luck32ForPrecise_lv2)
    buy_item_info(SplitTheVoid_lv2)
    buy_item_info(MasterChefHat_lv2)

    buy_item_info(ExtraDamage13_For_Precise_lv2)
    buy_item_info(Defense20_Speed10_lv2)
    buy_item_info(Evasion12_Strike6_lv2)
    buy_item_info(Evasion13_Health13_lv2)
    buy_item_info(HealthRegen18_Mango50_lv2)
    buy_item_info(HealthRegen20_Strike20_lv2)
    buy_item_info(HealthRegen12_HitRecovery15_lv2)


def buy_all_item_lv3():
    if event.check_event():
        return
    logger.debug("Ban dang mua item lv3")
    # buy_item_info(Investment198_Speed7_lv3)
    # buy_item_info(Investment218_Evasion8_lv3)
    buy_item_info(Critical20_Defense_lv3)
    buy_item_info(Immunity6_lv3)
    buy_item_info(ExtraDamage10_lv3, 2)
    buy_item_info(PreciseDamage16_Strike16_lv3)
    buy_item_info(TomeOfKnowledge_lv3)
    buy_item_info(Attack16_Arcane16_lv3)
    buy_item_info(Attack16_Strike16_lv3)
    buy_item_info(MultishotDamage20_lv3)
    buy_item_info(Random_10_28_HealthRegen_lv3)
    buy_item_info(Health48_For_Precise_lv3, 1)
    buy_item_info(Bicycle_lv3, 1)
    buy_item_info(Critical9_Luck_lv3)
    buy_item_info(Evasion16_Investment16_lv3)
    buy_item_info(Luck45_HitRecovery25_lv3, 1)
    buy_item_info(Critical21_For_Precise_lv3, 1)
    buy_item_info(RevivalCount1_CriticalRate5_lv3)


def buy_all_item_lv4():
    if event.check_event():
        return
    logger.debug("Ban dang mua item lv4")
    buy_item_info(Pillager_lv4)
    buy_item_info(ImmunityCount4_lv4, 2)
    buy_item_info(Minazuki_lv4)
    buy_item_info(Luck60_Speed25_lv4, 1)
    buy_item_info(Luck54_Arcane27_lv4, 1)
    buy_item_info(Health30_Speed20_lv4)
    buy_item_info(Evasion21_Attack5_lv4)
    buy_item_info(Holding_Plus_Def32_lv4, 1)
    buy_item_info(Random_10_28_Evasion_lv4, 1)
    buy_item_info(Random_16_36_Defense_lv4, 1)
    buy_item_info(Holding_Plus_Cooldown35_lv4)
    buy_item_info(Holding_Plus_HealthRegen30_lv4)
    buy_item_info(RevivalCount1_Health5_lv4)


def buy_all_item_lv5():
    if event.check_event():
        return
    logger.debug("Ban dang mua item lv5")
    buy_item_info(Immunity10_lv5)
    buy_item_info(Immunity_Unique_lv5, 1)
    buy_item_info(Health88_lv5, 1)
    # buy_item_info(Range16_Def16_lv5, 1)
    buy_item_info(Range15_Invest55_lv5, 1)
    buy_item_info(Critical30_Defense10_lv5, 2)
    buy_item_info(ExtraDamage30_Luck30_lv5, 1)
    buy_item_info(HealthRegen45_Invest99_lv5, 1)
    buy_item_info(Cooldown21_lv5, 2)


def buy_all_item_lv6():
    """
    Buys all level 6 items.

    This function purchases all the level 6 items required for the game.
    It logs a debug message and calls the `buy_item_info` function to buy each item.

    Args:
        None

    Returns:
        None
    """
    if event.check_event():
        return
    logger.info("Ban dang mua item lv6")
    buy_item_info(PantyMask_lv6, 1)
    buy_item_info(ExtraDamage30_lv6, 1)
    buy_item_info(Cooldown45_Speed15_lv6, 1)
    # buy_item_info(Range24_ExtraDamage14_lv6, 1)
    buy_item_info(PreciseDamage12_Every1s_Plus1_lv6, 1)
    buy_item_info(EnemyCount10_lv6, 1)


def buy_all_item(round_number):
    if event.check_event():
        return False
    logger.info(f"Ban dang mua item round {round_number}")
    if cgv.check_money() is False:
        logger.debug("Khong du tien, next round")
        return False
    if round_number == 2:
        buy_all_item_round2()
    if round_number == 3:
        buy_all_item_round3()
    if 3 < round_number <= 6:
        buy_all_item_lv1()
        buy_all_item_lv2()
    if 6 < round_number <= 9:
        buy_all_item_lv1()
        buy_all_item_lv2()
        buy_all_item_lv3()
    if 9 < round_number <= 12:
        buy_all_item_lv2()
        buy_all_item_lv3()
        buy_all_item_lv4()
    if 12 < round_number <= 15:
        buy_all_item_lv2()
        buy_all_item_lv3()
        buy_all_item_lv4()
        buy_all_item_lv5()
    if 15 < round_number <= 20:
        buy_all_item_lv3()
        buy_all_item_lv4()
        buy_all_item_lv5()
        buy_all_item_lv6()


def test_all_item():
    buy_all_set_item()
    buy_all_item_investments(0)
    buy_all_item_lv1()
    buy_all_item_lv2()
    buy_all_item_lv3()
    buy_all_item_lv4()
    buy_all_item_lv5()
    buy_all_item_lv6()


def reset_item():
    # global Attack10EveryBuyPlus5_lv2, Attack12_Kill1000_Unique_lv2, Attack16_Arcane16_lv3, Attack16_Arcane16_lv3, Attack35_Kill1000_Unique_lv5, Bicycle_lv3, Cooldown16_Kill1000_Unique_lv2
    # global Cooldown45_Speed15_lv6, Critical16_Kill1000_Unique_lv2, Critical20_Defense_lv3, Critical21_For_Precise_lv3, Critical30_Defense10_lv5, Critical40_Kill1000_Unique_lv5, Defense20_Speed10_lv2, EnemyCount10_lv6, Evasion6_For_Precise_lv1, Evasion8_Speed5_lv1, Evasion12_Strike6_lv2
    # global Evasion13_Health13_lv2, Evasion16_Investment16_lv3, Evasion21_Attack5_lv4, ExtraDamage10_lv3, ExtraDamage13_For_Precise_lv2, ExtraDamage14_Kill1000_Unique_lv2
    # global ExtraDamage30_Luck30_lv5, Evasion21_Attack5_lv4, Exp20_Range5_lv1, Exp40_Luck6_lv2, Exp45_Attack4_lv2
    # global ExtraDamage30_lv6, ExtraDamage40_Kill100_Unique_lv5
    # global Health30_Speed20_lv4, Health48_For_Precise_lv3, Health88_lv5, HealthRegen10_For_Precise_lv1
    # global HealthRegen12_HitRecovery15_lv2, HealthRegen12_HitRecovery15_lv2
    # global HealthRegen18_Mango50_lv2, HealthRegen20_Strike20_lv2, HealthRegen45_Invest99_lv5, Holding_Plus_Cooldown35_lv4
    # global Holding_Plus_Def32_lv4, Holding_Plus_HealthRegen30_lv4, Immunity_Unique_lv5, Immunity6_lv3, Immunity10_lv5, ImmunityCount4_lv4
    # global Investment88_For_Precise_lv1, Investment138_Defense3_lv2, Investment198_Speed7_lv3
    # global Investment218_Evasion8_lv3, Investment368_HitRecovery18_lv5, Locomotive_lv2, Luck13_lv1, Luck32ForPrecise_lv2, Luck45_HitRecovery25_lv3
    # global Luck54_Arcane27_lv4, Luck60_Speed25_lv4
    # global MasterChefHat_lv2, Minazuki_lv4, MultishotDamage20_lv3, PantyMask_lv6, PickupRange100_lv1, Pillager_lv4
    # global PreciseDamage12_Every1s_Plus1_lv6, PreciseDamage12_Speed12_lv2, PreciseDamage16_Strike16_lv3, Random_10_28_Evasion_lv4, Random_10_28_HealthRegen_lv3
    # global Random_16_36_Defense_lv4, Range15_Invest55_lv5, Range16_Def16_lv5, Range24_ExtraDamage14_lv6, RevivalCount1_CriticalRate5_lv3, RevivalCount1_Health5_lv4
    # global Set_Defense8_lv2, Set_Defense188_lv3, Set_ExtraDamage17_lv4, Set_Investment108_lv2, ShopDiscount_lv1, SplitTheVoid_lv2, TomeOfKnowledge_lv3

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
    ShopDiscount_lv1.reset_item_number()
    SplitTheVoid_lv2.reset_item_number()
    TomeOfKnowledge_lv3.reset_item_number()


if __name__ == "__main__":
    # print(os.path.join(path_parent, path_data, path_image, path_item))
    # print(path_parent)
    reset_item()
    print(TomeOfKnowledge_lv3.number)
    pass
