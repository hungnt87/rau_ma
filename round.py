import pyautogui
import time
import button
import hero
import item
from datetime import datetime
from log import logger
import threading

event_stop = threading.Event()
event_pause = threading.Event()


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


def set_event_run():
    global event_stop
    event_stop.clear()
    event_pause.set()
    item.set_event_run()
    button.set_event_run()


def set_event_stop():
    global event_stop
    event_stop.set()
    event_pause.set()
    item.set_event_stop()
    button.set_event_stop()


def set_event_pause():
    global event_pause
    event_pause.clear()
    item.set_event_pause()
    button.set_event_pause()


def set_event_resume():
    global event_pause
    event_pause.set()
    item.set_event_resume()
    button.set_event_resume()


def check_event():
    global event_stop, event_pause
    if event_stop.is_set():
        logger.info("Stop thread round 3")
        return False
    event_pause.wait()
    return True


def round_all(round_number=1, stop_event=event_stop, pause_event=event_pause):
    if stop_event.is_set():
        logger.info("Stop thread round 1")
        return
    n = 0
    while True:
        if check_event() is False:
            break
        n = n + 1
        logger.info(f"Bat dau roll in round: {n}")

        # button.click(button.CreateCustomLobby)
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
            button.enter_game()
            if stop_event.is_set():
                logger.info("Stop thread round enter game")
                break
            button.check_proceed_to_round()
            if stop_event.is_set():
                logger.info("Stop thread round check proceed to round")
                break
        else:
            reset_count_buy()
            reset_status_not_money()
        while True:
            if get_status_not_money() is True:
                break
            if number_roll > 0:
                if button.roll_game() is False:
                    break
            number_roll += 1
            hero.buy_all_previous_hero()
            item.buy_all_previous_item()
            hero.buy_all_hero(round_number=n)
            item.buy_all_item_investments(round_number=n)
            item.buy_all_set_item(round_number=n)
            item.buy_all_item(round_number=n)
            if get_status_not_money() is True:
                break
            if get_count_buy() >= number_buy:
                break
            if number_roll >= number_buy + 2:
                break

        if n < 20:
            button.next_round()
            logger.info(f"Day la vong auto lan thu {round_number+1}, round {n}")
        else:
            hero.reset_hero()
            hero.reset_previous_hero()
            item.reset_item()
            item.reset_previous_item()
            button.click_procceed_to_round()
            for s in range(120):
                if event.is_set():
                    logger.info("Stop thread round")
                    break
                s = 120 - s
                time.sleep(1)
                logger.info(f"Ban dang danh boss round {n}, thoi gian con lai {s}/120")
            logger.info(f"Ket thuc round {n}")
            # time.sleep(130)


if __name__ == "__main__":
    pass
