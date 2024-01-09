import os
import threading
import time
import pyautogui
import pydirectinput
import controller.global_variables as cgv
from controller.filelog import logger
from controller.global_variables import PathManager, SelectWindow, global_event, character_moves_event

path = PathManager()

# event = Event()
Dota2 = SelectWindow("Dota 2")
REGION = (0, 0, 1936, 1119)
CONFIDENCE = 0.8
GRAYSCALE = True


class Button:
    name = ""
    img = None
    region = None
    grayscale = None
    confidence = None

    def __init__(self, para_name):
        self.name = para_name
        self.img = self._get_button_img(para_name)
        self.region = REGION
        self.grayscale = GRAYSCALE
        self.confidence = CONFIDENCE

    def _get_button_img(self, para_name):
        # global HERO_IMG
        if self.img is None:
            file_name = para_name + ".png"
            self.img = path.get_absolute_path(os.path.join("assets", "img", "button", file_name))
        return self.img

    def check_button(self, time_wait = 15):
        if global_event.check_event():
            # logger.info(f"Stop thread check button 1{ButtonInfor.name}")
            return
        i = 0
        # time.sleep(1)
        # logger.debug(f"Check button {self.name}")
        while True:
            if global_event.check_event():
                # logger.info(f"Stop thread check button 1{ButtonInfor.name}")
                break
            try:
                res = pyautogui.locateCenterOnScreen(self.img, confidence = self.confidence, region = self.region,
                                                     grayscale = self.grayscale, )
                if res is not None:
                    logger.debug("Da tim thay {}".format(self.name))
                    # pydirectinput.moveTo(res.x, res.y)
                    return True
            except pyautogui.ImageNotFoundException:
                i = i + 1
                if i > time_wait:
                    logger.error(f"Khong tim thay hinh anh {self.name}")
                    return False
                logger.debug(f"Dang tim hinh anh {self.name} so lan {i}/{time_wait}")
                time.sleep(1)  # return False
            except Exception as e:
                logger.error(e)
                break

    def click(self, time_sleep = 2, time_wait = 15, ):
        if global_event.check_event():
            return False
        logger.info(f"Click {self.name}")
        # time.sleep(time_sleep)
        if self.check_button(time_wait = time_wait) is True:
            time.sleep(time_sleep)
            # logger.info("Click {}".format(self.name))
            try:
                if global_event.check_event():
                    return False
                res = pyautogui.locateCenterOnScreen(self.img, confidence = self.confidence, region = self.region,
                                                     grayscale = self.grayscale, )
                pydirectinput.click(res[0], res[1])
                pydirectinput.moveTo(200, 200)
                return True
            except pyautogui.ImageNotFoundException:
                logger.debug("Khong tim thay hinh anh {}".format(self.name))
                return None
            except Exception as e:
                logger.error(e)
                return

    @staticmethod
    def click_lock(name_item, box):
        if global_event.check_event():
            return False
        logger.info("Click lock")
        i = 0
        while True:
            if global_event.check_event():
                break
            try:
                res = pyautogui.locateCenterOnScreen(Button("Look").img, confidence = 0.8, region = box,
                                                     grayscale = True
                                                     )
                # pydirectinput.moveTo(res)
                # time.sleep(1)
                pydirectinput.click(res.x, res.y)
                # time.sleep(1)
                pydirectinput.moveTo(200, 200)
                logger.debug(f"Ban khong du tien mua {name_item}, khoa de lan sau mua")
                return True
            except pyautogui.ImageNotFoundException:
                i = i + 1
                if i > 2:
                    return False
                logger.debug(f"Dang tim hinh anh {Button('Look').name} so lan {i}")
                time.sleep(1)
                break
            except Exception as e:
                logger.error(e)
                break

    @staticmethod
    def click_lock_hero(box):
        if global_event.check_event():
            return False
        logger.info("Click lock")
        i = 0
        # box=(828,169,296,348)
        # box = (687,237,158,276)
        while True:
            if global_event.check_event():
                break
            try:
                res = pyautogui.locateCenterOnScreen(Button("Lock_hero").img, confidence = 0.8, region = box,
                                                     grayscale = True
                                                     )
                # pydirectinput.moveTo(res.x, res.y+20)
                # time.sleep(1)
                pydirectinput.click(res.x, res.y + 20)
                # time.sleep(1)
                pydirectinput.moveTo(200, 200)
                logger.debug(f"Ban khong du tien mua  khoa de lan sau mua")
                return True
            except pyautogui.ImageNotFoundException:
                i = i + 1
                if i > 2:
                    return False
                logger.debug(f"Dang tim hinh anh Lock_hero so lan {i}")
                time.sleep(0.5)
            except Exception as e:
                logger.error(e)
                break

    @staticmethod
    def check_money():
        global REGION, CONFIDENCE, GRAYSCALE
        i = 0
        while True:
            try:
                if global_event.check_event():
                    break
                res_center = pyautogui.locateCenterOnScreen(Button("NotMoney").img, confidence = CONFIDENCE,
                                                            region = REGION, grayscale = GRAYSCALE
                                                            )
                if res_center is not None:
                    logger.debug("Ban khong du tien, di tiep vong sau")
                    cgv.set_money(False)
                    return False
            except pyautogui.ImageNotFoundException:
                i = i + 1
                time.sleep(0.2)
                if i >= 2:
                    cgv.set_money(True)
                    logger.debug("Ban du tien")
                    return True
            except Exception as e:
                logger.error(e)
                break

    @staticmethod
    def button_check(para_name, time_wait = 2, ):
        global REGION, CONFIDENCE, GRAYSCALE
        i = 0
        while True:
            if global_event.check_event():
                break
            try:
                res_center = pyautogui.locateCenterOnScreen(Button(para_name).img, confidence = CONFIDENCE,
                                                            region = REGION, grayscale = GRAYSCALE
                                                            )

                # pydirectinput.moveTo(res.x, res.y)
                pydirectinput.click(res_center[0], res_center[1])
                pydirectinput.moveTo(200, 200)
                # logger.info("Khong lay item")
                return True
            except pyautogui.ImageNotFoundException:
                i = i + 1
                if i > time_wait:
                    # logger.debug(CONFIDENCE)
                    return None
                time.sleep(0.5)
            except Exception as e:
                logger.error(e)
                break

    @staticmethod
    def enter_game():
        if global_event.check_event():
            return False
        logger.info("Vao game")
        Button("CreateCustomLobby").click(time_sleep = 2, time_wait = 15)
        Button("ServerLocaltion").click(time_sleep = 2, time_wait = 15)
        Button("ServerLocaltion_Singapore").click(time_sleep = 2, time_wait = 15)
        Button("CreatePassLobby").click(time_sleep = 2, time_wait = 15)
        pyautogui.write("asx")  # add password
        Button("CreateGame").click(time_sleep = 2, time_wait = 15)
        # time.sleep(4)
        Button("StartGame").click(time_sleep = 4, time_wait = 20)
        Button("Accept").click(time_sleep = 2, time_wait = 20)
        global_event.sleep(30)

        Button("Confirm").click(time_sleep = 2, time_wait = 20)
        Button("Challenge").click(time_sleep = 2, time_wait = 20)
        # click(ChallengeMax, 2)

        Button("SelectCharacter").click(time_sleep = 2, time_wait = 20)
        # py.moveTo(100, 100)
        Button("Prepare").click(time_sleep = 2, time_wait = 20)

    @staticmethod
    def check_exit_round(time_wait = 40):
        if global_event.check_event():
            return False
        character_moves_event.app_pause()
        logger.debug("Cho bat dau di chuyen")
        global REGION, CONFIDENCE, GRAYSCALE
        i = 0
        Button("Resurrect").click(time_sleep = 2, time_wait = 8)
        character_moves_event.app_resume()
        logger.debug("Bat dau di chuyen")
        while True:
            if global_event.check_event():
                break
            try:
                res_center = pyautogui.locateCenterOnScreen(Button("ProceedToRound").img, confidence = CONFIDENCE,
                                                            region = REGION, grayscale = GRAYSCALE, )
                if res_center is not None:
                    logger.debug("Da ket thuc round")
                    character_moves_event.app_stop()
                    return True
            except pyautogui.ImageNotFoundException:
                # check_resurrect(2)
                # check_abandon()
                # check_find_item()
                if Button.button_check("Abandon", 2):
                    character_moves_event.app_stop()

                if Button.button_check("Recycle", 2):
                    character_moves_event.app_stop()
                i = i + 1
                if i > time_wait:
                    character_moves_event.app_stop()
                    return False
                logger.debug(f"Cho ket thuc round lan {i}/{time_wait}")
                time.sleep(1)
            except Exception as e:
                logger.error(e)
                break

    @staticmethod
    def next_round():
        if global_event.check_event():
            return False
        logger.info("Next round")
        Button("ProceedToRound").click(time_sleep = 2, time_wait = 20
                                       )  # Button("Resurrect").click(time_sleep=2, time_wait=10)

    @staticmethod
    def character_moves(round_number = 2):
        if global_event.check_event():
            return False
        if character_moves_event.check_event():
            return False
        pydirectinput.PAUSE = 0.1
        loc = (973, 575)
        loc1 = 130
        number_click = 0
        number_click_first = 0
        if round_number == 1:
            number_click = 10
            number_click_first=6
        else:
            number_click = 14
            number_click_first = 8
        # time.sleep(3)
        # pydirectinput.moveTo(loc[0], loc[1])

        for i in range(0, number_click_first):
            if global_event.check_event():
                return False
            if character_moves_event.check_event():
                return False
            pydirectinput.rightClick(loc[0], loc[1] + loc1 + 30)  # time.sleep(time_click)
        for i in range(0, 8):
            if global_event.check_event():
                return False
            if character_moves_event.check_event():
                return False
            pydirectinput.rightClick(loc[0] - loc1 - 30, loc[1] + 20)  # time.sleep(time_click)
        while True:
            if global_event.check_event():
                return False
            if character_moves_event.check_event():
                return False
            for i in range(0, number_click - 1):
                if global_event.check_event():
                    return False
                if character_moves_event.check_event():
                    return False
                pydirectinput.rightClick(loc[0], loc[1] - loc1)  # time.sleep(time_click)
            for i in range(0, number_click):
                if global_event.check_event():
                    return False
                if character_moves_event.check_event():
                    return False
                pydirectinput.rightClick(loc[0] + loc1 + 30, loc[1] + 20)
            for i in range(0, number_click):
                if global_event.check_event():
                    return False
                if character_moves_event.check_event():
                    return False
                pydirectinput.rightClick(loc[0], loc[1] + loc1 + 40)
            for i in range(0, number_click):
                if global_event.check_event():
                    return False
                if character_moves_event.check_event():
                    return False
                pydirectinput.rightClick(loc[0] - loc1 - 30, loc[1] + 20)  # time.sleep(time_click)

    @staticmethod
    def run_round(round_number = 2):
        if global_event.check_event():
            return False
        logger.debug("Bat dau run round")
        character_moves_event.app_start()
        t1 = threading.Thread(target = Button.check_exit_round, args = (40,), daemon = True)
        t2 = threading.Thread(target = Button.character_moves, args = (round_number,), daemon = True)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        # Button("ProceedToRound").click(time_sleep=2, time_wait=20)  # Button("Resurrect").click(time_sleep=2, time_wait=10)

    @staticmethod
    def exit_round20():
        if global_event.check_event():
            return False
        Button("ProceedToRound").click(time_sleep = 2, time_wait = 20)

    @staticmethod
    def exit_game_round20():
        if global_event.check_event():
            return False
        logger.info("Thoat game")
        Button("Button_X").click(time_sleep = 2, time_wait = 15)
        Button("Hide").click(time_sleep = 2, time_wait = 15)
        Button("Equip").click(time_sleep = 2, time_wait = 15)
        Button("BulkDisassembly").click(time_sleep = 2, time_wait = 15)
        # click(BulkAll)
        Button("BulkBlue").click(time_sleep = 2, time_wait = 15)
        Button("BulkGreen").click(time_sleep = 2, time_wait = 15)
        Button("BulkPink").click(time_sleep = 2, time_wait = 15)
        Button("ConfirmDisassemBingEquip").click(time_sleep = 2, time_wait = 15)
        Button("ClickToClose").click(time_sleep = 2, time_wait = 15)
        Button("Back").click(time_sleep = 2, time_wait = 15)
        Button("Disconnect").click(time_sleep = 2, time_wait = 15)
        Button("LeaveGame").click(time_sleep = 2, time_wait = 15)
        logger.info("Check game co update trong 10s")
        Button("Update").click(time_sleep = 2, time_wait = 15)

    @staticmethod
    def roll_game():
        if global_event.check_event():
            return False
        logger.info("Click roll")
        i = 0
        while True:
            if global_event.check_event():
                break
            try:
                res = pyautogui.locateCenterOnScreen(Button("Roll").img, confidence = CONFIDENCE, region = REGION,
                                                     grayscale = GRAYSCALE
                                                     )
                pydirectinput.click(res.x, res.y)
                pyautogui.moveTo(200, 200)
                if Button.check_money() is False:
                    cgv.set_money(False)
                    return False
                return True
            except pyautogui.ImageNotFoundException:
                i = i + 1
                if i > 5:
                    return False
                logger.debug(f"Dang tim hinh anh Roll so lan {i}/5")
                global_event.sleep(1)
            except Exception as e:
                logger.error(e)
                break


def main():
    pass


if __name__ == "__main__":
    # main()
    pass
