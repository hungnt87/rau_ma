import pyautogui
import time
import button
import pyscreeze
from datetime import datetime
from log import logger
count_buy_item = 0


class ItemInfo:
    def __init__(self, para_name, para_item_number=0):
        self.name = para_name
        self.img = "data\\image\\item\\" + para_name + ".png"
        self.number = para_item_number

    def reset_item_number(self):
        self.number = 0


def reset_count_buy_item():
    global count_buy_item
    count_buy_item = 0


def get_count_buy_item():
    global count_buy_item
    return count_buy_item


def buy_item(ItemInfo):
    """
    This function is used to buy a specific item.

    Parameters:
    ItemInfo (ItemInfo object): The information of the item to buy.

    Returns:
    True if the item is bought successfully, False otherwise.
    """
    try:
        res = pyautogui.locateOnScreen(
            ItemInfo.img, confidence=0.8, region=(0, 0, 1916, 1134))
        # logger.info("xuat hien ", ItemInfo.name)
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        pyautogui.click(res_center)
        return True
    except pyautogui.ImageNotFoundException:
        return False


# def buy_item_info(ItemInfo, number_item=5):
#     """
#     This function is used to buy a specific number of a specific item.

#     Parameters:
#     ItemInfo (ItemInfo object): The information of the item to buy.
#     number_item (int): The number of items to buy.

#     Returns:
#     Nothing.
#     """
#     logger.info("Bạn đang tìm item {}".format(ItemInfo.name))
#     global count_buy_item
#     number = ItemInfo.number
#     if number_item > number:
#         number_buy = number_item - number
#         buy = buy_item(ItemInfo)
#         if buy is True:
#             if button.check_not_money():
#                 break
#             else:
#                 number = number + 1
#                 logger.info("Bạn đã mua thành công 1 cái {}, bạn cần mua thêm {} nữa".format(
#                     ItemInfo.name, number_buy - number))
#                 ItemInfo.number = number
#                 count_buy_item = count_buy_item + 1
#                 logger.info("Ban da mua item lan thu {}".format(count_buy_item))
item_status_money = True


def reset_status_money():
    global item_status_money
    item_status_money = True


def buy_item_info(ItemInfo, number_item=3):
    # logger.info("Ban dang tim item {}".format(ItemInfo.name))
    global count_buy_item, item_status_money
    number = ItemInfo.number
    if number_item > number:
        number_buy = number_item - number
        try:
            location = pyautogui.locateOnScreen(
                ItemInfo.img, confidence=0.9, region=(0, 0, 1916, 1134))
            res_center = pyautogui.center(location)
            pyautogui.moveTo(res_center)
            pyautogui.click(res_center)
            pyautogui.moveTo(222, 213)
            if button.check_not_money() is True:
                item_status_money = False
            else:
                number = number + 1
                logger.info("Ban da mua thanh cong 1 cai {}, ban can mua them {}".format(
                    ItemInfo.name, number_buy - number))
                ItemInfo.number = number
                count_buy_item = count_buy_item + 1
        except pyautogui.ImageNotFoundException:
            return False
        except TypeError:
            logger.error("Khong tim thay hinh anh {}".format(ItemInfo.name))
            return False

        # for location in locations:
        #     # res_center = pyautogui.center(location)
        #     # pyautogui.moveTo(res_center)
        #     #time.sleep(2)
        #     logger.info("Found at:", location)
            # pyautogui.moveTo(222,213)
            # #pyautogui.click(res_center)
            # if button.check_not_money():
            #     logger.info("Bạn không đủ tiền mua item này")
            #     break
            # else:
            #     number = number + 1
            #     logger.info("Bạn đã mua thành công 1 cái {}, bạn cần mua thêm {} nữa".format(
            #         ItemInfo.name, number_buy - number))
            #     ItemInfo.number = number
            #     count_buy_item = count_buy_item + 1


Attack12_Kill1000_Unique_lv2 = ItemInfo("Attack12_Kill1000_Unique_lv2")
Attack16_Arcane16_lv3 = ItemInfo("Attack16_Arcane16_lv3")
Attack16_Strike16_lv3 = ItemInfo("Attack16_Strike16_lv3")
Bicycle_lv3 = ItemInfo("Bicycle_lv3")
Cooldown16_Kill1000_Unique_lv2 = ItemInfo("Cooldown16_Kill1000_Unique_lv2")
Cooldown21_lv5 = ItemInfo("Cooldown21_lv5")
Cooldown45_Speed15_lv6 = ItemInfo("Cooldown45_Speed15_lv6")
Critical9_Luck_lv3 = ItemInfo("Critical9_Luck_lv3")
Critical16_Kill100_Unique_lv2 = ItemInfo("Critical16_Kill100_Unique_lv2")
Critical30_Defense10_lv5 = ItemInfo("Critical30_Defense10_lv5")
Defense20_Speed10_lv2 = ItemInfo("Defense20_Speed10_lv2")
EnemyCount10_lv6 = ItemInfo("EnemyCount10_lv6")
Evasion6_For_Precise_lv1 = ItemInfo("Evasion6_For_Precise_lv1")
Evasion12_Strike6_lv2 = ItemInfo("Evasion12_Strike6_lv2")
Evasion13_Health13_lv2 = ItemInfo("Evasion13_Health13_lv2")
Evasion16_Investment16_lv3 = ItemInfo("Evasion16_Investment16_lv3")
Evasion21_Attack5_lv4 = ItemInfo("Evasion21_Attack5_lv4")
Evasion6_For_Precise_lv1 = ItemInfo("Evasion6_For_Precise_lv1")
Exp20_Range5_lv1 = ItemInfo("Exp20_Range5_lv1")
Exp40_Luck6_lv2 = ItemInfo("Exp40_Luck6_lv2")
Exp45_Attack4_lv2 = ItemInfo("Exp45_Attack4_lv2")
ExtraDamage10_lv3 = ItemInfo("ExtraDamage10_lv3")
ExtraDamage13_For_Precise_lv2 = ItemInfo("ExtraDamage13_For_Precise_lv2")
ExtraDamage14_Kill1000_Unique_lv2 = ItemInfo(
    "ExtraDamage14_Kill1000_Unique_lv2")
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
NorthWind_Luck13 = ItemInfo("NorthWind_Luck13")
MultishotDamage20_lv3 = ItemInfo("MultishotDamage20_lv3")
PantyMask_lv6 = ItemInfo("PantyMask_lv6")
PickupRange100_lv1 = ItemInfo("PickupRange100_lv1")
Pillager_lv4 = ItemInfo("Pillager_lv4")
PreciseDamage12_Every1s_Plus1_lv6 = ItemInfo(
    "PreciseDamage12_Every1s_Plus1_lv6")
PreciseDamage12_Speed12_lv2 = ItemInfo("PreciseDamage12_Speed12_lv2")
PreciseDamage16_Strike16_lv3 = ItemInfo("PreciseDamage16_Strike16_lv3")
Random_10_28_Evasion_lv4 = ItemInfo("Random_10_28_Evasion_lv4")
Random_10_28_HealthRegen_lv3 = ItemInfo("Random_10_28_HealthRegen_lv3")
Random_16_36_Defense_lv4 = ItemInfo("Random_16_36_Defense_lv4")
Range15_Invest55_lv5 = ItemInfo("Range15_Invest55_lv5")
Range16_Def16_lv5 = ItemInfo("Range16_Def16_lv5")
Range24_ExtraDamage14_lv6 = ItemInfo("Range24_ExtraDamage14_lv6")
RevivalCount1_Health5_lv4 = ItemInfo("RevivalCount1_Health5_lv4")
Set_Defense8_lv2 = ItemInfo("Set_Defense8_lv2")
Set_Defense188_lv3 = ItemInfo("Set_Defense188_lv3")
Set_ExtraDamage17_lv4 = ItemInfo("Set_ExtraDamage17_lv4")
Set_Investment108_lv2 = ItemInfo("Set_Investment108_lv2")
Set_Speed_lv1 = ItemInfo("Set_Speed_lv1")
PantyMask_lv6 = ItemInfo("PantyMask_lv6")
ShopDiscount_lv1 = ItemInfo("ShopDiscount_lv1")
SplitTheVoid_lv2 = ItemInfo("SplitTheVoid_lv2")
TomeOfKnowledge_lv3 = ItemInfo("TomeOfKnowledge_lv3")


def buy_all_set_item():
    logger.debug("Ban dang mua set item")
    buy_item_info(PickupRange100_lv1, 1)
    buy_item_info(Set_Speed_lv1, 1)
    buy_item_info(Set_Defense8_lv2, 1)
    buy_item_info(Set_Investment108_lv2, 1)
    buy_item_info(Set_Defense188_lv3, 1)
    buy_item_info(Set_ExtraDamage17_lv4, 1)


def buy_all_item_investments(round_number):
    logger.debug("Ban dang mua item investments")
    if round_number <= 9:
        buy_item_info(Investment88_For_Precise_lv1, 5)
    if 3 <= round_number <= 13:
        buy_item_info(Investment138_Defense3_lv2, 5)
    if 6 <= round_number <= 15:
        buy_item_info(Investment198_Speed7_lv3, 1)
        buy_item_info(Investment218_Evasion8_lv3, 1)
        buy_item_info(Investment368_HitRecovery18_lv5, 1)
    if round_number == 0:
        buy_item_info(Investment88_For_Precise_lv1, 5)
        buy_item_info(Investment138_Defense3_lv2, 5)
        buy_item_info(Investment198_Speed7_lv3, 5)
        buy_item_info(Investment218_Evasion8_lv3, 5)


def buy_all_item_round2():
    buy_item_info(Investment88_For_Precise_lv1)
    buy_item_info(ShopDiscount_lv1)


def buy_all_item_round3():
    buy_item_info(Investment88_For_Precise_lv1)
    buy_item_info(ShopDiscount_lv1)
    buy_item_info(PickupRange100_lv1)


def buy_all_item_lv1():
    logger.debug("Ban dang mua item lv1")
    # buy_item_info(Investment88_For_Precise_lv1)
    buy_item_info(ShopDiscount_lv1)
    buy_item_info(PickupRange100_lv1, 2)
    buy_item_info(Exp20_Range5_lv1, 2)
    buy_item_info(Evasion6_For_Precise_lv1)
    buy_item_info(HealthRegen10_For_Precise_lv1, 2)


def buy_all_item_lv2():
    logger.debug("Ban dang mua item lv2")
    # buy_item_info(Investment138_Defense3_lv2)
    buy_item_info(PreciseDamage12_Speed12_lv2)
    buy_item_info(Exp40_Luck6_lv2)
    buy_item_info(Exp45_Attack4_lv2)
    buy_item_info(Locomotive_lv2)
    buy_item_info(Luck32ForPrecise_lv2)
    buy_item_info(SplitTheVoid_lv2)
    buy_item_info(MasterChefHat_lv2)
    buy_item_info(Attack12_Kill1000_Unique_lv2, 1)
    buy_item_info(Cooldown16_Kill1000_Unique_lv2, 1)
    buy_item_info(ExtraDamage14_Kill1000_Unique_lv2, 1)
    buy_item_info(Critical16_Kill100_Unique_lv2, 1)
    buy_item_info(ExtraDamage13_For_Precise_lv2)
    buy_item_info(Defense20_Speed10_lv2)
    buy_item_info(Evasion12_Strike6_lv2)
    buy_item_info(Evasion13_Health13_lv2)
    buy_item_info(HealthRegen18_Mango50_lv2)
    buy_item_info(HealthRegen20_Strike20_lv2)
    buy_item_info(HealthRegen12_HitRecovery15_lv2)


def buy_all_item_lv3():
    logger.debug("Ban dang mua item lv3")
    # buy_item_info(Investment198_Speed7_lv3)
    # buy_item_info(Investment218_Evasion8_lv3)
    buy_item_info(Immunity6_lv3)
    buy_item_info(ExtraDamage10_lv3, 2)
    buy_item_info(PreciseDamage16_Strike16_lv3)
    buy_item_info(TomeOfKnowledge_lv3)
    buy_item_info(Attack16_Arcane16_lv3)
    buy_item_info(Attack16_Strike16_lv3)
    buy_item_info(MultishotDamage20_lv3, 5)
    buy_item_info(Random_10_28_HealthRegen_lv3, 1)
    buy_item_info(Health48_For_Precise_lv3, 1)
    buy_item_info(Bicycle_lv3, 1)
    buy_item_info(Critical9_Luck_lv3, 1)
    buy_item_info(Evasion16_Investment16_lv3, 1)
    buy_item_info(Luck45_HitRecovery25_lv3, 1)


def buy_all_item_lv4():
    logger.debug("Ban dang mua item lv4")
    buy_item_info(Pillager_lv4)

    buy_item_info(ImmunityCount4_lv4, 1)
    buy_item_info(Minazuki_lv4)
    buy_item_info(Luck60_Speed25_lv4, 1)
    buy_item_info(Luck54_Arcane27_lv4, 1)
    buy_item_info(Health30_Speed20_lv4, 1)
    buy_item_info(Evasion21_Attack5_lv4, 1)
    buy_item_info(Holding_Plus_Def32_lv4, 1)
    buy_item_info(Random_10_28_Evasion_lv4, 1)
    buy_item_info(Random_16_36_Defense_lv4, 1)
    buy_item_info(Holding_Plus_Cooldown35_lv4, 1)
    buy_item_info(Holding_Plus_HealthRegen30_lv4, 1)
    buy_item_info(RevivalCount1_Health5_lv4, 1)


def buy_all_item_lv5():
    logger.debug("Ban dang mua item lv5")
    buy_item_info(Immunity10_lv5, 5)
    buy_item_info(Immunity_Unique_lv5, 5)
    buy_item_info(ExtraDamage40_Kill100_Unique_lv5, 1)
    buy_item_info(Health88_lv5, 1)
    buy_item_info(Range16_Def16_lv5, 1)
    buy_item_info(Range15_Invest55_lv5, 1)
    buy_item_info(Critical30_Defense10_lv5, 2)
    buy_item_info(ExtraDamage30_Luck30_lv5, 1)
    buy_item_info(HealthRegen45_Invest99_lv5, 1)
    buy_item_info(Cooldown21_lv5, 2)


def buy_all_item_lv6():
    logger.debug("Ban dang mua item lv6")
    buy_item_info(PantyMask_lv6, 1)
    buy_item_info(ExtraDamage30_lv6, 1)
    buy_item_info(Cooldown45_Speed15_lv6, 1)
    buy_item_info(Range24_ExtraDamage14_lv6, 1)
    buy_item_info(PreciseDamage12_Every1s_Plus1_lv6, 1)
    buy_item_info(EnemyCount10_lv6, 1)


def buy_all_item(round_number):
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
    global Attack12_Kill1000_Unique_lv2, Attack16_Arcane16_lv3, Attack16_Arcane16_lv3, Bicycle_lv3, Cooldown16_Kill1000_Unique_lv2
    global Cooldown45_Speed15_lv6, Critical16_Kill100_Unique_lv2, Critical30_Defense10_lv5, Defense20_Speed10_lv2, EnemyCount10_lv6, Evasion6_For_Precise_lv1, Evasion12_Strike6_lv2
    global Evasion13_Health13_lv2, Evasion16_Investment16_lv3, Evasion21_Attack5_lv4, ExtraDamage10_lv3, ExtraDamage13_For_Precise_lv2, ExtraDamage14_Kill1000_Unique_lv2
    global ExtraDamage30_Luck30_lv5, Evasion21_Attack5_lv4, Exp20_Range5_lv1, Exp40_Luck6_lv2, Exp45_Attack4_lv2
    global ExtraDamage30_lv6, ExtraDamage40_Kill100_Unique_lv5
    global Health30_Speed20_lv4, Health48_For_Precise_lv3, Health88_lv5, HealthRegen10_For_Precise_lv1
    global HealthRegen12_HitRecovery15_lv2, HealthRegen12_HitRecovery15_lv2
    global HealthRegen18_Mango50_lv2, HealthRegen20_Strike20_lv2, HealthRegen45_Invest99_lv5, Holding_Plus_Cooldown35_lv4
    global Holding_Plus_Def32_lv4, Holding_Plus_HealthRegen30_lv4, Immunity_Unique_lv5, Immunity6_lv3, Immunity10_lv5, ImmunityCount4_lv4
    global Investment88_For_Precise_lv1, Investment138_Defense3_lv2, Investment198_Speed7_lv3
    global Investment218_Evasion8_lv3, Investment368_HitRecovery18_lv5, Locomotive_lv2, Luck13_lv1, Luck32ForPrecise_lv2, Luck45_HitRecovery25_lv3
    global Luck54_Arcane27_lv4, Luck60_Speed25_lv4
    global MasterChefHat_lv2, Minazuki_lv4, MultishotDamage20_lv3, PantyMask_lv6, PickupRange100_lv1, Pillager_lv4
    global PreciseDamage12_Every1s_Plus1_lv6, PreciseDamage12_Speed12_lv2, PreciseDamage16_Strike16_lv3, Random_10_28_Evasion_lv4, Random_10_28_HealthRegen_lv3
    global Random_16_36_Defense_lv4, Range15_Invest55_lv5, Range16_Def16_lv5, Range24_ExtraDamage14_lv6, RevivalCount1_Health5_lv4
    global Set_Defense8_lv2, Set_Defense188_lv3, Set_ExtraDamage17_lv4, Set_Investment108_lv2, ShopDiscount_lv1, SplitTheVoid_lv2, TomeOfKnowledge_lv3

    Attack12_Kill1000_Unique_lv2.reset_item_number()
    Attack16_Arcane16_lv3.reset_item_number()
    Attack16_Strike16_lv3.reset_item_number()
    Bicycle_lv3.reset_item_number()
    Cooldown16_Kill1000_Unique_lv2.reset_item_number()
    Cooldown21_lv5.reset_item_number()
    Cooldown45_Speed15_lv6.reset_item_number()
    Critical9_Luck_lv3.reset_item_number()
    Critical16_Kill100_Unique_lv2.reset_item_number()
    Critical30_Defense10_lv5.reset_item_number()
    Defense20_Speed10_lv2.reset_item_number()
    EnemyCount10_lv6.reset_item_number()
    Evasion6_For_Precise_lv1.reset_item_number()
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
    RevivalCount1_Health5_lv4.reset_item_number()
    Set_Defense8_lv2.reset_item_number()
    Set_Defense188_lv3.reset_item_number()
    Set_ExtraDamage17_lv4.reset_item_number()
    Set_Investment108_lv2.reset_item_number()
    ShopDiscount_lv1.reset_item_number()
    SplitTheVoid_lv2.reset_item_number()
    TomeOfKnowledge_lv3.reset_item_number()
