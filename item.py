import pyautogui
import time


ShopDiscount = r"data\image\item\ShopDiscount.png"
number_ShopDiscount = 0

item_NotMoney = r"data\image\item\NotMoney.png"

Investment_lv1_precise = r"data\image\item\Investment_lv1_precise.png"
number_Investment_lv1_precise = 0

TomeOfKnowledge=r"data\image\item\TomeOfKnowledge.png"


def buy_item(item_img):
    try:
        res = pyautogui.locateOnScreen(
            item_img, confidence=0.8, region=(0, 0, 1916, 1134))
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        time.sleep(0.2)
        pyautogui.click(res_center)
        time.sleep(0.2)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def check_item(item_img):
    try:
        res = pyautogui.locateOnScreen(
            item_img, confidence=0.8, region=(0, 0, 1916, 1134))
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        time.sleep(0.2)
       #pyautogui.click(res_center)
        #time.sleep(0.2)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def check_money(image):
    try:
        res = pyautogui.locateOnScreen(
            image, confidence=0.8, region=(0, 0, 1916, 1134))
        # res_center = pyautogui.center(res)
        # pyautogui.moveTo(res_center)
        return True
    except pyautogui.ImageNotFoundException:
        return None


def check_not_money():
    i = 0
    while True:
        if check_money(item_NotMoney) is True:
            print("ko du tien")
            return True
        else:
            i = i+1
        if i >= 10:
            return False
            break


def buy_ShopDiscount():
    global number_ShopDiscount
    if number_ShopDiscount <= 5:
        for n in range(0, 4):
            if buy_item(ShopDiscount):
                print("Da mua ")


def buy_Investment_lv1_precise():
    global number_Investment_lv1_precise
    if number_Investment_lv1_precise <= 5:
        for n in range(0, 4):
            if buy_item(Investment_lv1_precise):
                print("Da mua ")
            print("ko co")
            
def buy_TomeOfKnowledge():  
    for n in range(0, 4):
        if buy_item(Investment_lv1_precise):
            print("Da mua TomeOfKnowledge ")
        print("ko co TomeOfKnowledge")

