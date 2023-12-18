"""
This script is used to automatically buy items in the game Village Life.
It uses the pyautogui library to control the mouse and automate the game.

The script contains functions to buy specific items, such as ShopDiscount, Investment_lv1_precise, TomeOfKnowledge, Exp20_Range5, Exp40_Luck6, Locomotive, etc.

The script also contains a function to buy all items in a specific category. For example, the function buy_all_shop_items() will buy all items in the ShopDiscount category.

The script also contains a function to check if the "Not Money" button is displayed. If the button is displayed, the script will not buy any items.

The script can be improved by adding more items to the list of items to buy, by adding more categories of items, and by adding additional functionality as needed.
"""

import pyautogui
import time
import button

class infor_item:
     def __init__(self,para_name,para_item_number):
         self.name= para_name
         self.img="data\\image\\item\\"+para_name+".png"
         self.number=para_item_number

# ShopDiscount
number_ShopDiscount = 0
ShopDiscount=infor_item("ShopDiscount",number_ShopDiscount)


# Investment_lv1_precise
number_Investment_lv1_precise = 0
Investment_lv1_precise = infor_item("Investment_lv1_precise",number_Investment_lv1_precise)


# TomeOfKnowledge
TomeOfKnowledg_number=0
TomeOfKnowledge=infor_item("TomeOfKnowledge",TomeOfKnowledg_number)

# Exp20_Range5
Exp20_Range5=infor_item("Exp20_Range5",0)

# Exp40_Luck6
Exp40_Luck6=infor_item("Exp40_Luck6",0)

# Locomotive
Locomotive_number=0
Locomotive=infor_item("Locomotive",Locomotive_number)

# MasterChefHat
MasterChefHat_number=0
MasterChefHat=infor_item("MasterChefHat",MasterChefHat_number)

# Helmet_32Luck_Precise
Helmet_32Luck_Precise=infor_item("Helmet_32Luck_Precise",0)

# WitlessShako_Health_Precise
WitlessShako_Health_Precise=infor_item("WitlessShako_Health_Precise",0)

# NorthWind_Luck13
NorthWind_Luck13=infor_item("NorthWind_Luck13",0)

# Vtuber_Inves198_Speed7
Vtuber_Inves198_Speed7=infor_item("Vtuber_Inves198_Speed7",0)

# Bicycle_lv3
Bicycle_lv3=infor_item("Bicycle_lv3",0)

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
        print("xuat hien ",infor_item.name)
        
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        time.sleep(0.2)
        pyautogui.click(res_center)        
        time.sleep(0.2)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def buy_item_infor(infor_item, number_item):
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
        number_buy=number_item-number
        
        for n in range(0, number_buy):
            buy = buy_item(infor_item)
            if buy is True:
                print("Bạn đã có {} cái {}".format(infor_item.number,infor_item.name))
                print("Bạn cần mua thêm {} cái {} nữa".format(number_buy,infor_item.name))
                if button.check_not_money():
                    break
                else:
                    number=number+1
                    print("Bạn đã mua thành công 1 cái {}, bạn cần mua thêm {} nữa".format(infor_item.name,number_buy-number))
                    infor_item.number=number              
def buy_ShopDiscount():
    """
    This function is used to buy all items in the ShopDiscount category.
    """
    buy_item_infor(ShopDiscount,5)

def buy_Investment_lv1_precise():
    """
    This function is used to buy all items in the Investment_lv1_precise category.
    """
    buy_item_infor(Investment_lv1_precise,5)

def buy_TomeOfKnowledge():
    """
    This function is used to buy all items in the TomeOfKnowledge category.
    """
    buy_item_infor(TomeOfKnowledge,5)

def buy_Exp20_Range5():
    """
    This function is used to buy all items in the Exp20_Range5 category.
    """
    buy_item_infor(Exp20_Range5,5)

def buy_Exp40_Luck6():
    """
    This function is used to buy all items in the Exp40_Luck6 category.
    """
    buy_item_infor(Exp40_Luck6,5)

def buy_Locomotive():
    """
    This function is used to buy all items in the Locomotive category.
    """
    buy_item_infor(Locomotive,5)

def buy_all_shop_items():
    """
    This function is used to buy all items in the shop.
    """
    buy_ShopDiscount()
    buy_Investment_lv1_precise()
    buy_TomeOfKnowledge()
    buy_Exp20_Range5()
    buy_Exp40_Luck6()
    buy_Locomotive()

def buy_all_items():
    """
    This function is used to buy all items in the game.
    """
    buy_all_shop_items()
    # buy_MasterChefHat()
    # buy_Helmet_32Luck_Precise()
    # buy_WitlessShako_Health_Precise()
    # buy_NorthWind_Luck13()
    # buy_Vtuber_Inves198_Speed7()
    # buy_Exp40_Luck6()
    # buy_Bicycle_lv3()


