import pyautogui
import time
import button
import hero
import item


def round_1():
    # hero.Clinkz_number
    button.enter_game()
    button.check_proceed_to_round()


def round_2():
    for n in range(0, 3):
        # buy item
        item.buy_investment_lv1_precise()
        item.buy_shop_discount()
        # item.buy_TomeOfKnowledge()

        # buy hero
        hero.buy_hoodwink()
        hero.buy_winter_wyvern()

        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()


def round_3():
    for n in range(0, 5):
        # buy item
        print("Đang mua item lần:", n)
        item.buy_shop_discount()
        item.buy_investment_lv1_precise()
        # item.buy_Vtuber_Inves198_Speed7()
        item.buy_tome_of_knowledge()
        item.buy_locomotive()
        item.buy_exp20_range5()
        # item.buy_Exp40_Luck6()
        # item.buy_Attack16_Arcane16()
        # item.buy_Attack16_Strike16()
        # item.buy_Bicycle_lv3()
        # item.buy_Luck60_Speed25()
        item.buy_health_regen12_hit_recovery15()
        # item.buy_SplitTheVoid()
        # item.buy_Holding_30HealthRegen()
        # item.buy_Critical30_Defense10()
        # item.buy_MasterChefHat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        hero.buy_hoodwink()
        hero.buy_winter_wyvern()
        # hero.buy_Clinkz()
        # hero.buy_DarkWillow()
        # hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    button.next_round()


def round_4():
    for n in range(0, 6):
        print("Đang mua item lần:", n)
        item.buy_shop_discount()
        item.buy_investment_lv1_precise()
        item.buy_vtuber_inves198_speed7()
        item.buy_tome_of_knowledge()
        item.buy_locomotive()
        item.buy_exp20_range5()
        # item.buy_Exp40_Luck6()
        # item.buy_Attack16_Arcane16()
        # item.buy_Attack16_Strike16()
        # item.buy_Bicycle_lv3()
        # item.buy_Luck60_Speed25()
        item.buy_health_regen12_hit_recovery15()
        item.buy_split_the_void()
        # item.buy_Holding_30HealthRegen()
        # item.buy_Critical30_Defense10()
        # item.buy_MasterChefHat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        hero.buy_hoodwink()
        hero.buy_winter_wyvern()
        # hero.buy_Clinkz()
        # hero.buy_DarkWillow()
        # hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()


def round_5():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        item.buy_shop_discount()
        item.buy_investment_lv1_precise()
        item.buy_vtuber_inves198_speed7()
        item.buy_tome_of_knowledge()
        item.buy_locomotive()
        item.buy_exp20_range5()
        # item.buy_Exp40_Luck6()
        # item.buy_Attack16_Arcane16()
        # item.buy_Attack16_Strike16()
        # item.buy_Bicycle_lv3()
        # item.buy_Luck60_Speed25()
        item.buy_health_regen12_hit_recovery15()
        item.buy_split_the_void()
        # item.buy_Holding_30HealthRegen()
        # item.buy_Critical30_Defense10()
        # item.buy_MasterChefHat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        hero.buy_hoodwink()
        hero.buy_winter_wyvern()
        # hero.buy_Clinkz()
        # hero.buy_DarkWillow()
        # hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()


def round_6():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        item.buy_shop_discount()
        item.buy_investment_lv1_precise()
        item.buy_vtuber_inves198_speed7()
        item.buy_tome_of_knowledge()
        item.buy_locomotive()
        item.buy_exp20_range5()
        item.buy_exp40_luck6()
        item.buy_attack16_arcane16()
        item.buy_attack16_strike16()
        item.buy_bicycle_lv3()
        item.buy_luck60_speed25()
        item.buy_health_regen12_hit_recovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        # item.buy_Critical30_Defense10()
        # item.buy_MasterChefHat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        hero.buy_hoodwink()
        hero.buy_winter_wyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        # hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()


def round_7():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        item.buy_vtuber_inves198_speed7()
        item.buy_tome_of_knowledge()
        item.buy_locomotive()
        # item.buy_Exp20_Range5()
        item.buy_exp40_luck6()
        item.buy_attack16_arcane16()
        item.buy_attack16_strike16()
        item.buy_bicycle_lv3()
        item.buy_luck60_speed25()
        item.buy_health_regen12_hit_recovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        item.buy_master_chef_hat()
        item.buy_helmet_32_luck_precise()
        # buy hero
        hero.buy_hoodwink()
        hero.buy_winter_wyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        # hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()


def round_8():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        item.buy_vtuber_inves198_speed7()
        item.buy_tome_of_knowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        item.buy_exp40_luck6()
        item.buy_attack16_arcane16()
        item.buy_attack16_strike16()
        item.buy_bicycle_lv3()
        item.buy_luck60_speed25()
        item.buy_health_regen12_hit_recovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        item.buy_master_chef_hat()
        item.buy_helmet_32_luck_precise()
        # buy hero
        hero.buy_hoodwink()
        hero.buy_winter_wyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        # hero.buy_Sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()


def round_9():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        # item.buy_Vtuber_Inves198_Speed7()
        item.buy_tome_of_knowledge()
        item.buy_locomotive()
        # item.buy_Exp20_Range5()
        item.buy_exp40_luck6()
        item.buy_attack16_arcane16()
        item.buy_attack16_strike16()
        item.buy_bicycle_lv3()
        item.buy_luck60_speed25()
        item.buy_health_regen12_hit_recovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        item.buy_master_chef_hat()
        item.buy_helmet_32_luck_precise()
        # buy hero
        hero.buy_hoodwink()
        hero.buy_winter_wyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()


def round_10():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        item.buy_vtuber_inves198_speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        # item.buy_Exp40_Luck6()
        item.buy_attack16_arcane16()
        item.buy_attack16_strike16()
        item.buy_bicycle_lv3()
        item.buy_luck60_speed25()
        item.buy_health_regen12_hit_recovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        item.buy_master_chef_hat()
        item.buy_helmet_32_luck_precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    # next round
    button.next_round()


def round_11():
    for n in range(0, 7):
        # buy item
        print("Đang mua item lần:", n)
        # item.buy_ShopDiscount()
        # item.buy_Investment_lv1_precise()
        # item.buy_Vtuber_Inves198_Speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        # item.buy_Exp40_Luck6()
        item.buy_attack16_arcane16()
        item.buy_attack16_strike16()
        item.buy_bicycle_lv3()
        item.buy_luck60_speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        item.buy_master_chef_hat()
        item.buy_helmet_32_luck_precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
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
        item.buy_vtuber_inves198_speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        # item.buy_Exp40_Luck6()
        item.buy_attack16_arcane16()
        item.buy_attack16_strike16()
        item.buy_bicycle_lv3()
        item.buy_luck60_speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        item.buy_master_chef_hat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
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
        # item.buy_Vtuber_Inves198_Speed7()
        # item.buy_TomeOfKnowledge()
        # item.buy_Locomotive()
        # item.buy_Exp20_Range5()
        item.buy_exp40_luck6()
        item.buy_attack16_arcane16()
        item.buy_attack16_strike16()
        item.buy_bicycle_lv3()
        item.buy_luck60_speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        item.buy_master_chef_hat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
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
        item.buy_attack16_arcane16()
        item.buy_attack16_strike16()
        item.buy_bicycle_lv3()
        item.buy_luck60_speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        item.buy_master_chef_hat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
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
        # item.buy_Attack16_Arcane16()
        # item.buy_Attack16_Strike16()
        # item.buy_Bicycle_lv3()
        # item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        item.buy_master_chef_hat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
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
        # item.buy_Exp40_Luck6()
        # item.buy_Attack16_Arcane16()
        # item.buy_Attack16_Strike16()
        # item.buy_Bicycle_lv3()
        # item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        item.buy_master_chef_hat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
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
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        item.buy_master_chef_hat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
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
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        # item.buy_MasterChefHat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
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
        # item.buy_Exp40_Luck6()
        # item.buy_Attack16_Arcane16()
        # item.buy_Attack16_Strike16()
        # item.buy_Bicycle_lv3()
        # item.buy_Luck60_Speed25()
        # item.buy_HealthRegen12_HitRecovery15()
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        # item.buy_MasterChefHat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
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
        item.buy_split_the_void()
        item.buy_holding_30_health_regen()
        item.buy_critical30_defense10()
        # item.buy_MasterChefHat()
        # item.buy_Helmet_32Luck_Precise()
        # buy hero
        # hero.buy_Hoodwink()
        # hero.buy_WinterWyvern()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        # roll
        button.roll_game()
        pyautogui.moveTo(200, 200)
    hero.reset_hero()
    item.reset_item()
    button.click_procceed_to_round()
    time.sleep(140)
    # next round
