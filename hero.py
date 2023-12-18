import pyautogui
import time
import button


class infor_hero:
    def __init__(self, para_name, para_number_hero):
        self.name = para_name
        self.img = "data\\image\\hero\\"+para_name+".png"
        self.lv1_img = "data\\image\\hero\\"+para_name+"_lv1.png"
        self.lv2_img = "data\\image\\hero\\"+para_name+"_lv2.png"
        self.lv3_img = "data\\image\\hero\\"+para_name+"_lv3.png"
        self.lv4_img = "data\\image\\hero\\"+para_name+"_lv4.png"
        self.lv5_img = "data\\image\\hero\\"+para_name+"_lv5.png"
        self.number = para_number_hero


# hero lv1
WinterWyvern_number = 1
WinterWyvern = infor_hero("WinterWyvern", WinterWyvern_number)
Hoodwink_number = 0
Hoodwink = infor_hero("Hoodwink", Hoodwink_number)

# hero lv2
Luna_number = 0
Luna = infor_hero("Luna", Luna_number)
Windranger_number = 0
Windranger = infor_hero("Windranger", Windranger_number)
Oracle_number = 0
Oracle = infor_hero("Oracle", Oracle_number)
TrollWarlord_number = 0
TrollWarlord = infor_hero("TrollWarlord", TrollWarlord_number)
Dazzale_number = 0
Dazzale = infor_hero("Dazzale", Dazzale_number)
DarkWillow_number = 0
DarkWillow = infor_hero("DarkWillow", DarkWillow_number)
Clinkz_number = 0
Clinkz = infor_hero("Clinkz", Clinkz_number)

# def get_hero_level(infor_hero):
#     try:

#         res = pyautogui.locateOnScreen(
#             infor_hero.lv1_img, confidence=0.8, region=(0, 0, 1916, 1134))
#         return 1
#     except pyautogui.ImageNotFoundException:
#         return 0


def buy_hero(hero_img):
    try:
        res = pyautogui.locateOnScreen(
            hero_img, confidence=0.8, region=(0, 0, 1916, 1134))
        res_center = pyautogui.center(res)
        pyautogui.moveTo(res_center)
        time.sleep(0.2)
        pyautogui.click(res_center)
        time.sleep(0.2)
        return True
    except pyautogui.ImageNotFoundException:
        return None


def buy_hero_infor(infor_hero, number_hero):
    i=0       
    while True:
        if i>=4:
            break
        number = infor_hero.number 
        if number_hero > number:
            i=i+1
            number_buy = number_hero-number
            # print("Bạn đã có {} hero {}".format(
            #         infor_hero.number, infor_hero.name))
            # print("Bạn cần mua thêm {} hero {} nữa".format(
            #         number_buy, infor_hero.name))
                    
            if buy_hero(infor_hero.img) is True:
                if button.check_not_money():
                    break
                else:
                    number = number+1
                    
                    infor_hero.number = number
                    print("Bạn đã mua thành công 1 hero {}, bạn đang có {}, bạn cần mua thêm {} nữa".format(
                        infor_hero.name,infor_hero.number, number_hero-number))

            
        else:
            print("ban da du hero roi, ko can mua nua")
            break            


# def buy_hero_Windranger(hero_number):
#     global number_hero_Windranger
#     print("Windranger: ", number_hero_Windranger)
#     while True:
#         if get_hero_level(Windranger) is True:
#             number_hero_Windranger = 1
#             break
#         break
#     if hero_number > number_hero_Windranger:
#         for n in range(0, 4):
#             buy = buy_hero(Windranger)
#             if buy is True:
#                 number_hero_Windranger = number_hero_Windranger+1
#                 print("mua: ", number_hero_Windranger)
#                 if hero_number <= number_hero_Windranger:
#                     break
