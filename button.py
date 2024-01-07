import os
import sys
import pyautogui
import time
import pydirectinput
from controller.filelog import logger
import controller.global_variables as cgv

# from controller.global_variables import Global_variables

gv = cgv.Global_variables()
event_stop = cgv.event_stop
event_pause = cgv.event_pause


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


path_parent = os.getcwd()
path_data = "data"
path_image = "image"
# relative_path = os.path.join(path_data, path_image)
# path_data_image = os.path.join(path_data, path_image)


class ButtonInfor:
    name = ""
    img = None

    def __init__(self, para_name):
        self.name = para_name
        self.img = self.get_button_img(para_name)

    def get_button_img(self, para_name):
        # global HERO_IMG
        if self.img is None:
            file_name = para_name + ".png"
            relative_path = os.path.join(path_data, path_image, file_name)
            imgage = resource_path(relative_path)
            self.img = imgage
        return self.img


status_not_money = True


def get_status_not_money():
    global status_not_money
    if status_not_money is True:
        return True
    else:
        return False


def set_status_not_money(status=False):
    global status_not_money
    status_not_money = status


def reset_status_not_money():
    global status_not_money
    status_not_money = True


Back = ButtonInfor("Back")
Disconnect = ButtonInfor("Disconnect")
LeaveGame = ButtonInfor("LeaveGame")
CreateCustomLobby = ButtonInfor("CreateCustomLobby")
ServerLocaltion = ButtonInfor("ServerLocaltion")
ServerLocaltion_Singapore = ButtonInfor("ServerLocaltion_Singapore")
CreatePassLobby = ButtonInfor("CreatePassLobby")
CreateGame = ButtonInfor("CreateGame")
StartGame = ButtonInfor("StartGame")
Accept = ButtonInfor("Accept")
Confirm = ButtonInfor("Confirm")
Challenge = ButtonInfor("Challenge")
ChallengeMax = ButtonInfor("ChallengeMax")
SelectCharacter = ButtonInfor("SelectCharacter")
Prepare = ButtonInfor("Prepare")
ProceedToRound2 = ButtonInfor("ProceedToRound2")
Roll = ButtonInfor("Roll")
ProceedToRound = ButtonInfor("ProceedToRound")
Resurrect = ButtonInfor("Resurrect")
NotMoney = ButtonInfor("NotMoney")
Recycle = ButtonInfor("Recycle")
Abandon = ButtonInfor("Abandon")
Back_On_Round20 = ButtonInfor("Back_On_Round20")
Hide = ButtonInfor("Hide")
BulkDisassembly = ButtonInfor("BulkDisassembly")
BulkAll = ButtonInfor("BulkAll")
BulkBlue = ButtonInfor("BulkBlue")
BulkGreen = ButtonInfor("BulkGreen")
BulkPink = ButtonInfor("BulkPink")
ConfirmDisassemBingEquip = ButtonInfor("ConfirmDisassemBingEquip")
Equip = ButtonInfor("Equip")
ClickToClose = ButtonInfor("ClickToClose")
Look = ButtonInfor("Look")
Lock_hero = ButtonInfor("Lock_hero")
Save = ButtonInfor("Save")
Button_X = ButtonInfor("Button_X")
Update = ButtonInfor("Update")


def check_button(ButtonInfor, time_wait=60):
    if gv.check_event():
        # logger.info(f"Stop thread check button 1{ButtonInfor.name}")
        return
    i = 0
    # time.sleep(1)
    logger.debug(f"Check button {ButtonInfor.name}")
    while True:
        if gv.check_event():
            # logger.info(f"Stop thread check button 1{ButtonInfor.name}")
            break
        try:
            res = pyautogui.locateCenterOnScreen(
                ButtonInfor.img,
                confidence=0.9,
                region=(0, 0, 1936, 1119),
                grayscale=True,
            )
            # pydirectinput.moveTo(res.x, res.y)
            # if res is not None:
            # logger.info("Da tim thay {}".format(ButtonInfor.name))

            return True
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > time_wait:
                logger.error(f"Khong tim thay hinh anh {ButtonInfor.name}")
                return False
            logger.debug(f"Dang tim hinh anh {ButtonInfor.name} so lan {i}/{time_wait}")
            time.sleep(1)
            # return False
        except Exception as e:
            logger.error(e)
            break


def click(
    ButtonInfor,
    time_sleep=2,
    time_wait=15,
):
    """Click button infor
    Args:
        ButtonInfor: ButtonInfor
        time_sleep: time sleep after click
    """
    if gv.check_event():
        return
    logger.info(f"Click {ButtonInfor.name}")

    time.sleep(time_sleep)
    if check_button(ButtonInfor, time_wait=time_wait) is True:
        time.sleep(time_sleep)
        logger.info("Click {}".format(ButtonInfor.name))
        try:
            res = pyautogui.locateCenterOnScreen(
                ButtonInfor.img,
                confidence=0.8,
                region=(0, 0, 1936, 1119),
                grayscale=True,
            )
            pydirectinput.click(res[0], res[1])
            pydirectinput.moveTo(200, 200)
            return True
        except pyautogui.ImageNotFoundException:
            logger.debug("Khong tim thay hinh anh {}".format(ButtonInfor.name))
            return False
        except Exception as e:
            logger.error(e)
            return


def check_not_money():
    i = 0
    while True:
        if gv.check_event():
            break
        try:
            pyautogui.locateCenterOnScreen(
                NotMoney.img, confidence=0.9, region=(0, 0, 1936, 1119), grayscale=False
            )
            logger.debug("Ban khong du tien, di tiep vong sau")
            set_status_not_money(True)
            return True
        except pyautogui.ImageNotFoundException:
            i = i + 1
            time.sleep(0.2)
            if i >= 2:
                status_not_money = False
                return False
        except Exception as e:
            logger.error(e)
            break


def check_find_item(
    time_wait=2,
):
    i = 0
    while True:
        if gv.check_event():
            break
        try:
            res = pyautogui.locateCenterOnScreen(
                Recycle.img, confidence=0.8, region=(0, 0, 1936, 1119), grayscale=True
            )
            # pydirectinput.moveTo(res.x, res.y)
            pydirectinput.click(res.x, res.y)
            pydirectinput.moveTo(200, 200)
            # logger.info("Khong lay item")
            return True
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > time_wait:
                return False
            time.sleep(0.5)
        except Exception as e:
            logger.error(e)
            break


def check_resurrect(
    time_wait=10,
):
    i = 0
    while True:
        if gv.check_event():
            break
        try:
            res = pyautogui.locateCenterOnScreen(
                Resurrect.img,
                confidence=0.9,
                region=(0, 0, 1920, 1135),
                grayscale=False,
            )
            # time.sleep(1)
            # pydirectinput.moveTo(res.x, res.y)
            pydirectinput.click(res.x, res.y)
            pydirectinput.moveTo(200, 200)
            # logger.info("Chon Resurrect ")
            break
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > time_wait:
                return True
            time.sleep(1)
        except Exception as e:
            logger.error(e)
            break


def check_abandon(
    time_wait=2,
):
    # logger.info("Kiem tra Abandon")
    i = 0
    while True:
        if gv.check_event():
            break
        try:
            res = pyautogui.locateCenterOnScreen(
                Abandon.img, confidence=0.9, region=(0, 0, 1936, 1119), grayscale=False
            )
            # time.sleep(1)
            # pydirectinput.moveTo(res.x, res.y)
            # time.sleep(1)
            pydirectinput.click(res.x, res.y)
            return True
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > time_wait:
                return False
            # logger.debug("Cho xuat hien Abandon so lan {}".format(i))
            time.sleep(0.5)
        except Exception as e:
            logger.error(e)
            break


def check_proceed_to_round(
    time_wait=40,
):
    check_resurrect()
    i = 0
    while True:
        if gv.check_event():
            break
        try:
            res = pyautogui.locateCenterOnScreen(
                ProceedToRound.img,
                confidence=0.9,
                region=(0, 0, 1936, 1119),
                grayscale=True,
            )
            # time.sleep(1)
            return True
        except pyautogui.ImageNotFoundException:
            # check_resurrect(2)
            check_abandon()
            check_find_item()
            i = i + 1
            if i > time_wait:
                return False
            logger.debug(f"Cho xuat hien {ProceedToRound.name} lan {i}/{time_wait}")
            time.sleep(1)
        except pyscreeze.ImageNotFoundException:
            logger.error("khong tim thay hinh anh")
            return False
        except Exception as e:
            logger.error(e)
            break


def exit_game():
    logger.info("Thoat game")
    click(Back, 0)
    click(Disconnect, 0)
    click(LeaveGame, 0)


def exit_game_round20():
    if gv.check_event():
        return False
    logger.info("Thoat game")
    bulk_disassembly()
    click(Back)
    click(Disconnect)
    click(LeaveGame)
    logger.info("Check game co update trong 10s")
    click(Update, time_sleep=2, time_wait=10)


def enter_game():
    if gv.check_event():
        return False
    logger.info("Vao game")
    click(CreateCustomLobby)
    click(ServerLocaltion)
    click(ServerLocaltion_Singapore)
    click(CreatePassLobby)
    pyautogui.write("asx")  # add password
    click(CreateGame)
    # time.sleep(4)
    click(StartGame, time_sleep=2, time_wait=20)
    click(Accept)
    if gv.check_event():
        return
    time.sleep(30)
    click(Confirm, time_sleep=2, time_wait=60)
    # click(ChallengeMax, 2)
    click(Challenge, time_sleep=2)
    click(SelectCharacter, time_sleep=2)
    # py.moveTo(100, 100)
    click(Prepare, time_sleep=2)


def roll_game():
    if gv.check_event():
        return False
    logger.info("Click {}".format(Roll.name))
    i = 0
    while True:
        if gv.check_event():
            break
        try:
            res = pyautogui.locateCenterOnScreen(
                Roll.img, confidence=0.9, region=(0, 0, 1936, 1119), grayscale=True
            )
            pydirectinput.click(res.x, res.y)
            pyautogui.moveTo(200, 200)
            if check_not_money() is True:
                set_status_not_money(True)
                return False
            return True
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > 5:
                return False
            logger.debug(f"Dang tim hinh anh {Roll.name} so lan {i}/60")
            time.sleep(1)
        except Exception as e:
            logger.error(e)
            break


def click_procceed_to_round():
    if gv.check_event():
        return False
    click(ProceedToRound)


def next_round():
    if gv.check_event():
        return False
    logger.info("Next round")
    click(ProceedToRound)
    check_proceed_to_round()


def bulk_disassembly():
    """
    Perform bulk disassembly by clicking on the necessary buttons.
    """
    if gv.check_event():
        return
    logger.info("Bat dau phan giai tat ca trang bi da nhat")
    try:
        click(Button_X)
        click(Hide)
        click(Equip)
        click(BulkDisassembly)
        # click(BulkAll)
        click(BulkBlue, time_sleep=1, time_wait=5)
        click(BulkGreen, time_sleep=1, time_wait=5)
        click(BulkPink, time_sleep=1, time_wait=5)
        click(ConfirmDisassemBingEquip)
        click(ClickToClose, time_sleep=4, time_wait=10)
        return True
    except Exception as e:
        logger.error("Khong hoan thanh phan giai trang bi")
        logger.error(e)
        return False


def click_lock(
    name_item,
    box,
):
    if gv.check_event():
        return
    logger.info("Click lock")
    i = 0
    while True:
        if gv.check_event():
            break
        try:
            res = pyautogui.locateCenterOnScreen(
                Look.img, confidence=0.8, region=box, grayscale=True
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
            logger.debug(f"Dang tim hinh anh {Look.name} so lan {i}")
            time.sleep(1)
            break
        except Exception as e:
            logger.error(e)
            break


def click_lock_hero(
    box,
):
    logger.info("Click lock")
    i = 0
    # box=(828,169,296,348)
    # box = (687,237,158,276)
    while True:
        if gv.check_event():
            break
        try:
            res = pyautogui.locateCenterOnScreen(
                Lock_hero.img, confidence=0.9, region=box, grayscale=True
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
            logger.debug(f"Dang tim hinh anh {Lock_hero.name} so lan {i}")
            time.sleep(0.5)
        except Exception as e:
            logger.error(e)
            break


if __name__ == "__main__":
    # bulk_disassembly()
    # exit_game()
    # exit_game_round20()
    # time.sleep(2)
    # check_button(Update, 5)
    # bulk_disassembly()
    gv.app_start()
    time.sleep(2)

    # exit_game_round20()
    pass
