import pyautogui
import time
import button
import hero
import item
from datetime import datetime
from log import logger


def get_count_buy():
    count = hero.get_count_buy_hero() + item.get_count_buy_item()
    return count


def reset_count_buy():
    hero.reset_count_buy_hero()
    item.reset_count_buy_item()


def round_all(round_number):
    n = 0
    while n < 20:
        n = n+1
        logger.info(f"Bat dau roll in round: {n}")
        number_roll = 0

        if n == 2:
            number_buy = 2
        elif n <= 4:
            number_buy = 3
        elif n <= 6:
            number_buy = 4
        elif n <= 8:
            number_buy = 4
        elif n <= 15:
            number_buy = 5
        else:
            number_buy = 5
        if n == 1:
            button.enter_game()
            button.check_proceed_to_round()
        else:
            reset_count_buy()
            while True:
                if number_roll > 0:
                    button.roll_game()
                number_roll += 1
                hero.buy_all_hero(round_number=n)
                item.buy_all_item_investments(round_number=n)
                item.buy_all_set_item(round_number=n)
                item.buy_all_item(round_number=n)
                if get_count_buy() >= number_buy:
                    break
                if number_roll >= number_buy+2:
                    break

            if n < 20:
                button.next_round()
                logger.info(
                    f"Day la vong auto lan thu {round_number}, round thu {n}")
            else:
                hero.reset_hero()
                item.reset_item()
                button.click_procceed_to_round()
                time.sleep(130)
                logger.info(f"Ket thuc round {n}")
