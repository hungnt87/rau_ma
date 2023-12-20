import pyautogui
import time
import button

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
        print("xuat hien ", ItemInfo.name)
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        pyautogui.click(res_center)
        return True
    except pyautogui.ImageNotFoundException:
        return False


def buy_item_info(ItemInfo, number_item=5):
    """
    This function is used to buy a specific number of a specific item.

    Parameters:
    ItemInfo (ItemInfo object): The information of the item to buy.
    number_item (int): The number of items to buy.

    Returns:
    Nothing.
    """
    print("Bạn đang tìm item {}".format(ItemInfo.name))
    global count_buy_item
    number = ItemInfo.number
    if number_item > number:
        number_buy = number_item - number
        for n in range(0, number_buy):
            buy = buy_item(ItemInfo)
            if buy is True:
                print("Bạn đã có {} cái {}".format(
                    ItemInfo.number, ItemInfo.name))
                print("Bạn cần mua thêm {} cái {} nữa".format(
                    number_buy, ItemInfo.name))
                if button.check_not_money():
                    break
                else:
                    number = number + 1
                    print("Bạn đã mua thành công 1 cái {}, bạn cần mua thêm {} nữa".format(
                        ItemInfo.name, number_buy - number))
                    ItemInfo.number = number
                    count_buy_item = count_buy_item + 1
                    print("Ban da mua item lan thu {}".format(count_buy_item))


Attack16_Arcane16_lv3 = ItemInfo("Attack16_Arcane16_lv3")
Attack16_Strike16_lv3 = ItemInfo("Attack16_Strike16_lv3")
Bicycle_lv3 = ItemInfo("Bicycle_lv3")
Cooldown16_Kill1000_Unique_lv2 = ItemInfo("Cooldown16_Kill1000_Unique_lv2")
Cooldown45_Speed15_lv6 = ItemInfo("Cooldown45_Speed15_lv6")
Critical30_Defense10 = ItemInfo("Critical30_Defense10")
Defense20_Speed10_lv2 = ItemInfo("Defense20_Speed10_lv2")
Evasion6_For_Pricise_lv1= ItemInfo("Evasion6_For_Pricise_lv1")
Evasion13_Health13_lv2 = ItemInfo("Evasion13_Health13_lv2")
Evasion21_Attack5_lv4 = ItemInfo("Evasion21_Attack5_lv4")
Evasion6_For_Precise_lv1 = ItemInfo("Evasion6_For_Precise_lv1")
Exp20_Range5 = ItemInfo("Exp20_Range5")
Exp40_Luck6 = ItemInfo("Exp40_Luck6")
ExtraDamage10_lv3 = ItemInfo("ExtraDamage10_lv3")
ExtraDamage14_Kill1000_Unique_lv2 = ItemInfo("ExtraDamage14_Kill1000_Unique_lv2")
ExtraDamage30_Luck30_lv5 = ItemInfo("ExtraDamage30_Luck30_lv5")
ExtraDamage30_lv6 = ItemInfo("ExtraDamage30_lv6")
ExtraDamage40_Kill100_Unique_lv5 = ItemInfo("ExtraDamage40_Kill100_Unique_lv5")
Health30_Speed20_lv4 = ItemInfo("Health30_Speed20_lv4")
Health88_lv5 = ItemInfo("Health88_lv5")
HealthRegen10_For_Precise_lv1 = ItemInfo("HealthRegen10_For_Precise_lv1")
HealthRegen12_HitRecovery15 = ItemInfo("HealthRegen12_HitRecovery15")
Helmet_32Luck_Precise = ItemInfo("Helmet_32Luck_Precise")
Holding_30HealthRegen = ItemInfo("Holding_30HealthRegen")
Immunity_Unique_lv5 = ItemInfo("Immunity_Unique_lv5")
Investment_lv1_precise = ItemInfo("Investment_lv1_precise")
Locomotive_lv2 = ItemInfo("Locomotive_lv2")
Luck54_Arcane27_lv4 = ItemInfo("Luck54_Arcane27_lv4")
Luck60_Speed25 = ItemInfo("Luck60_Speed25")
MasterChefHat = ItemInfo("MasterChefHat")
NorthWind_Luck13 = ItemInfo("NorthWind_Luck13")
PickupRange100_lv1 = ItemInfo("PickupRange100_lv1")
PreciseDamage12_Every1s_Plus1 = ItemInfo("PreciseDamage12_Every1s_Plus1")
Random_10_28_Evasion_lv4 = ItemInfo("Random_10_28_Evasion_lv4")
Range24_ExtraDamage14_lv6 = ItemInfo("Range24_ExtraDamage14_lv6")
ShopDiscount = ItemInfo("ShopDiscount")
SplitTheVoid = ItemInfo("SplitTheVoid")
TomeOfKnowledge = ItemInfo("TomeOfKnowledge")
Vtuber_Inves198_Speed7 = ItemInfo("Vtuber_Inves198_Speed7")
WitlessShako_Health_Precise = ItemInfo("WitlessShako_Health_Precise")


def buy_pickup_range100_lv1():
    buy_item_info(PickupRange100_lv1,2)


def buy_precise_damage12_every1s_plus1():
    buy_item_info(PreciseDamage12_Every1s_Plus1)


def buy_cooldown16_kill1000_unique_lv2():
    buy_item_info(Cooldown16_Kill1000_Unique_lv2, 1)


def buy_defense20_speed10_lv2():
    buy_item_info(Defense20_Speed10_lv2, 5)


def buy_evasion13_health13_lv2():
    buy_item_info(Evasion13_Health13_lv2, 5)


def buy_evasion21_attack5_lv4():
    buy_item_info(Evasion21_Attack5_lv4, 5)


def buy_evasion6_for_precise_lv1():
    buy_item_info(Evasion6_For_Precise_lv1, 5)


def buy_extra_damage10_lv3():
    buy_item_info(ExtraDamage10_lv3, 5)


def buy_extra_damage14_kill1000_unique_lv2():
    buy_item_info(ExtraDamage14_Kill1000_Unique_lv2, 1)


def buy_extra_damage30_luck30_lv5():
    buy_item_info(ExtraDamage30_Luck30_lv5, 1)


def buy_extra_damage30_lv6():
    buy_item_info(ExtraDamage30_lv6, 5)


def buy_extra_damage40_kill100_unique_lv5():
    buy_item_info(ExtraDamage40_Kill100_Unique_lv5, 1)


def buy_health88_lv5():
    buy_item_info(Health88_lv5, 5)


def buy_cooldown45_speed15_lv6():
    buy_item_info(Cooldown45_Speed15_lv6, 5)


def buy_random_10_28_evasion_lv4():
    buy_item_info(Random_10_28_Evasion_lv4, 5)


def buy_luck54_arcane27_lv4():
    buy_item_info(Luck54_Arcane27_lv4, 5)


def buy_immunity_unique_lv5():
    buy_item_info(Immunity_Unique_lv5, 1)


def buy_range24_extra_damage14_lv6():
    buy_item_info(Range24_ExtraDamage14_lv6, 5)


def buy_health30_speed20_lv4():
    buy_item_info(Health30_Speed20_lv4, 5)


def buy_health_regen10_for_precise_lv1():
    buy_item_info(HealthRegen10_For_Precise_lv1, 5)


def buy_shop_discount():
    """
    This function is used to buy all items in the ShopDiscount category.
    """
    buy_item_info(ShopDiscount, 5)


def buy_investment_lv1_precise():
    """
    This function is used to buy all items in the Investment_lv1_precise category.
    """
    buy_item_info(Investment_lv1_precise, 5)


def buy_tome_of_knowledge():
    """
    This function is used to buy all items in the TomeOfKnowledge category.
    """
    buy_item_info(TomeOfKnowledge, 5)


def buy_exp20_range5():
    """
    This function is used to buy all items in the Exp20_Range5 category.
    """
    buy_item_info(Exp20_Range5, 5)


def buy_exp40_luck6():
    """
    This function is used to buy all items in the Exp40_Luck6 category.
    """
    buy_item_info(Exp40_Luck6, 5)


def buy_locomotive_lv2():
    """
    This function is used to buy all items in the Locomotive category.
    """
    buy_item_info(Locomotive_lv2, 5)


def buy_master_chef_hat():
    """
    This function is used to buy all items in the MasterChefHat category.
    """
    buy_item_info(MasterChefHat, 5)


def buy_bicycle_lv3():
    buy_item_info(Bicycle_lv3)


def buy_attack16_arcane16():
    buy_item_info(Attack16_Arcane16_lv3, 5)


def buy_attack16_strike16():
    buy_item_info(Attack16_Strike16_lv3, 5)


def buy_critical30_defense10():
    buy_item_info(Critical30_Defense10, 5)


def buy_health_regen12_hit_recovery15():
    buy_item_info(HealthRegen12_HitRecovery15, 5)


def buy_holding_30_health_regen():
    buy_item_info(Holding_30HealthRegen, 5)


def buy_luck60_speed25():
    buy_item_info(Luck60_Speed25, 5)


def buy_split_the_void():
    buy_item_info(SplitTheVoid, 5)


def buy_vtuber_inves198_speed7():
    buy_item_info(Vtuber_Inves198_Speed7, 5)


def buy_helmet_32_luck_precise():
    buy_item_info(Helmet_32Luck_Precise, 5)
def buy_all_item_lv1():
    buy_investment_lv1_precise()
    buy_shop_discount()
    buy_health_regen10_for_precise_lv1()
    buy_pickup_range100_lv1()
def buy_all_item_lv2():
    buy_locomotive_lv2()
    buy_defense20_speed10_lv2()
    buy_evasion13_health13_lv2()
    buy_cooldown16_kill1000_unique_lv2()
    buy_extra_damage14_kill1000_unique_lv2()

def buy_all_item_lv3():
    buy_bicycle_lv3()
    buy_extra_damage10_lv3()
    buy_extra_damage10_lv3()

def buy_all_item_lv4():
    buy_random_10_28_evasion_lv4()
    buy_luck54_arcane27_lv4()
    buy_health30_speed20_lv4()
    buy_evasion21_attack5_lv4()

def buy_all_item_lv5():
    buy_immunity_unique_lv5()
    buy_health88_lv5()
    buy_extra_damage40_kill100_unique_lv5()
    buy_extra_damage30_luck30_lv5()
def buy_all_item_lv6():
    buy_cooldown45_speed15_lv6()
    buy_range24_extra_damage14_lv6()
    buy_extra_damage30_lv6()

def reset_item():
    global Attack16_Arcane16_lv3, Attack16_Arcane16_lv3, Bicycle_lv3, Cooldown16_Kill1000_Unique_lv2
    global Cooldown45_Speed15_lv6, Critical30_Defense10, Defense20_Speed10_lv2, Evasion6_For_Pricise_lv1
    global Evasion13_Health13_lv2, Evasion21_Attack5_lv4, ExtraDamage10_lv3, ExtraDamage14_Kill1000_Unique_lv2
    global ExtraDamage30_Luck30_lv5, ExtraDamage30_lv6, ExtraDamage40_Kill100_Unique_lv5
    global Health30_Speed20_lv4, Health88_lv5, HealthRegen10_For_Precise_lv1
    global HealthRegen12_HitRecovery15, Holding_30HealthRegen, Luck54_Arcane27_lv4, Luck60_Speed25
    global MasterChefHat, Random_10_28_Evasion_lv4, ShopDiscount, SplitTheVoid, TomeOfKnowledge
    global Vtuber_Inves198_Speed7
    Attack16_Arcane16_lv3.reset_item_number()
    Attack16_Strike16_lv3.reset_item_number()
    Bicycle_lv3.reset_item_number()
    Cooldown16_Kill1000_Unique_lv2.reset_item_number()
    Cooldown45_Speed15_lv6.reset_item_number()
    Critical30_Defense10.reset_item_number()
    Defense20_Speed10_lv2.reset_item_number()
    Evasion6_For_Pricise_lv1.reset_item_number()
    Evasion13_Health13_lv2.reset_item_number()
    Evasion21_Attack5_lv4.reset_item_number()
    Evasion6_For_Precise_lv1.reset_item_number()
    Exp20_Range5.reset_item_number()
    Exp40_Luck6.reset_item_number()
    ExtraDamage10_lv3.reset_item_number()
    ExtraDamage14_Kill1000_Unique_lv2.reset_item_number()
    ExtraDamage30_Luck30_lv5.reset_item_number()
    ExtraDamage30_lv6.reset_item_number()
    ExtraDamage40_Kill100_Unique_lv5.reset_item_number()
    Health30_Speed20_lv4.reset_item_number()
    Health88_lv5.reset_item_number()
    HealthRegen10_For_Precise_lv1.reset_item_number()
    HealthRegen12_HitRecovery15.reset_item_number()
    Helmet_32Luck_Precise.reset_item_number()
    Holding_30HealthRegen.reset_item_number()
    Holding_30HealthRegen.reset_item_number()
    Immunity_Unique_lv5.reset_item_number()
    Investment_lv1_precise.reset_item_number()
    Locomotive_lv2.reset_item_number()
    Luck54_Arcane27_lv4.reset_item_number()
    Luck60_Speed25.reset_item_number()
    MasterChefHat.reset_item_number()
    NorthWind_Luck13.reset_item_number()
    Range24_ExtraDamage14_lv6.reset_item_number()
    PickupRange100_lv1.reset_item_number()
    PreciseDamage12_Every1s_Plus1.reset_item_number()
    Random_10_28_Evasion_lv4.reset_item_number()
    Range24_ExtraDamage14_lv6.reset_item_number()
    ShopDiscount.reset_item_number()
    SplitTheVoid.reset_item_number()
    TomeOfKnowledge.reset_item_number()
    Vtuber_Inves198_Speed7.reset_item_number()
    WitlessShako_Health_Precise.reset_item_number()




