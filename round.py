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
                button.Resurrect.img, confidence=0.8, region=(0, 0, 1916, 1134))
            res_center = pyautogui.center(res)
            time.sleep(1)
            pyautogui.moveTo(res_center)
            pyautogui.click(res_center)
            print("Chon Resurrect ")

            for x in range(0, time_wait):
                print(" cho van dau", x)
                time.sleep(1)
            break
        except pyautogui.ImageNotFoundException:
            i = i+1
            if i > time_wait:
                break
            print("cho xuat hien Resurrect", i)
            time.sleep(1)


def round_1():
    button.enter_game()
    check_Resurrect(30)


def round_2():
    for n in range(0, 3):
        # buy item
        item.buy_Investment_lv1_precise()
        item.buy_ShopDiscount()
        
        item.buy_TomeOfKnowledge()

        # buy hero
        hero.buy_hero_infor(hero.Hoodwink, 5)
        hero.buy_hero_infor(hero.PriestArcane, 1)
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        hero.buy_hero_infor(hero.TrollWarlord,5)

        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round_2()
    check_Resurrect(35)


def round_3():
    for n in range(0, 5):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        # buy hero
        hero.buy_hero_infor(hero.Hoodwink, 5)
        hero.buy_hero_infor(hero.PriestArcane, 1)
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        hero.buy_hero_infor(hero.TrollWarlord,5)

        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round_3()
    check_Resurrect(40)


def round_4():
    for n in range(0, 6):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()

        # buy hero
        hero.buy_hero_infor(hero.Hoodwink, 5)
        hero.buy_hero_infor(hero.PriestArcane, 1)
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        hero.buy_hero_infor(hero.TrollWarlord,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round_5()
    check_Resurrect(45)


def round_5():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()

        # buy hero
        hero.buy_hero_infor(hero.Hoodwink, 5)
        hero.buy_hero_infor(hero.PriestArcane, 1)
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        hero.buy_hero_infor(hero.TrollWarlord,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    # button.next_round_6()
    # check_Resurrect(55)
    button.exit_game()
