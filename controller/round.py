import threading
import time

import controller.global_variables as cgv
import controller.hero as hero
import controller.item as item
from controller.button import Button
from controller.filelog import logger
from controller.global_variables import character_moves_event, global_event


def round_all(auto_number=1):
    if global_event.check_event():
        # logger.info("Stop thread round 1")
        return False
    round_number = 0
    hero.reset_hero()
    hero.reset_previous_hero()
    item.reset_item()
    item.reset_previous_item()
    while round_number < 20:
        if global_event.check_event():
            # logger.info("Stop thread round 2")
            break
        round_number = round_number + 1
        logger.info(f"Bat dau roll in round: {round_number}")
        time.sleep(1)
        number_roll = 0
        cgv.reset_count_of_buy()
        cgv.set_money(True)

        if round_number == 2:
            number_buy = 4
        elif round_number <= 4:
            number_buy = 4
        elif round_number <= 6:
            number_buy = 6
        elif round_number <= 8:
            number_buy = 7
        elif round_number <= 15:
            number_buy = 9
        else:
            number_buy = 9
        if round_number == 1:
            # button.click(button.CreateCustomLobby)
            if Button.enter_game() is False:
                break
            if Button.run_round(round_number=round_number) is False:
                break
        else:
            while True:
                if global_event.check_event():
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
                hero.buy_all_hero(round_number=round_number)
                item.buy_all_item(round_number=round_number)

                if hero.buy_all_previous_hero() is False:
                    break
                if item.buy_all_previous_item() is False:
                    break
                logger.debug(f"Da roll: {number_roll} lan")
                logger.debug(f"Da mua: {cgv.get_count_of_buy()} lan")
                if cgv.check_money() is False:
                    break
                if cgv.get_count_of_buy() >= number_buy:
                    break
                if number_roll >= number_buy + 2:
                    break

            if round_number < 20:
                if Button.next_round() is False:
                    break
                if Button.run_round(round_number=round_number) is False:
                    break
                logger.info(
                    f"Day la round: {round_number}, auto lan thu: {auto_number}"
                )
            else:
                if Button.exit_round20() is False:
                    break
                t1 = threading.Thread(target=attack_boss, args=())
                t2 = threading.Thread(
                    target=Button.character_moves, args=(round_number,)
                )
                t1.start()
                t2.start()
                t1.join()
                t2.join()

                logger.info(
                    f"Ket thuc round: {round_number} auto lan thu: {auto_number}"
                )


def attack_boss():
    character_moves_event.app_start()
    character_moves_event.app_pause()
    time_wait = 120
    for s in range(time_wait):
        if global_event.check_event():
            # logger.info("Stop thread round 3")
            break
        if s == 3:
            character_moves_event.app_resume()
        if s == 70:
            character_moves_event.app_stop()

        global_event.sleep(1)
        logger.info(f"Ban dang danh boss round {s}, thoi gian con lai {s}/{time_wait}s")
    character_moves_event.app_stop()


if __name__ == "__main__":
    time.sleep(2)
    logger.info("Start")

    n = 8
    start = time.time()

    thread_buy_all_hero = threading.Thread(target=hero.buy_all_hero, args=(n,))
    thread_buy_all_item = threading.Thread(target=item.buy_all_item, args=(n,))

    thread_buy_all_hero.start()
    thread_buy_all_item.start()

    thread_buy_all_hero.join()
    thread_buy_all_item.join()
    end = time.time()
    n = 8
    start2 = time.time()
    hero.buy_all_hero(n)
    item.buy_all_item(n)

    end2 = time.time()
    print("Time 1: ", end - start)
    print("Time 2: ", end2 - start2)
    pass
