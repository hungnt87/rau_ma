import pyautogui
import time


import item
from controller.filelog import logger
import controller.global_variables as cgv
from controller.button import Button
import controller.hero as hero

event = cgv.Event()
event_stop = cgv.event_stop
event_pause = cgv.event_pause


# hero.hero_status_money
# item.item_status_money
def get_count_buy():
    count = cgv.get_count_of_buy()
    return count


def reset_count_buy():
    cgv.reset_count_of_buy()
    # item.reset_count_buy_item()


def round_all(round_number=1, stop_event=event_stop, pause_event=event_pause):
    if event.check_event():
        # logger.info("Stop thread round 1")
        return False
    n = 0
    while n < 20:
        if event.check_event():
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
            if Button.enter_game() is False:
                break
            if Button.run_round() is False:
                break
        else:
            # reset_count_buy()
            # reset_status_not_money()
            cgv.reset_count_of_buy()
            cgv.set_money(True)

            while True:
                if event.check_event():
                    # logger.info("Stop thread round 3")
                    break
                if cgv.check_money() is False:
                    break
                if number_roll > 0:
                    if Button.roll_game() is False:
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
                logger.debug(f"Da roll {number_roll} lan")
                logger.debug(f"Da mua {cgv.get_count_of_buy()} lan")
                if cgv.check_money() is False:
                    break
                if cgv.get_count_of_buy() >= number_buy:
                    break
                if number_roll >= number_buy + 2:
                    break

            if n < 20:
                if Button.next_round() is False:
                    break
                if Button.run_round() is False:
                    break
                logger.info(f"Day la vong auto lan thu {round_number}, round {n}")
            else:
                # reset_count_buy()
                cgv.reset_count_of_buy()
                cgv.set_money(True)
                hero.reset_hero()
                hero.reset_previous_hero()
                item.reset_item()
                item.reset_previous_item()
                if Button.exit_round20() is False:
                    break
                for s in range(50):
                    if event.check_event():
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
