import pyautogui
import time
import button

class infor_item:
     def __init__(self,para_name,para_item_number):
         self.name= para_name
         self.img="data\\image\\item\\"+para_name+".png"
         self.number=para_item_number

number_ShopDiscount = 0
ShopDiscount=infor_item("ShopDiscount",number_ShopDiscount)


#NotMoney = infor_item("NotMoney",0)
number_Investment_lv1_precise = 0
Investment_lv1_precise = infor_item("Investment_lv1_precise",number_Investment_lv1_precise)

TomeOfKnowledg_number=0
TomeOfKnowledge=infor_item("TomeOfKnowledge",TomeOfKnowledg_number)


def buy_item(infor_item):
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

# def check_item(item_img):
#     try:
#         res = pyautogui.locateOnScreen(
#             item_img, confidence=0.8, region=(0, 0, 1916, 1134))
#         res_center = pyautogui.center(res)
#         pyautogui.moveTo(res_center)
#         time.sleep(0.2)
#        #pyautogui.click(res_center)
#         #time.sleep(0.2)
#         return True
#     except pyautogui.ImageNotFoundException:
#         return False

# def check_money(image):
#     try:
#         res = pyautogui.locateOnScreen(
#             image, confidence=0.8, region=(0, 0, 1916, 1134))
#         # res_center = pyautogui.center(res)
#         # pyautogui.moveTo(res_center)
#         return True
#     except pyautogui.ImageNotFoundException:
#         return None


# def check_not_money():
#     i = 0
#     while True:
#         if check_money(item_NotMoney) is True:
#             print("ko du tien")
#             return True
#         else:
#             i = i+1
#         if i >= 10:
#             return False
#             break


# def buy_ShopDiscount(item_number):
#     global number_ShopDiscount
#     if number_ShopDiscount <= 5:
#         for n in range(0, 4):
#             if buy_item(ShopDiscount.name):
#                 print("Da mua ")
def buy_item_infor(infor_item, number_item):
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
    buy_item_infor(ShopDiscount,5)

def buy_Investment_lv1_precise():
    buy_item_infor(Investment_lv1_precise,5)
            
def buy_TomeOfKnowledge():  
    buy_item_infor(TomeOfKnowledge,5)

