import pyautogui
import time
import button
import hero
import item
from datetime import datetime
from log import logger
import threading
import controller.global_variables as cgv

gv = cgv.Global_variables()
event_stop = cgv.event_stop
event_pause = cgv.event_pause


# hero.hero_status_money
# item.item_status_money
def get_count_buy():
    count = hero.get_count_buy_hero() + item.get_count_buy_item()
    return count


def reset_count_buy():
    hero.reset_count_buy_hero()
    item.reset_count_buy_item()


def get_status_not_money():
    # global hero.hero_status_money, item.item_status_money
    if button.get_status_not_money() is True:
        # logger.debug("Du tien")
        return True
    else:
        # logger.debug("Khong du tien")
        return False


def reset_status_not_money():
    button.set_status_not_money(False)


def round_all(round_number=1, stop_event=event_stop, pause_event=event_pause):
    if gv.check_event():
        # logger.info("Stop thread round 1")
        return False
    n = 0
    while True:
        if gv.check_event():
            # logger.info("Stop thread round 2")
            break
        n = n + 1
        logger.info(f"Bat dau roll in round: {n}")
        time.sleep(1)
        number_roll = 0

        if n == 2:
            number_buy = 4
        elif n <= 4:
            number_buy = 4
        elif n <= 6:
            number_buy = 6
        elif n <= 8:
            number_buy = 7
        elif n <= 15:
            number_buy = 9
        else:
            number_buy = 9
        if n == 1:
            # button.click(button.CreateCustomLobby)
            if button.enter_game() is False:
                break
            if button.check_proceed_to_round() is False:
                break
        else:
            reset_count_buy()
            reset_status_not_money()
            while True:
                if gv.check_event():
                    # logger.info("Stop thread round 3")
                    break
                if get_status_not_money() is True:
                    break
                if number_roll > 0:
                    if button.roll_game() is False:
                        break
                number_roll += 1
                if hero.buy_all_previous_hero() is False:
                    break
                if item.buy_all_previous_item() is False:
                    break
                if hero.buy_all_hero(round_number=n) is False:
                    break
                if item.buy_all_item_investments(round_number=n) is False:
                    break
                if item.buy_all_set_item(round_number=n) is False:
                    break
                if item.buy_all_item(round_number=n) is False:
                    break
                if get_status_not_money() is True:
                    break
                if get_count_buy() >= number_buy:
                    break
                if number_roll >= number_buy + 2:
                    break

            if n < 20:
                if button.next_round() is False:
                    break
                logger.info(f"Day la vong auto lan thu {round_number}, round {n}")
            else:
                hero.reset_hero()
                hero.reset_previous_hero()
                item.reset_item()
                item.reset_previous_item()
                if button.click_procceed_to_round() is False:
                    break
                for s in range(50):
                    if gv.check_event():
                        # logger.info("Stop thread round 3")
                        break
                    s = 50 - s
                    time.sleep(1)
                    logger.info(
                        f"Ban dang danh boss round {n}, thoi gian con lai {s}/50s"
                    )
                logger.info(f"Ket thuc round {n}")
                # time.sleep(130)


if __name__ == "__main__":
    pass
