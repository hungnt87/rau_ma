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
    #hero.Clinkz_number
    button.enter_game()
    button.check_ProceedToRound()


def round_2():
    for n in range(0, 3):
        # buy item
        item.buy_Investment_lv1_precise()
        item.buy_ShopDiscount()        
        #item.buy_TomeOfKnowledge()

        # buy hero
        hero.buy_Hoodwink()
        hero.buy_WinterWyvern()

        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
    
    


def round_3():
    for n in range(0, 5):
        # buy item
        print("Đang mua item lần:", n)
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        #item.buy_Vtuber_Inves198_Speed7()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        #item.buy_Exp40_Luck6()
        #item.buy_Attack16_Arcane16()
        #item.buy_Attack16_Strike16()
        # item.buy_Bicycle_lv3()
        # item.buy_Luck60_Speed25()
        item.buy_HealthRegen12_HitRecovery15()
        # item.buy_SplitTheVoid()
        # item.buy_Holding_30HealthRegen()
        #item.buy_Critical30_Defense10()
        #item.buy_MasterChefHat()
        #item.buy_Helmet_32Luck_Precise()
        # buy hero
        hero.buy_Hoodwink()
        hero.buy_WinterWyvern()
        #hero.buy_Clinkz()
        #hero.buy_DarkWillow()
        #hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    button.next_round()

def round_4():
    for n in range(0, 6):
        print("Đang mua item lần:", n)
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_Vtuber_Inves198_Speed7()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        #item.buy_Exp40_Luck6()
        #item.buy_Attack16_Arcane16()
        #item.buy_Attack16_Strike16()
        #item.buy_Bicycle_lv3()
        #item.buy_Luck60_Speed25()
        item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        # item.buy_Holding_30HealthRegen()
        #item.buy_Critical30_Defense10()
        #item.buy_MasterChefHat()
        #item.buy_Helmet_32Luck_Precise()
        # buy hero
        hero.buy_Hoodwink()
        hero.buy_WinterWyvern()
        #hero.buy_Clinkz()
        #hero.buy_DarkWillow()
        #hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()


def round_5():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_Vtuber_Inves198_Speed7()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        #item.buy_Exp40_Luck6()
        #item.buy_Attack16_Arcane16()
        #item.buy_Attack16_Strike16()
        #item.buy_Bicycle_lv3()
        #item.buy_Luck60_Speed25()
        item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        # item.buy_Holding_30HealthRegen()
        #item.buy_Critical30_Defense10()
        #item.buy_MasterChefHat()
        #item.buy_Helmet_32Luck_Precise()
        # buy hero
        hero.buy_Hoodwink()
        hero.buy_WinterWyvern()
        #hero.buy_Clinkz()
        #hero.buy_DarkWillow()
        #hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
def round_6():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        item.buy_ShopDiscount()
        item.buy_Investment_lv1_precise()
        item.buy_Vtuber_Inves198_Speed7()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6()
        item.buy_Attack16_Arcane16()
        item.buy_Attack16_Strike16()
        item.buy_Bicycle_lv3()
        item.buy_Luck60_Speed25()
        item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        #item.buy_Critical30_Defense10()
        #item.buy_MasterChefHat()
        #item.buy_Helmet_32Luck_Precise()
        # buy hero
        hero.buy_Hoodwink()
        hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        #hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
def round_7():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        #item.buy_ShopDiscount()
        #item.buy_Investment_lv1_precise()
        item.buy_Vtuber_Inves198_Speed7()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        #item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6()
        item.buy_Attack16_Arcane16()
        item.buy_Attack16_Strike16()
        item.buy_Bicycle_lv3()
        item.buy_Luck60_Speed25()
        item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        item.buy_MasterChefHat()
        item.buy_Helmet_32Luck_Precise()
        # buy hero
        hero.buy_Hoodwink()
        hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        #hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
    
def round_8():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        #item.buy_ShopDiscount()
        #item.buy_Investment_lv1_precise()
        item.buy_Vtuber_Inves198_Speed7()
        item.buy_TomeOfKnowledge()
        #item.buy_Locomotive()
        #item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6()
        item.buy_Attack16_Arcane16()
        item.buy_Attack16_Strike16()
        item.buy_Bicycle_lv3()
        item.buy_Luck60_Speed25()
        item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        item.buy_MasterChefHat()
        item.buy_Helmet_32Luck_Precise()
        # buy hero
        hero.buy_Hoodwink()
        hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        #hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
    
def round_9():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        #item.buy_ShopDiscount()
        #item.buy_Investment_lv1_precise()
        #item.buy_Vtuber_Inves198_Speed7()
        item.buy_TomeOfKnowledge()
        item.buy_Locomotive()
        #item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6()
        item.buy_Attack16_Arcane16()
        item.buy_Attack16_Strike16()
        item.buy_Bicycle_lv3()
        item.buy_Luck60_Speed25()
        item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        item.buy_MasterChefHat()
        item.buy_Helmet_32Luck_Precise()
        # buy hero
        hero.buy_Hoodwink()
        hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()
    
def round_10():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        #item.buy_ShopDiscount()
        #item.buy_Investment_lv1_precise()
        item.buy_Vtuber_Inves198_Speed7()
        #item.buy_TomeOfKnowledge()
       #item.buy_Locomotive()
        #item.buy_Exp20_Range5()
        #item.buy_Exp40_Luck6()
        item.buy_Attack16_Arcane16()
        item.buy_Attack16_Strike16()
        item.buy_Bicycle_lv3()
        item.buy_Luck60_Speed25()
        item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        item.buy_MasterChefHat()
        item.buy_Helmet_32Luck_Precise()
        # buy hero
        #hero.buy_Hoodwink()
        #hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_11():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        #item.buy_ShopDiscount()
        #item.buy_Investment_lv1_precise()
        #item.buy_Vtuber_Inves198_Speed7()
        #item.buy_TomeOfKnowledge()
        #item.buy_Locomotive()
        #item.buy_Exp20_Range5()
        #item.buy_Exp40_Luck6()
        item.buy_Attack16_Arcane16()
        item.buy_Attack16_Strike16()
        item.buy_Bicycle_lv3()
        item.buy_Luck60_Speed25()
        #item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        item.buy_MasterChefHat()
        item.buy_Helmet_32Luck_Precise()
        # buy hero
        #hero.buy_Hoodwink()
        #hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_12():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        item.buy_Vtuber_Inves198_Speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        #item.buy_Exp40_Luck6()
        item.buy_Attack16_Arcane16()
        item.buy_Attack16_Strike16()
        item.buy_Bicycle_lv3()
        item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        item.buy_MasterChefHat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_13():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        #item.buy_Vtuber_Inves198_Speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        item.buy_Exp40_Luck6()
        item.buy_Attack16_Arcane16()
        item.buy_Attack16_Strike16()
        item.buy_Bicycle_lv3()
        item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        item.buy_MasterChefHat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_14():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        # #item.buy_Vtuber_Inves198_Speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        # item.buy_Exp40_Luck6()
        item.buy_Attack16_Arcane16()
        item.buy_Attack16_Strike16()
        item.buy_Bicycle_lv3()
        item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        item.buy_MasterChefHat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_15():
    for n in range(0, 10):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        # #item.buy_Vtuber_Inves198_Speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        # #item.buy_Exp40_Luck6()
        #item.buy_Attack16_Arcane16()
        #item.buy_Attack16_Strike16()
        # item.buy_Bicycle_lv3()
        # item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        item.buy_MasterChefHat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_16():
    for n in range(0, 8):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        # #item.buy_Vtuber_Inves198_Speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        #item.buy_Exp40_Luck6()
        #item.buy_Attack16_Arcane16()
        #item.buy_Attack16_Strike16()
        # item.buy_Bicycle_lv3()
        # item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        item.buy_MasterChefHat()
        #item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_17():
    for n in range(0, 8):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        # #item.buy_Vtuber_Inves198_Speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        # #item.buy_Exp40_Luck6()
        # #item.buy_Attack16_Arcane16()
        # #item.buy_Attack16_Strike16()
        # # item.buy_Bicycle_lv3()
        # # item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        item.buy_MasterChefHat()
        #item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_18():
    for n in range(0, 9):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        # #item.buy_Vtuber_Inves198_Speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        # #item.buy_Exp40_Luck6()
        # #item.buy_Attack16_Arcane16()
        # #item.buy_Attack16_Strike16()
        # # item.buy_Bicycle_lv3()
        # # item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        #item.buy_MasterChefHat()
        #item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_19():
    for n in range(0, 9):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        # #item.buy_Vtuber_Inves198_Speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        #item.buy_Exp40_Luck6()
        #item.buy_Attack16_Arcane16()
        #item.buy_Attack16_Strike16()
        # item.buy_Bicycle_lv3()
        # item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        #item.buy_MasterChefHat()
        #item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()

def round_20():
    for n in range(0, 10):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        # #item.buy_Vtuber_Inves198_Speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        # #item.buy_Exp40_Luck6()
        # #item.buy_Attack16_Arcane16()
        # #item.buy_Attack16_Strike16()
        # # item.buy_Bicycle_lv3()
        # # item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_SplitTheVoid()
        item.buy_Holding_30HealthRegen()
        item.buy_Critical30_Defense10()
        #item.buy_MasterChefHat()
        #item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_Clinkz()
        hero.buy_DarkWillow()
        hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    hero.reset_hero()
    item.reset_item()
    button.next_round()
    time.sleep(140)
    # next round
    


  
