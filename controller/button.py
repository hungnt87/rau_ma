import os
import threading

import pyautogui
import pydirectinput

import controller.global_variables as cgv
from controller.filelog import logger
from controller.global_variables import SelectWindow, character_moves_event, global_event, path

REGION = (0, 0, 1936, 1119)
CONFIDENCE = 0.8
GRAYSCALE = True


class Button:
    name = ""
    img = None
    
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
    
    def check_button(self, time_wait = 30):
        if global_event.check_event():
            return False
        i = 0
        while True:
            if global_event.check_event():
                # logger.info(f"Stop thread check button 1{ButtonInfor.name}")
                break
            try:
                res = pyautogui.locateCenterOnScreen(self.img, confidence = self.confidence, region = self.region,
                                                     grayscale = self.grayscale, )
                if res:
                    logger.debug("Da tim thay: {}".format(self.name))
                    return True
            except pyautogui.ImageNotFoundException:
                i = i + 1
                if i > time_wait:
                    logger.error(f"Khong tim thay hinh anh: {self.name}")
                    return False
                logger.debug(f"Dang tim hinh anh: {self.name} so lan {i}/{time_wait}")
                global_event.sleep(1)  # return False
            except Exception as e:
                logger.error(e)
                break
        if global_event.check_event():
            return False
    
    def click(self, time_sleep = 1, time_wait = 60):
        if global_event.check_event():
            return False
        if self.name == "Button_X" or self.name == "Hide":
            logger.info(f"Chuan bi thoat game sau: {time_sleep}s")
            character_moves_event.app_stop()
            global_event.sleep(time_sleep = time_sleep)
        else:
            pass
        
        logger.info(f"Click {self.name}")
        # time.sleep(time_sleep)
        if self.check_button(time_wait = time_wait) is True:
            global_event.sleep(time_sleep)
            # logger.info("Click {}".format(self.name))
            try:
                if global_event.check_event():
                    return False
                res = pyautogui.locateCenterOnScreen(self.img, minSearchTime = 1, confidence = self.confidence,
                                                     region = self.region, grayscale = self.grayscale, )
                global_event.sleep(0.5)
                pydirectinput.click(res[0], res[1])
                global_event.sleep(0.5)
                pydirectinput.moveTo(200, 200)
                return True
            except pyautogui.ImageNotFoundException:
                logger.debug(f"Khong tim thay hinh anh: {self.name}")
                return None
            except Exception as e:
                logger.error(e)
                return
        if global_event.check_event():
            return False
    
    @staticmethod
    def click_lock_item(name_item, box):
        if global_event.check_event():
            return False
        logger.info("Click lock")
        try:
            res = pyautogui.locateCenterOnScreen(Button("Look").img, minSearchTime = 0.5, confidence = 0.8,
                                                 region = box, grayscale = True)
            # pydirectinput.moveTo(res)
            global_event.sleep(0.5)
            pydirectinput.click(res.x, res.y)
            global_event.sleep(0.5)
            # time.sleep(1)
            pydirectinput.moveTo(200, 200)
            logger.debug(f"Ban khong du tien mua {name_item}, khoa de lan sau mua")
            return True
        except pyautogui.ImageNotFoundException:
            return False
        except Exception as e:
            logger.error(e)
            return False
    
    @staticmethod
    def click_lock_hero(hero_name, box):
        if global_event.check_event():
            return False
        logger.info("Click lock")
        try:
            res = pyautogui.locateCenterOnScreen(Button("Lock_hero").img, minSearchTime = 0.5, confidence = 0.8,
                                                 region = box, grayscale = True)
            global_event.sleep(0.5)
            pydirectinput.click(res.x, res.y + 20)
            global_event.sleep(0.5)
            pydirectinput.moveTo(200, 200)
            logger.debug(f"Ban khong du tien {hero_name} khoa de lan sau mua")
            return True
        except pyautogui.ImageNotFoundException:
            logger.debug(f"Khong tim thay hinh anh {Button('Lock_hero').name}")
            return False
        except Exception as e:
            logger.error(e)
            return False
    
    @staticmethod
    def check_money():
        global REGION, CONFIDENCE, GRAYSCALE
        try:
            if global_event.check_event():
                return
            res_center = pyautogui.locateCenterOnScreen(Button("NotMoney").img, minSearchTime = 0.5,
                                                        confidence = CONFIDENCE, region = REGION,
                                                        grayscale = GRAYSCALE, )
            if res_center:
                logger.debug("Ban khong du tien, di tiep vong sau")
                cgv.set_money(False)
                return False
        except pyautogui.ImageNotFoundException:
            cgv.set_money(True)
            return True
        except Exception as e:
            logger.error(e)
            return None
    
    @staticmethod
    def button_check(para_name, time_wait = 2, ):
        global REGION, CONFIDENCE, GRAYSCALE
        if global_event.check_event():
            return False
        try:
            res_center = pyautogui.locateCenterOnScreen(Button(para_name).img, minSearchTime = time_wait,
                                                        confidence = CONFIDENCE, region = REGION,
                                                        grayscale = GRAYSCALE, )
            if res_center:
                return True
        except pyautogui.ImageNotFoundException:
            logger.debug(f"Khong tim thay hinh anh {Button(para_name).name}")
            return False
        except Exception as e:
            logger.error(e)
            return False
    
    @staticmethod
    def enter_game():
        if global_event.check_event():
            return False
        logger.info("Vao game")
        Button("CreateCustomLobby").click()
        Button("ServerLocaltion").click()
        Button("ServerLocaltion_Singapore").click()
        Button("CreatePassLobby").click()
        pyautogui.write("asx")  # add password
        Button("CreateGame").click()
        # time.sleep(4)
        Button("StartGame").click(time_sleep = 5, time_wait = 30)
        Button("Accept").click(time_sleep = 5, time_wait = 30)
        # global_event.sleep(30)
        
        Button("Confirm").click(time_sleep = 5, time_wait = 120)
        Button("Challenge").click()
        # click(ChallengeMax, 2)
        
        Button("SelectCharacter").click()
        # py.moveTo(100, 100)
        Button("Prepare").click()
    
    @staticmethod
    def check_exit_round(time_wait = 40):
        if global_event.check_event():
            return False
        character_moves_event.app_start()
        character_moves_event.app_pause()
        global REGION, CONFIDENCE, GRAYSCALE
        i = 0
        
        character_moves_event.app_resume()
        logger.debug("Bat dau di chuyen")
        while True:
            if global_event.check_event():
                break
            try:
                res_center = pyautogui.locateCenterOnScreen(Button("ProceedToRound").img, confidence = CONFIDENCE,
                                                            region = REGION, grayscale = GRAYSCALE, )
                if res_center:
                    logger.debug("Da ket thuc round")
                    character_moves_event.app_stop()
                    return True
            except pyautogui.ImageNotFoundException:
                if Button.button_check("Abandon", 2):
                    character_moves_event.app_stop()
                    Button("Abandon").click()
                if Button.button_check("Recycle", 2):
                    character_moves_event.app_stop()
                    Button("Recycle").click()
                i = i + 1
                logger.debug(f"Cho ket thuc round lan {i}/{time_wait}")
                global_event.sleep(1)
                if i > time_wait:
                    character_moves_event.app_stop()
                    return False
            
            except Exception as e:
                logger.error(e)
                break
        if global_event.check_event():
            return False
    
    @staticmethod
    def check_resurrect():
        if global_event.check_event():
            return False
        global REGION, CONFIDENCE, GRAYSCALE
        i = 0
        while True:
            if global_event.check_event():
                break
            try:
                res_center = pyautogui.locateCenterOnScreen(Button("Resurrect").img, confidence = CONFIDENCE,
                                                            region = REGION, grayscale = GRAYSCALE, )
                if res_center:
                    global_event.sleep(0.5)
                    pydirectinput.click(res_center[0], res_center[1])
                    global_event.sleep(0.5)
                    pydirectinput.moveTo(200, 200)
                    global_event.sleep(1)
                    character_moves_event.app_resume()
                    return True
            except pyautogui.ImageNotFoundException:
                i = i + 1
                logger.debug(f"Cho ket thuc round lan {i}/10")
                global_event.sleep(1)
                if i > 3:
                    character_moves_event.app_resume()
                if i > 10:
                    return False
            except Exception as e:
                logger.error(e)
                break
        if global_event.check_event():
            return False
    
    @staticmethod
    def next_round():
        if global_event.check_event():
            return False
        logger.info("Next round")
        Button("ProceedToRound").click(time_sleep = 2, time_wait = 20)
    
    @staticmethod
    def character_moves(round_number = 2):
        logger.debug("Cho bat dau di chuyen")
        if global_event.check_event():
            return False
        if not global_event.event_stop.is_set():
            if character_moves_event.check_event():
                return False
        pydirectinput.PAUSE = 0.1
        loc = (973, 575)
        loc1 = 130
        logger.debug("Bat dau di chuyen")
        if round_number == 1:
            number_click = 9
            number_click_first = 6
        else:
            number_click = 12
            number_click_first = 8
        for i in range(0, number_click_first):
            if global_event.check_event():
                return False
            if character_moves_event.check_event():
                return False
            pydirectinput.rightClick(loc[0], loc[1] + loc1 + 30)
        for i in range(0, 6):
            if global_event.check_event():
                return False
            if character_moves_event.check_event():
                return False
            pydirectinput.rightClick(loc[0] - loc1 - 30, loc[1] + 20)
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
                pydirectinput.rightClick(loc[0], loc[1] - loc1)
            
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
                pydirectinput.rightClick(loc[0] - loc1 - 30, loc[1] + 20)
    
    @staticmethod
    def run_round(round_number = 2):
        if global_event.check_event():
            return False
        logger.debug("Bat dau run round")
        character_moves_event.app_start()
        character_moves_event.app_pause()
        t_check_exit_round = threading.Thread(target = Button.check_exit_round, args = (40,))
        t_check_resurrect = threading.Thread(target = Button.check_resurrect, args = (), daemon = True)
        t_character_moves = threading.Thread(target = Button.character_moves, args = (round_number,), daemon = True)
        # start thread
        t_check_exit_round.start()
        t_check_resurrect.start()
        t_character_moves.start()
        # join thread
        t_check_exit_round.join()
        t_character_moves.join()
        if global_event.check_event():
            return False
    
    @staticmethod
    def exit_round20():
        if global_event.check_event():
            return False
        Button("ProceedToRound").click()
        if global_event.check_event():
            return False
    
    @staticmethod
    def exit_game_round20():
        if global_event.check_event():
            return False
        logger.info("Thoat game")
        Button("Button_X").click()
        Button("Hide").click()
        Button("Equip").click()
        Button("BulkDisassembly").click()
        # click(BulkAll)
        Button("BulkBlue").click()
        Button("BulkGreen").click()
        Button("BulkPink").click()
        Button("ConfirmDisassemBingEquip").click()
        Button("ClickToClose").click()
        Button("Back").click()
        Button("Disconnect").click()
        Button("LeaveGame").click()
        logger.info("Check game co update trong 15s")
        Button("Update").click(time_sleep = 2, time_wait = 15)
        if global_event.check_event():
            return False
    
    @staticmethod
    def roll_game():
        if global_event.check_event():
            return False
        logger.info("Click roll")
        try:
            res = pyautogui.locateCenterOnScreen(Button("Roll").img, minSearchTime = 1, confidence = CONFIDENCE,
                                                 region = REGION, grayscale = GRAYSCALE, )
            global_event.sleep(0.5)
            pydirectinput.click(res.x, res.y)
            global_event.sleep(0.5)
            pyautogui.moveTo(200, 200)
            if Button.check_money() is False:
                cgv.set_money(False)
                return False
            return True
        except pyautogui.ImageNotFoundException:
            logger.debug(f"Khong tim thay hinh anh {Button('Roll').name}")
            return False
        except Exception as e:
            logger.error(e)
            return None


def main():
    pass


if __name__ == "__main__":
    # main()
    pass
