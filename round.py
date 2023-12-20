import pyautogui
import time
import button
import hero
import item


def get_count_buy():
    count = hero.get_count_buy_hero() + item.get_count_buy_item()
    return count


def reset_count_buy():
    hero.reset_count_buy_hero()
    item.reset_count_buy_item()


def round_1():
    # hero.Clinkz_number

    button.enter_game()
    button.check_proceed_to_round()


def round_2():
    number_roll = 0
    number_buy = 3
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero
        hero.buy_hoodwink()
        hero.buy_dazzale()
        hero.buy_oracle()
        # buy item
        item.buy_all_item_round2()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy:
            continue
        break

    # next round
    button.next_round()


def round_3():
    number_roll = 0
    number_buy = 3
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero
        hero.buy_hoodwink()
        hero.buy_dazzale()
        hero.buy_oracle()
        # buy item
        item.buy_all_item_round3()
        
        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy+1:
            continue
        break

    # next round
    button.next_round()


def round_4():
    number_roll = 0
    number_buy = 4
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero
        hero.buy_hoodwink()
        hero.buy_dazzale()
        hero.buy_oracle()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        # buy item
        item.buy_all_item_lv1()
        item.buy_all_item_lv2()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break
        # roll

        if number_roll <= number_buy+1:
            continue
        break

    # next round
    button.next_round()


def round_5():
    number_roll = 0
    number_buy = 4
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        #buy hero
        hero.buy_hoodwink()
        hero.buy_dazzale()
        hero.buy_oracle()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        # buy item
        item.buy_all_item_lv1()
        item.buy_all_item_lv2()
        item.buy_all_item_lv3()


        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break
        # roll

        if number_roll <= number_buy+2:
            continue
        break

    # next round
    button.next_round()


def round_6():
    number_roll = 0
    number_buy = 4
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        hero.buy_hoodwink()
        hero.buy_dazzale()
        hero.buy_oracle()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        # buy item
        item.buy_all_item_lv1()
        item.buy_all_item_lv2()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy+2:
            continue
        break

    # next round
    button.next_round()


def round_7():
    number_roll = 0
    number_buy = 4
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero
        hero.buy_hoodwink()
        hero.buy_dazzale()
        hero.buy_oracle()
        hero.buy_clinkz()
        hero.buy_dark_willow()
        # buy item
        item.buy_all_item_lv1()
        item.buy_all_item_lv2()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy+2:
            continue
        break

    # next round
    button.next_round()


def round_8():
    number_roll = 0
    number_buy = 4
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)

        # buy hero

        hero.buy_clinkz()
        hero.buy_dazzale()
        hero.buy_oracle()
        hero.buy_dark_willow()
        hero.buy_sniper()
        # buy item

        item.buy_all_item_lv1()
        item.buy_all_item_lv2()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy:
            continue
        break

    # next round
    button.next_round()


def round_9():
    number_roll = 0
    number_buy = 5
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero

        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        # buy item

        item.buy_all_item_lv1()
        item.buy_all_item_lv2()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy + 2:
            continue
        break

    # next round
    button.next_round()


def round_10():
    number_roll = 0
    number_buy = 5
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero

        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        # buy item

        #item.buy_all_item_lv1()
        item.buy_all_item_lv2()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy + 2:
            continue
        break

    # next round
    button.next_round()


def round_11():
    number_roll = 0
    number_buy = 5
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero

        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        # buy item

        #item.buy_all_item_lv1()
        #item.buy_all_item_lv2()
        item.buy_all_item_lv4()
        item.buy_all_item_lv3()
        

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break
       
        if number_roll <= number_buy + 2:
            continue
        break

    # next round
    button.next_round()


def round_12():
    number_roll = 0
    number_buy = 4
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero

        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        # buy item

        item.buy_all_item_lv5()
        item.buy_all_item_lv4()
        item.buy_all_item_lv3()
        
        

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy + 2:
            continue
        break

    # next round
    button.next_round()


def round_13():
    number_roll = 0
    number_buy = 4
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        # buy item
        item.buy_all_item_lv5()
        item.buy_all_item_lv4()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy + 2:
            continue
        break

    # next round
    button.next_round()


def round_14():
    number_roll = 0
    number_buy = 4
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        #buy hero
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        hero.buy_templar_assassin()
        hero.buy_drow_ranger()
        hero.buy_zet()
        # buy item
        item.buy_all_item_lv6()
        item.buy_all_item_lv5()
        item.buy_all_item_lv4()
        item.buy_all_item_lv3()


        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy + 2:
            continue
        break

    # next round
    button.next_round()


def round_15():
    number_roll = 0
    number_buy = 5
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        hero.buy_templar_assassin()
        hero.buy_drow_ranger()
        hero.buy_zet()
        # buy item

        item.buy_all_item_lv3()
        item.buy_all_item_lv4()
        item.buy_all_item_lv5()
        item.buy_all_item_lv6()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy + 1:
            continue
        break

    # next round
    button.next_round()


def round_16():
    number_roll = 0
    number_buy = 5
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        hero.buy_templar_assassin()
        hero.buy_drow_ranger()
        hero.buy_zet()
        # buy item

        item.buy_all_item_lv6()
        item.buy_all_item_lv5()
        item.buy_all_item_lv4()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy + 1:
            continue
        break

    # next round
    button.next_round()


def round_17():
    number_roll = 0
    number_buy = 5
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        hero.buy_templar_assassin()
        hero.buy_drow_ranger()
        hero.buy_zet()
        # buy item

        item.buy_all_item_lv6()
        item.buy_all_item_lv5()
        item.buy_all_item_lv4()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy + 1:
            continue
        break

    # next round
    button.next_round()


def round_18():
    number_roll = 0
    number_buy = 5
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        hero.buy_templar_assassin()
        hero.buy_drow_ranger()
        hero.buy_zet()
        # buy item

        item.buy_all_item_lv6()
        item.buy_all_item_lv5()
        item.buy_all_item_lv4()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy + 1:
            continue
        break

    # next round
    button.next_round()


def round_19():
    number_roll = 0
    number_buy = 5
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        hero.buy_templar_assassin()
        hero.buy_drow_ranger()
        hero.buy_zet()
        # buy item

        item.buy_all_item_lv6()
        item.buy_all_item_lv5()
        item.buy_all_item_lv4()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy + 1:
            continue
        break

    # next round
    button.next_round()


def round_20():
    number_roll = 0
    number_buy = 5
    reset_count_buy()
    while True:
        if number_roll > 0:
            button.roll_game()
            pyautogui.moveTo(200, 200)
        # buy hero
        hero.buy_clinkz()
        hero.buy_dark_willow()
        hero.buy_sniper()
        hero.buy_templar_assassin()
        hero.buy_drow_ranger()
        hero.buy_zet()
        # buy item

        item.buy_all_item_lv6()
        item.buy_all_item_lv5()
        item.buy_all_item_lv4()
        item.buy_all_item_lv3()

        number_roll = number_roll + 1
        if get_count_buy() >= number_buy:
            break

        if number_roll <= number_buy + 1:
            continue
        break

    # next round
    #button.next_round()
    hero.reset_hero()
    item.reset_item()
    button.click_procceed_to_round()
    time.sleep(130)
    # next round
