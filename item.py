
import pyautogui
import time
import button


class infor_item:
    def __init__(self, para_name, para_item_number=0):
        self.name = para_name
        self.img = "data\\image\\item\\"+para_name+".png"
        self.number = para_item_number

    def reset_item_number(self):
        self.number = 0


ShopDiscount = infor_item("ShopDiscount")

Investment_lv1_precise = infor_item("Investment_lv1_precise")
TomeOfKnowledge = infor_item("TomeOfKnowledge")
Exp20_Range5 = infor_item("Exp20_Range5")

Exp40_Luck6 = infor_item("Exp40_Luck6")

Locomotive = infor_item("Locomotive")

MasterChefHat = infor_item("MasterChefHat")

Helmet_32Luck_Precise = infor_item("Helmet_32Luck_Precise")

# WitlessShako_Health_Precise
WitlessShako_Health_Precise = infor_item("WitlessShako_Health_Precise")

# NorthWind_Luck13
NorthWind_Luck13 = infor_item("NorthWind_Luck13")

# Vtuber_Inves198_Speed7
Vtuber_Inves198_Speed7 = infor_item("Vtuber_Inves198_Speed7")

# Bicycle_lv3
Bicycle_lv3 = infor_item("Bicycle_lv3")
Attack16_Arcane16 = infor_item("Attack16_Arcane16")
Attack16_Strike16 = infor_item("Attack16_Strike16")
Critical30_Defense10 = infor_item("Critical30_Defense10")
HealthRegen12_HitRecovery15 = infor_item("HealthRegen12_HitRecovery15")
Holding_30HealthRegen = infor_item("Holding_30HealthRegen")
Luck60_Speed25 = infor_item("Luck60_Speed25")
SplitTheVoid = infor_item("SplitTheVoid")


def buy_item(infor_item):
    """
    This function is used to buy a specific item.

    Parameters:
    infor_item (infor_item object): The information of the item to buy.

    Returns:
    True if the item is bought successfully, False otherwise.
    """
    try:
        res = pyautogui.locateOnScreen(
            infor_item.img, confidence=0.8, region=(0, 0, 1916, 1134))
        print("xuat hien ", infor_item.name)
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        pyautogui.click(res_center)
        return True
    except pyautogui.ImageNotFoundException:
        return False


def buy_item_infor(infor_item, number_item=1):
    """
    This function is used to buy a specific number of a specific item.

    Parameters:
    infor_item (infor_item object): The information of the item to buy.
    number_item (int): The number of items to buy.

    Returns:
    Nothing.
    """
    number = infor_item.number
    if number_item > number:
        number_buy = number_item-number
        for n in range(0, number_buy):
            buy = buy_item(infor_item)
            if buy is True:
                print("Bạn đã có {} cái {}".format(
                    infor_item.number, infor_item.name))
                print("Bạn cần mua thêm {} cái {} nữa".format(
                    number_buy, infor_item.name))
                if button.check_not_money():
                    break
                else:
                    number = number+1
                    print("Bạn đã mua thành công 1 cái {}, bạn cần mua thêm {} nữa".format(
                        infor_item.name, number_buy-number))
                    infor_item.number = number
def reset_item():
    global ShopDiscount, Investment_lv1_precise,TomeOfKnowledge,Exp20_Range5,Exp40_Luck6,Locomotive
    global MasterChefHat, Helmet_32Luck_Precise ,WitlessShako_Health_Precise, NorthWind_Luck13, Vtuber_Inves198_Speed7
    global Bicycle_lv3, Attack16_Arcane16,Attack16_Strike16, Critical30_Defense10, HealthRegen12_HitRecovery15
    global Holding_30HealthRegen, Luck60_Speed25, SplitTheVoid 
    ShopDiscount.reset_item_number()
    Investment_lv1_precise.reset_item_number()
    TomeOfKnowledge.reset_item_number()
    Exp20_Range5.reset_item_number()
    Exp40_Luck6.reset_item_number()
    Locomotive.reset_item_number()
    MasterChefHat.reset_item_number()
    Helmet_32Luck_Precise.reset_item_number()
    WitlessShako_Health_Precise.reset_item_number()
    NorthWind_Luck13.reset_item_number()
    Vtuber_Inves198_Speed7.reset_item_number()
    Bicycle_lv3.reset_item_number()
    Attack16_Arcane16.reset_item_number()
    Attack16_Strike16.reset_item_number()
    Critical30_Defense10.reset_item_number()
    HealthRegen12_HitRecovery15.reset_item_number()
    Holding_30HealthRegen.reset_item_number()
    Luck60_Speed25.reset_item_number()
    SplitTheVoid.reset_item_number()


    

def buy_ShopDiscount():
    """
    This function is used to buy all items in the ShopDiscount category.
    """
    buy_item_infor(ShopDiscount, 5)


def buy_Investment_lv1_precise():
    """
    This function is used to buy all items in the Investment_lv1_precise category.
    """
    buy_item_infor(Investment_lv1_precise, 5)


def buy_TomeOfKnowledge():
    """
    This function is used to buy all items in the TomeOfKnowledge category.
    """
    buy_item_infor(TomeOfKnowledge, 5)


def buy_Exp20_Range5():
    """
    This function is used to buy all items in the Exp20_Range5 category.
    """
    buy_item_infor(Exp20_Range5, 5)


def buy_Exp40_Luck6():
    """
    This function is used to buy all items in the Exp40_Luck6 category.
    """
    buy_item_infor(Exp40_Luck6, 5)


def buy_Locomotive():
    """
    This function is used to buy all items in the Locomotive category.
    """
    buy_item_infor(Locomotive, 5)


def buy_MasterChefHat():
    """
    This function is used to buy all items in the MasterChefHat category.
    """
    buy_item_infor(MasterChefHat, 5)


def buy_Bicycle_lv3():
    buy_item_infor(Bicycle_lv3)


def buy_Attack16_Arcane16():
    buy_item_infor(Attack16_Arcane16, 5)


def buy_Attack16_Strike16():
    buy_item_infor(Attack16_Strike16, 5)


def buy_Critical30_Defense10():
    buy_item_infor(Critical30_Defense10, 5)


def buy_HealthRegen12_HitRecovery15():
    buy_item_infor(HealthRegen12_HitRecovery15, 5)


def buy_Holding_30HealthRegen():
    buy_item_infor(Holding_30HealthRegen, 5)


def buy_Luck60_Speed25():
    buy_item_infor(Luck60_Speed25, 5)


def buy_SplitTheVoid():
    buy_item_infor(SplitTheVoid, 5)


def buy_Vtuber_Inves198_Speed7():
    buy_item_infor(Vtuber_Inves198_Speed7, 5)


def buy_Helmet_32Luck_Precise():
    buy_item_infor(Helmet_32Luck_Precise, 5)


