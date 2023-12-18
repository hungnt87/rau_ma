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
def round_1():
    button.enter_game()
    button.check_ProceedToRound()


def round_2():
    for n in range(0, 3):
        # buy item
        item.buy_Investment_lv1_precise()
        item.buy_ShopDiscount()        
        item.buy_TomeOfKnowledge()

        # buy hero
        hero.buy_hero_infor(hero.Hoodwink, 5)
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        hero.buy_hero_infor(hero.TrollWarlord,5)

        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
    
    


def round_3():
    for n in range(0, 5):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)

        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    button.next_round()

def round_4():
    for n in range(0, 6):
        # buy item
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()


def round_5():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
def round_6():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
def round_7():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
    
def round_8():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
    
def round_9():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
    
def round_10():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_11():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_12():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_13():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
       # hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_14():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
       # hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_15():
    for n in range(0, 10):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_16():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_17():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_18():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_19():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_20():
    for n in range(0, 7):
        # buy item
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6
        
        # buy hero
        hero.buy_hero_infor(hero.Oracle, 1)
        hero.buy_hero_infor(hero.Dazzale, 1)
        hero.buy_hero_infor(hero.Hoodwink, 5)     
        hero.buy_hero_infor(hero.WinterWyvern, 4)
        #hero.buy_hero_infor(hero.TrollWarlord,5)
        hero.buy_hero_infor(hero.Clinkz,5)
        hero.buy_hero_infor(hero.DarkWillow,5)
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    


  
