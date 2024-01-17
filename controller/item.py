import os
import threading
import time

import pyautogui
import pydirectinput
import pyscreeze

import controller.global_variables as cgv
from controller import SelectWindow
from controller.button import Button
from controller.filelog import logger
from controller.global_variables import global_event, path, region_item

previous_item = dict()

CONFIDENCE_BUY_ITEM = 0.8
GRAYSCALE_BUY_ITEM = True


class Item:
    img = None

    def __init__(
        self,
        name,
        number_need_buy=5,
        grayscale=GRAYSCALE_BUY_ITEM,
        confidence=CONFIDENCE_BUY_ITEM,
    ):
        self.name = name
        self.number = 0
        self.number_need_buy = number_need_buy
        self.img = self.get_item_img(name)
        self.grayscale = grayscale
        self.confidence = confidence

    def reset_item_number(self):
        self.number = 0

    def get_item_img(self, name):
        file_name = name + ".png"
        if self.img == None:
            img = self.img = path.get_resource_path(
                os.path.join("assets", "img", "item", file_name)
            )
            if os.path.exists(img) is False:
                logger.error(f"Không tìm thấy file: {img} ")
                return None
            else:
                return img
        else:
            return self.img

    def buy(self):
        # logger.info("Ban dang tim item {}".format(ItemInfo.name))
        if global_event.check_event():
            return False
        if self.img == None:
            logger.error(f"Không tìm thấy hình ảnh item: {self.name}")
            return None
        count_of_buy = self.number_need_buy - self.number
        if count_of_buy > 0:
            try:
                location = pyautogui.locateCenterOnScreen(
                    self.img,
                    confidence=self.confidence,
                    region=(
                        region_item.x,
                        region_item.y,
                        region_item.width,
                        region_item.height,
                    ),
                    grayscale=self.grayscale,
                )
                previous_item[location] = self

            except pyautogui.ImageNotFoundException:
                return False
            except OSError as e:
                logger.error(f"Item buy: {e}")

        else:
            pass

    def check_item(self, confidence=0.85, grayscale=False):
        if global_event.check_event():
            return False
        if self.img == None:
            logger.error(f"Không tìm thấy hình ảnh item: {self.name}")
            return None
        distance = pow(10, 2)
        elements = []
        try:
            locations = pyautogui.locateAllOnScreen(
                self.img,
                confidence=confidence,
                region=(
                    region_item.x,
                    region_item.y,
                    region_item.width,
                    region_item.height,
                ),
                grayscale=grayscale,
            )
            if locations:
                for location in locations:
                    if all(
                        map(
                            lambda x: pow(location.left - x.left, 2)
                            + pow(location.top - x.top, 2)
                            > distance,
                            elements,
                        )
                    ):
                        elements.append(location)
            if elements:
                for element in elements:
                    element = pyautogui.center(element)
                    look_region = (element[0], element[1], 267, 312)
                    Button.click_lock_item(self.name, look_region)
        except pyautogui.ImageNotFoundException:
            return False
        except pyscreeze.ImageNotFoundException:
            return False
        except OSError as e:
            logger.error(f"Item buy: {e}")


Attack4EveryEndRound_lv4 = Item("Attack4EveryEndRound_lv4")
Attack6_Range4_lv1 = Item("Attack6_Range4_lv1", number_need_buy=1)
Attack10EveryBuyPlus5_lv2 = Item("Attack10EveryBuyPlus5_lv2", number_need_buy=10)
Attack12_Kill1000_Unique_lv2 = Item(
    "Attack12_Kill1000_Unique_lv2", number_need_buy=1, grayscale=False, confidence=0.9
)
Attack16_Arcane16_lv3 = Item("Attack16_Arcane16_lv3")
Attack16_Strike16_lv3 = Item("Attack16_Strike16_lv3")
Attack16Every1RevivalCount_lv5 = Item("Attack16Every1RevivalCount_lv5")
Attack35_Cooldown15_lv6 = Item("Attack35_Cooldown15_lv6")
Attack35_Kill1000_Unique_lv5 = Item(
    "Attack35_Kill1000_Unique_lv5", number_need_buy=1, grayscale=False, confidence=0.9
)
Bicycle_lv3 = Item("Bicycle_lv3", number_need_buy=0)
Cooldown16_Kill1000_Unique_lv2 = Item(
    "Cooldown16_Kill1000_Unique_lv2",
    number_need_buy=1,
    grayscale=False,
    confidence=0.9,
)
Cooldown21_lv5 = Item("Cooldown21_lv5", number_need_buy=1)
Cooldown45_Speed15_lv6 = Item("Cooldown45_Speed15_lv6", number_need_buy=1)
Cooldown50_Attack10_Health20_lv6 = Item(
    "Cooldown50_Attack10_Health20_lv6", number_need_buy=1
)
Critical9_Luck_lv3 = Item("Critical9_Luck_lv3", number_need_buy=1)
Critical10_Attack5_lv1 = Item("Critical10_Attack5_lv1", number_need_buy=2)
Critical16_Kill1000_Unique_lv2 = Item(
    "Critical16_Kill1000_Unique_lv2",
    number_need_buy=1,
    grayscale=False,
    confidence=0.9,
)
Critical20_Defense_lv3 = Item("Critical20_Defense_lv3", number_need_buy=1)
Critical30_Defense10_lv5 = Item("Critical30_Defense10_lv5", number_need_buy=1)
Critical40_Kill1000_Unique_lv5 = Item(
    "Critical40_Kill1000_Unique_lv5",
    number_need_buy=1,
    grayscale=False,
    confidence=0.9,
)
Defense20_Speed10_lv2 = Item("Defense20_Speed10_lv2", number_need_buy=1)
Defense24_Evasion12_Lv3 = Item("Defense24_Evasion12_Lv3", number_need_buy=1)
Critical21_For_Precise_lv3 = Item("Critical21_For_Precise_lv3")
EnemyCount10_lv6 = Item("EnemyCount10_lv6")
Evasion6_For_Precise_lv1 = Item("Evasion6_For_Precise_lv1", number_need_buy=2)
Evasion8_Speed5_lv1 = Item("Evasion8_Speed5_lv1", number_need_buy=2)
Evasion12_Strike6_lv2 = Item("Evasion12_Strike6_lv2", number_need_buy=2)
Evasion13_Health13_lv2 = Item("Evasion13_Health13_lv2", number_need_buy=2)
Evasion16_Investment16_lv3 = Item("Evasion16_Investment16_lv3", number_need_buy=2)
Evasion21_Attack5_lv4 = Item("Evasion21_Attack5_lv4", number_need_buy=2)
Every30InvenstmentPlusDefense1_lv6 = Item(
    "Every30InvenstmentPlusDefense1_lv6", number_need_buy=1
)
Exp20_Range5_lv1 = Item("Exp20_Range5_lv1", 1)
Exp40_Luck6_lv2 = Item("Exp40_Luck6_lv2", 1)
Exp45_Attack4_lv2 = Item("Exp45_Attack4_lv2", 1)
ExtraDamage10_lv3 = Item("ExtraDamage10_lv3")
ExtraDamage13_For_Precise_lv2 = Item("ExtraDamage13_For_Precise_lv2")
ExtraDamage14_Kill1000_Unique_lv2 = Item(
    "ExtraDamage14_Kill1000_Unique_lv2",
    number_need_buy=1,
    grayscale=False,
    confidence=0.9,
)
ExtraDamage20FullHp_lv3 = Item("ExtraDamage20FullHp_lv3", number_need_buy=1)
ExtraDamage30_Luck30_lv5 = Item("ExtraDamage30_Luck30_lv5")
ExtraDamage30_lv6 = Item("ExtraDamage30_lv6")
ExtraDamage40_HitRecovery8_lv6 = Item("ExtraDamage40_HitRecovery8_lv6")
ExtraDamage40_Kill100_Unique_lv5 = Item(
    "ExtraDamage40_Kill100_Unique_lv5",
    number_need_buy=1,
    grayscale=False,
    confidence=0.9,
)
Health30_Speed20_lv4 = Item("Health30_Speed20_lv4", 0)
Health48_For_Precise_lv3 = Item("Health48_For_Precise_lv3", 1)
Health88_lv5 = Item("Health88_lv5", 1)
HealthRegen10_For_Precise_lv1 = Item("HealthRegen10_For_Precise_lv1")
HealthRegen12_HitRecovery15_lv2 = Item("HealthRegen12_HitRecovery15_lv2")
HealthRegen18_Mango50_lv2 = Item("HealthRegen18_Mango50_lv2")
HealthRegen20_Strike20_lv2 = Item("HealthRegen20_Strike20_lv2")
HealthRegen45_Invest99_lv5 = Item("HealthRegen45_Invest99_lv5")
HealthRegen52_HitRecovery25_lv6 = Item("HealthRegen52_HitRecovery25_lv6")
Holding_Plus_Cooldown35_lv4 = Item("Holding_Plus_Cooldown35_lv4", number_need_buy=0)
Holding_Plus_Def32_lv4 = Item("Holding_Plus_Def32_lv4", number_need_buy=0)
Holding_Plus_HealthRegen30_lv4 = Item(
    "Holding_Plus_HealthRegen30_lv4", number_need_buy=0
)
Immunity_Unique_lv5 = Item("Immunity_Unique_lv5", number_need_buy=1)
Immunity2_lv2 = Item("Immunity2_lv2")
Immunity6_lv3 = Item("Immunity6_lv3")
Immunity10_lv5 = Item("Immunity10_lv5")
ImmunityCount4_lv4 = Item("ImmunityCount4_lv4")
Investment88_For_Precise_lv1 = Item("Investment88_For_Precise_lv1", 6)
Investment138_Defense3_lv2 = Item("Investment138_Defense3_lv2", 3)
Investment198_Speed7_lv3 = Item("Investment198_Speed7_lv3", 3)
Investment218_Evasion8_lv3 = Item("Investment218_Evasion8_lv3", 3)
Investment368_HitRecovery18_lv5 = Item("Investment368_HitRecovery18_lv5", 1)
Locomotive_lv2 = Item("Locomotive_lv2")
LostAll_Investments_Get_Attack_Unique_lv6 = Item(
    "LostAll_Investments_Get_Attack_Unique_lv6", number_need_buy=1
)
Luck13_lv1 = Item("Luck13_lv1", number_need_buy=2)
Luck32ForPrecise_lv2 = Item("Luck32ForPrecise_lv2", number_need_buy=2)
Luck45_HitRecovery25_lv3 = Item("Luck45_HitRecovery25_lv3", number_need_buy=2)
Luck54_Arcane27_lv4 = Item("Luck54_Arcane27_lv4", number_need_buy=2)
Luck60_Speed25_lv4 = Item("Luck60_Speed25_lv4", number_need_buy=0)
Luck60ForPrecise_lv5 = Item("Luck60ForPrecise_lv5", number_need_buy=1)
MasterChefHat_lv2 = Item("MasterChefHat_lv2", 2)
Minazuki_lv4 = Item("Minazuki_lv4")
MultishotDamage20_lv3 = Item("MultishotDamage20_lv3", 1)
MultishotRate100_Precision5_lv2 = Item("MultishotRate100_Precision5_lv2", 1)
PantyMask_lv6 = Item("PantyMask_lv6", 1)
PickupRange100_lv1 = Item("PickupRange100_lv1", number_need_buy=3)
PickupRange300_Unique_lv3 = Item("PickupRange300_Unique_lv3", number_need_buy=1)
Pillager_lv4 = Item("Pillager_lv4")
PreciseDamage12_Every1s_Plus1_lv6 = Item(
    "PreciseDamage12_Every1s_Plus1_lv6", number_need_buy=1
)
PreciseDamage12_Speed12_lv2 = Item("PreciseDamage12_Speed12_lv2", number_need_buy=1)
PreciseDamage13_Investment33_lv2 = Item(
    "PreciseDamage13_Investment33_lv2", number_need_buy=1
)
PreciseDamage16_Strike16_lv3 = Item("PreciseDamage16_Strike16_lv3")
Presision40_Defense_lv6 = Item("Presision40_Defense_lv6", number_need_buy=1)
Presision40_Range10_lv6 = Item("Presision40_Range10_lv6", number_need_buy=1)
Question_lv2 = Item("Question_lv2")
Question_lv4 = Item("Question_lv4")
Random_10_28_Evasion_lv4 = Item("Random_10_28_Evasion_lv4", number_need_buy=2)
Random_10_28_HealthRegen_lv3 = Item("Random_10_28_HealthRegen_lv3")
Random_15_35_Precision_lv5 = Item("Random_15_35_Precision_lv5")
Random_16_36_Defense_lv4 = Item("Random_16_36_Defense_lv4")
Range4_AracaneDamage12_lv1 = Item("Range4_AracaneDamage12_lv1", number_need_buy=1)
Range4_StrikeDamage10_lv1 = Item("Range4_StrikeDamage10_lv1", number_need_buy=1)
Range15_Invest55_lv5 = Item("Range15_Invest55_lv5", number_need_buy=1)
Range16_Def16_lv5 = Item("Range16_Def16_lv5", number_need_buy=0)
Range24_ExtraDamage14_lv6 = Item("Range24_ExtraDamage14_lv6", number_need_buy=0)
RevivalCount1_CriticalRate5_lv3 = Item("RevivalCount1_CriticalRate5_lv3")
RevivalCount1_Health5_lv4 = Item("RevivalCount1_Health5_lv4")
Set_Defense8_lv2 = Item("Set_Defense8_lv2", number_need_buy=1)
Set_Attack24_lv5 = Item("Set_Attack24_lv5", number_need_buy=1)
Set_CriticalRate18_lv4 = Item("Set_CriticalRate18_lv4", number_need_buy=1)
Set_Defense8_lv2 = Item("Set_Defense8_lv2", number_need_buy=1)
Set_Defense19_lv3 = Item("Set_Defense19_lv3", number_need_buy=1)
Set_Defense188_lv3 = Item("Set_Defense188_lv3", number_need_buy=1)
Set_ExtraDamage13_lv3 = Item("Set_ExtraDamage13_lv3", number_need_buy=1)
Set_ExtraDamage17_lv4 = Item("Set_ExtraDamage17_lv4", number_need_buy=1)
Set_Investment108_lv2 = Item("Set_Investment108_lv2", number_need_buy=1)
Set_Luck88_lv6 = Item("Set_Luck88_lv6", number_need_buy=1)
Set_Speed_lv1 = Item("Set_Speed_lv1", number_need_buy=1)
Set_Speed22_lv2 = Item("Set_Speed22_lv2", number_need_buy=1)
Set_Speed25_lv3 = Item("Set_Speed25_lv3", number_need_buy=1)
ShopDiscount_lv1 = Item("ShopDiscount_lv1", number_need_buy=5)
ShopPlus1_lv4 = Item("ShopPlus1_lv4", number_need_buy=1)
SoulCrystalsPlus35EveryMango_lv2 = Item(
    "SoulCrystalsPlus35EveryMango_lv2", number_need_buy=1
)
Speed45_Luck5_lv5 = Item("Speed45_Luck5_lv5", number_need_buy=1)
Speed80_Range8_lv6 = Item("Speed80_Range8_lv6", number_need_buy=1)
SplitTheVoid_lv2 = Item("SplitTheVoid_lv2")
TomeOfKnowledge_lv3 = Item("TomeOfKnowledge_lv3")


def buy_all_previous_item():
    if global_event.check_event():
        return False
    global previous_item
    if previous_item:
        logger.debug("Ban dang mua item")
        for key, value in list(previous_item.items()):
            if value.number < value.number_need_buy:
                if global_event.check_event():
                    return False
                global_event.sleep(0.5)
                pydirectinput.click(key[0], key[1])
                pydirectinput.moveTo(222, 213)
                if Button.check_money():
                    logger.info(f"Ban da mua thanh cong 1 cai {value.name}")
                    value.number += 1
                    cgv.count_of_buy += 1
                    del previous_item[key]
                else:
                    look_region = (key[0], key[1], 267, 312)
                    cgv.set_money(False)
                    if Button.click_lock_item(value.name, look_region) is True:
                        # del previous_item[key]
                        logger.debug("Khong du tien, Khoa item")

                    else:
                        del previous_item[key]
            else:
                del previous_item[key]
                # return False
    else:
        # logger.debug("Khong co item khoa o round truoc")
        pass


def buy_all_set_item(round_number):
    if global_event.check_event():
        return False
    logger.debug("Ban dang tim set item")
    if 2 < round_number < 18:
        PickupRange100_lv1.buy()
        if PickupRange100_lv1.number < 3:
            PickupRange300_Unique_lv3.buy()
    if round_number > 4:
        Set_Speed_lv1.buy()
        Set_Speed22_lv2.buy()
        Set_Speed25_lv3.buy()
        Set_Defense8_lv2.buy()
        Set_Defense19_lv3.buy()
        Set_Investment108_lv2.buy()
        Set_Defense188_lv3.buy()
        Set_ExtraDamage17_lv4.buy()
        Set_CriticalRate18_lv4.buy()
        Set_Attack24_lv5.buy()
        Set_Luck88_lv6.buy()
        Set_ExtraDamage13_lv3.buy()
        Attack10EveryBuyPlus5_lv2.buy()
        SplitTheVoid_lv2.buy()
    if 4 < round_number < 18:
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

    if round_number <= 9:
        logger.debug("Ban dang tim item investments")
        Investment88_For_Precise_lv1.buy()
        Investment138_Defense3_lv2.buy()
    elif round_number <= 15:
        logger.debug("Ban dang tim item investments")
        Investment138_Defense3_lv2.buy()
        Investment198_Speed7_lv3.buy()
        Investment368_HitRecovery18_lv5.buy()


def buy_all_item_lv1(round_number):
    if global_event.check_event():
        return
    if 3 <= round_number <= 12:
        logger.debug("Ban dang tim item lv1")
        Luck13_lv1.buy()
        ShopDiscount_lv1.buy()
        Evasion8_Speed5_lv1.buy()
        Exp20_Range5_lv1.buy()
        Evasion6_For_Precise_lv1.buy()
        HealthRegen10_For_Precise_lv1.buy()
        Range4_AracaneDamage12_lv1.buy()
        Range4_StrikeDamage10_lv1.buy()
        Critical10_Attack5_lv1.buy()
        Attack6_Range4_lv1.buy()


def buy_all_item_lv2(round_number):
    if global_event.check_event():
        return
    if 3 <= round_number <= 14:
        logger.debug("Ban dang tim item lv2")
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
        SoulCrystalsPlus35EveryMango_lv2.buy()
        MultishotRate100_Precision5_lv2.buy()
        Question_lv2.buy()
        PreciseDamage13_Investment33_lv2.buy()


def buy_all_item_lv3(round_number):
    if global_event.check_event():
        return
    if round_number >= 5:
        logger.debug("Ban dang tim item lv3")
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
        Defense24_Evasion12_Lv3.buy()
        ExtraDamage20FullHp_lv3.buy()


def buy_all_item_lv4(round_number):
    if global_event.check_event():
        return

    if round_number >= 6:
        logger.debug("Ban dang tim item lv4")
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
        Attack4EveryEndRound_lv4.buy()
        Question_lv4.buy()
    if 6 <= round_number <= 15:
        ShopPlus1_lv4.buy()


def buy_all_item_lv5(round_number):
    if global_event.check_event():
        return
    if round_number >= 7:
        logger.debug("Ban dang tim item lv5")
        Immunity10_lv5.buy()
        Immunity_Unique_lv5.buy()
        Health88_lv5.buy()
        Range16_Def16_lv5.buy()
        Range15_Invest55_lv5.buy()
        Critical30_Defense10_lv5.buy()
        ExtraDamage30_Luck30_lv5.buy()
        HealthRegen45_Invest99_lv5.buy()
        Cooldown21_lv5.buy()
        Luck60ForPrecise_lv5.buy()
        Attack16Every1RevivalCount_lv5.buy()
        Random_15_35_Precision_lv5.buy()
        Speed45_Luck5_lv5.buy()


def buy_all_item_lv6(round_number):
    if global_event.check_event():
        return
    if round_number >= 8:
        logger.info("Ban dang tim item lv6")
        PantyMask_lv6.buy()
        ExtraDamage30_lv6.buy()
        Cooldown45_Speed15_lv6.buy()
        Range24_ExtraDamage14_lv6.buy()
        PreciseDamage12_Every1s_Plus1_lv6.buy()
        EnemyCount10_lv6.buy()
        Attack35_Cooldown15_lv6.buy()
        Cooldown50_Attack10_Health20_lv6.buy()
        ExtraDamage40_HitRecovery8_lv6.buy()
        HealthRegen52_HitRecovery25_lv6.buy()
        LostAll_Investments_Get_Attack_Unique_lv6.buy()
        Presision40_Defense_lv6.buy()
        Presision40_Range10_lv6.buy()
        Speed80_Range8_lv6.buy()
        if LostAll_Investments_Get_Attack_Unique_lv6.number < 1:
            Every30InvenstmentPlusDefense1_lv6.buy()


def buy_all_item(round_number):
    if global_event.check_event():
        return False
    logger.info(f"Ban dang tim item round {round_number}")
    if cgv.check_money() is False:
        logger.debug("Khong du tien, next round")
        return False
    t_buy_all_item_investments = threading.Thread(
        target=buy_all_item_investments, args=(round_number,)
    )
    t_buy_all_set_item = threading.Thread(target=buy_all_set_item, args=(round_number,))
    t_buy_all_item_lv1 = threading.Thread(target=buy_all_item_lv1, args=(round_number,))
    t_buy_all_item_lv2 = threading.Thread(target=buy_all_item_lv2, args=(round_number,))
    t_buy_all_item_lv3 = threading.Thread(target=buy_all_item_lv3, args=(round_number,))
    t_buy_all_item_lv4 = threading.Thread(target=buy_all_item_lv4, args=(round_number,))
    t_buy_all_item_lv5 = threading.Thread(target=buy_all_item_lv5, args=(round_number,))
    t_buy_all_item_lv6 = threading.Thread(target=buy_all_item_lv6, args=(round_number,))
    t_buy_all_item_investments.start()
    t_buy_all_set_item.start()
    t_buy_all_item_lv1.start()
    t_buy_all_item_lv2.start()
    t_buy_all_item_lv3.start()
    t_buy_all_item_lv4.start()
    t_buy_all_item_lv5.start()
    t_buy_all_item_lv6.start()

    t_buy_all_item_investments.join()
    t_buy_all_set_item.join()
    t_buy_all_item_lv1.join()
    t_buy_all_item_lv2.join()
    t_buy_all_item_lv3.join()
    t_buy_all_item_lv4.join()
    t_buy_all_item_lv5.join()
    t_buy_all_item_lv6.join()


def reset_item():
    if global_event.check_event():
        return False
    Attack4EveryEndRound_lv4.reset_item_number()
    Attack6_Range4_lv1.reset_item_number()
    Attack10EveryBuyPlus5_lv2.reset_item_number()
    Attack12_Kill1000_Unique_lv2.reset_item_number()
    Attack16_Arcane16_lv3.reset_item_number()
    Attack16_Strike16_lv3.reset_item_number()
    Attack16Every1RevivalCount_lv5.reset_item_number()
    Attack35_Cooldown15_lv6.reset_item_number()
    Attack35_Kill1000_Unique_lv5.reset_item_number()
    Bicycle_lv3.reset_item_number()
    Cooldown16_Kill1000_Unique_lv2.reset_item_number()
    Cooldown21_lv5.reset_item_number()
    Cooldown45_Speed15_lv6.reset_item_number()
    Cooldown50_Attack10_Health20_lv6.reset_item_number()
    Critical9_Luck_lv3.reset_item_number()
    Critical10_Attack5_lv1.reset_item_number()
    Critical16_Kill1000_Unique_lv2.reset_item_number()
    Critical20_Defense_lv3.reset_item_number()
    Critical21_For_Precise_lv3.reset_item_number()
    Critical30_Defense10_lv5.reset_item_number()
    Critical40_Kill1000_Unique_lv5.reset_item_number()
    Defense20_Speed10_lv2.reset_item_number()
    Defense24_Evasion12_Lv3.reset_item_number()
    EnemyCount10_lv6.reset_item_number()
    Evasion6_For_Precise_lv1.reset_item_number()
    Evasion8_Speed5_lv1.reset_item_number()
    Evasion13_Health13_lv2.reset_item_number()
    Evasion13_Health13_lv2.reset_item_number()
    Evasion16_Investment16_lv3.reset_item_number()
    Evasion21_Attack5_lv4.reset_item_number()
    Every30InvenstmentPlusDefense1_lv6.reset_item_number()
    Exp20_Range5_lv1.reset_item_number()
    Exp40_Luck6_lv2.reset_item_number()
    Exp45_Attack4_lv2.reset_item_number()
    ExtraDamage10_lv3.reset_item_number()
    ExtraDamage13_For_Precise_lv2.reset_item_number()
    ExtraDamage14_Kill1000_Unique_lv2.reset_item_number()
    ExtraDamage20FullHp_lv3.reset_item_number()
    ExtraDamage30_Luck30_lv5.reset_item_number()
    ExtraDamage30_lv6.reset_item_number()
    ExtraDamage40_HitRecovery8_lv6.reset_item_number()
    ExtraDamage40_Kill100_Unique_lv5.reset_item_number()
    Health30_Speed20_lv4.reset_item_number()
    Health48_For_Precise_lv3.reset_item_number()
    Health88_lv5.reset_item_number()
    HealthRegen10_For_Precise_lv1.reset_item_number()
    HealthRegen12_HitRecovery15_lv2.reset_item_number()
    HealthRegen18_Mango50_lv2.reset_item_number()
    HealthRegen20_Strike20_lv2.reset_item_number()
    HealthRegen45_Invest99_lv5.reset_item_number()
    HealthRegen52_HitRecovery25_lv6.reset_item_number()
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
    LostAll_Investments_Get_Attack_Unique_lv6.reset_item_number()
    Luck13_lv1.reset_item_number()
    Luck32ForPrecise_lv2.reset_item_number()
    Luck45_HitRecovery25_lv3.reset_item_number()
    Luck54_Arcane27_lv4.reset_item_number()
    Luck60_Speed25_lv4.reset_item_number()
    Luck60ForPrecise_lv5.reset_item_number()
    MasterChefHat_lv2.reset_item_number()
    Minazuki_lv4.reset_item_number()
    MultishotDamage20_lv3.reset_item_number()
    MultishotRate100_Precision5_lv2.reset_item_number()
    PantyMask_lv6.reset_item_number()
    PickupRange100_lv1.reset_item_number()
    PickupRange300_Unique_lv3.reset_item_number()
    Pillager_lv4.reset_item_number()
    PreciseDamage12_Every1s_Plus1_lv6.reset_item_number()
    PreciseDamage12_Speed12_lv2.reset_item_number()
    PreciseDamage13_Investment33_lv2.reset_item_number()
    PreciseDamage16_Strike16_lv3.reset_item_number()
    Presision40_Defense_lv6.reset_item_number()
    Presision40_Range10_lv6.reset_item_number()
    Question_lv2.reset_item_number()
    Question_lv4.reset_item_number()
    Random_10_28_Evasion_lv4.reset_item_number()
    Random_10_28_HealthRegen_lv3.reset_item_number()
    Random_15_35_Precision_lv5.reset_item_number()
    Random_16_36_Defense_lv4.reset_item_number()
    Range4_AracaneDamage12_lv1.reset_item_number()
    Range4_StrikeDamage10_lv1.reset_item_number()
    Range15_Invest55_lv5.reset_item_number()
    Range16_Def16_lv5.reset_item_number()
    Range24_ExtraDamage14_lv6.reset_item_number()
    RevivalCount1_CriticalRate5_lv3.reset_item_number()
    RevivalCount1_Health5_lv4.reset_item_number()
    Set_Attack24_lv5.reset_item_number()
    Set_CriticalRate18_lv4.reset_item_number()
    Set_Defense8_lv2.reset_item_number()
    Set_Defense19_lv3.reset_item_number()
    Set_Defense188_lv3.reset_item_number()
    Set_ExtraDamage13_lv3.reset_item_number()
    Set_ExtraDamage17_lv4.reset_item_number()
    Set_Investment108_lv2.reset_item_number()
    Set_Luck88_lv6.reset_item_number()
    Set_Speed_lv1.reset_item_number()
    Set_Speed22_lv2.reset_item_number()
    Set_Speed25_lv3.reset_item_number()
    ShopDiscount_lv1.reset_item_number()
    ShopPlus1_lv4.reset_item_number()
    SoulCrystalsPlus35EveryMango_lv2.reset_item_number()
    Speed45_Luck5_lv5.reset_item_number()
    Speed80_Range8_lv6.reset_item_number()
    SplitTheVoid_lv2.reset_item_number()
    TomeOfKnowledge_lv3.reset_item_number()


def reset_previous_item():
    global previous_item
    previous_item.clear()


def get_all_name_item():
    image_files = [f for f in os.listdir("assets/img/item") if f.endswith(".png")]
    list_name_item = list()
    for img in image_files:
        img = img.split(".")[0]
        list_name_item.append(img)
    return list_name_item


def check_all_item():
    for item in get_all_name_item():
        Item(item).check_item(confidence=0.85, grayscale=False)


if __name__ == "__main__":
    dota2 = SelectWindow("Dota 2")
    dota2.move_window_to(0, 0)
    dota2.set_foreground()
    check_all_item()

    pass
