import pyautogui
import time
import button
import hero
import item


def click_image(image):
    i = 0
    while True:
        try:
            res = pyautogui.locateOnScreen(
                image, confidence=0.8, region=(0, 0, 1916, 1134))
            res_center = pyautogui.center(res)
            time.sleep(1)
            pyautogui.moveTo(res_center)
            pyautogui.click(res_center)
            # pyautogui.moveTo(0, 0)
            # print("I can see it")
            break
        except pyautogui.ImageNotFoundException:
            i = i+1
            if i > 120:
                break
            print(i)
            time.sleep(0.5)



def get_round(image):
    i = 0
    while True:
        try:
            res = pyautogui.locateOnScreen(
                image, confidence=0.8, region=(0, 0, 1916, 1134))
            res_center = pyautogui.center(res)
            # time.sleep(1)
            # pyautogui.moveTo(res_center)
           # pyautogui.click(res_center)
            print("I can see it")

            break
        except pyautogui.ImageNotFoundException:
            i = i+1
            if i > 120:
                break
            print(i)
            time.sleep(0.5)
def check_Resurrect(time_wait):
    i = 0
    while True:
        try:
            res = pyautogui.locateOnScreen(
                button.bt_Resurrect, confidence=0.8, region=(0, 0, 1916, 1134))
            res_center = pyautogui.center(res)
            time.sleep(1)
            pyautogui.moveTo(res_center)
            pyautogui.click(res_center)
            print("Chon Resurrect ")
            
            for x in range(0,time_wait):
                print(" cho van dau", x)
                time.sleep(1)
            break
        except pyautogui.ImageNotFoundException:
            i = i+1
            if i > time_wait:
                break
            print("cho xuat hien Resurrect",i)
            time.sleep(1)



def round_1():
    click_image(button.bt_CreateCustomLobby)
    click_image(button.bt_ServerLocaltion)
    click_image(button.bt_ServerLocaltion_Singapore)
    click_image(button.bt_CreatePassLobby)
    pyautogui.write("as")  # add password
    click_image(button.bt_CreateGame)
    # time.sleep(4)
    click_image(button.bt_StartGame)
    click_image(button.bt_Accept)  # start game
    click_image(button.bt_Confirm)
    click_image(button.bt_Challenge)
    click_image(button.bt_SelectCharacter)
    pyautogui.moveTo(100, 100)
    click_image(button.bt_Prepare)
    check_Resurrect(30)
    

def round_2():
    for n in range(0, 2):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()

        # buy hero
        hero.buy_hero_infor(hero.Hoodwink,5)
        hero.buy_hero_infor(hero.PriestArcane,1)
        hero.buy_hero_infor(hero.WinterWyvern,4)      

        # roll
        click_image(button.bt_Roll)
        pyautogui.moveTo(200, 200)
    # next round
    click_image(button.bt_ProceedToRound2)
    check_Resurrect(40)
def round_3():
    for n in range(0, 4):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()

        # buy hero
        hero.buy_hero_Luna(1)

        # roll
        click_image(button.bt_Roll)
        pyautogui.moveTo(200, 200)
    # next round
    click_image(button.bt_ProceedToRound3)
    check_Resurrect(45)
def round_4():    
    for n in range(0, 5):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()

        # buy hero
        hero.buy_hero_Luna(1)
        hero.buy_hero_Windranger(1)
        # roll
        click_image(button.bt_Roll)
        pyautogui.moveTo(200, 200)
    # next round
    click_image(button.bt_ProceedToRound4)
    check_Resurrect(50)
def round_5():

    for n in range(0, 6):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()

        # buy hero
        hero.buy_hero_Luna(1)
        hero.buy_hero_Windranger(1)
        # roll
        click_image(button.bt_Roll)
        pyautogui.moveTo(200, 200)
    # next round
    click_image(button.bt_ProceedToRound5)
    check_Resurrect(55)
    
