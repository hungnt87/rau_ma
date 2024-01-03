import pyautogui
import time
from log import logger
import pydirectinput
import os
import sys
import threading


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


path_parent = os.getcwd()
path_data = "data"
path_image = "image"
# relative_path = os.path.join(path_data, path_image)
path_data_image = os.path.join(path_data, path_image)


class ButtonInfor:
    def __init__(self, para_name):
        self.name = para_name
        file_name = para_name + ".png"
        relative_path = os.path.join(path_data_image, file_name)
        self.img = resource_path(relative_path)


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
ProceedToRound3 = ButtonInfor("ProceedToRound3")
ProceedToRound4 = ButtonInfor("ProceedToRound4")
ProceedToRound5 = ButtonInfor("ProceedToRound5")
ProceedToRound6 = ButtonInfor("ProceedToRound6")
ProceedToRound7 = ButtonInfor("ProceedToRound7")
ProceedToRound8 = ButtonInfor("ProceedToRound8")
ProceedToRound9 = ButtonInfor("ProceedToRound9")
ProceedToRound10 = ButtonInfor("ProceedToRound10")
ProceedToRound11 = ButtonInfor("ProceedToRound11")
ProceedToRound12 = ButtonInfor("ProceedToRound12")
ProceedToRound13 = ButtonInfor("ProceedToRound13")
ProceedToRound14 = ButtonInfor("ProceedToRound14")
ProceedToRound15 = ButtonInfor("ProceedToRound15")
ProceedToRound16 = ButtonInfor("ProceedToRound16")
ProceedToRound17 = ButtonInfor("ProceedToRound17")
ProceedToRound18 = ButtonInfor("ProceedToRound18")
ProceedToRound19 = ButtonInfor("ProceedToRound19")
ProceedToRound20 = ButtonInfor("ProceedToRound20")
Resurrect = ButtonInfor("Resurrect")
NotMoney = ButtonInfor("NotMoney")
Recycle = ButtonInfor("Recycle")
Abandon = ButtonInfor("Abandon")
Back_On_Round20 = ButtonInfor("Back_On_Round20")
Hide = ButtonInfor("Hide")
BulkDisassembly = ButtonInfor("BulkDisassembly")
BulkAll = ButtonInfor("BulkAll")
ConfirmDisassemBingEquip = ButtonInfor("ConfirmDisassemBingEquip")
Equip = ButtonInfor("Equip")
ClickToClose = ButtonInfor("ClickToClose")
Look = ButtonInfor("Look")
Lock_hero = ButtonInfor("Lock_hero")
Save = ButtonInfor("Save")
Button_X = ButtonInfor("Button_X")
Update = ButtonInfor("Update")

event_stop = threading.Event()
event_pause = threading.Event()


def check_button(
    ButtonInfor, time_wait=60, stop_event=event_stop, pause_event=event_pause
):
    i = 0
    # time.sleep(1)
    logger.debug(f"Check button {ButtonInfor.name}")
    while True:
        if stop_event.is_set():
            logger.info(f"Stop thread check button 1 {ButtonInfor.name}")
            break
        if pause_event.is_set():
            logger.info(f"Pause thread check button 1 {ButtonInfor.name}")
            time.sleep(1)
            continue
        try:
            if stop_event.is_set():
                logger.info(f"Stop thread check button 2{ButtonInfor.name}")
                break
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
            if stop_event.is_set():
                logger.info(f"Stop thread check button 3 {ButtonInfor.name}")
                break
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


def click(ButtonInfor, time_sleep=2, time_wait=60, stop_event=event_stop):
    """Click button infor
    Args:
        ButtonInfor: ButtonInfor
        time_sleep: time sleep after click
    """
    logger.info(f"Click {ButtonInfor.name}")
    if stop_event.is_set():
        logger.info(f"Stop thread click button 1{ButtonInfor.name}")
        return
    # time.sleep(time_sleep)
    if check_button(ButtonInfor, time_wait=time_wait) is True:
        if stop_event.is_set():
            logger.info(f"Stop thread click button 2{ButtonInfor.name}")
            return
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


def check_not_money(event=threading.Event()):
    i = 0
    while True:
        if event.is_set():
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


def check_find_item(time_wait=2, event=threading.Event()):
    i = 0
    while True:
        if event.is_set():
            break
        try:
            res = pyautogui.locateCenterOnScreen(
                Recycle.img, confidence=0.9, region=(0, 0, 1936, 1119), grayscale=False
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


def check_resurrect(time_wait=10, event=threading.Event()):
    i = 0
    while True:
        if event.is_set():
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


def check_abandon(time_wait=2, event=threading.Event()):
    # logger.info("Kiem tra Abandon")
    i = 0
    while True:
        if event.is_set():
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


def check_proceed_to_round(time_wait=40, event=threading.Event()):
    check_resurrect()
    i = 0
    while True:
        if event.is_set():
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


def exit_game_round20(event=threading.Event()):
    logger.info("Thoat game")
    bulk_disassembly()
    click(Back, event=event)
    click(Disconnect, event=event)
    click(LeaveGame, event=event)
    logger.info("Check game co update trong 10s")
    click(Update, time_sleep=2, time_wait=10, event=event)


def enter_game(event=threading.Event()):
    # event.set()
    if event.is_set():
        logger.info("Stop thread enter game")
        return
    logger.info("Vao game")
    click(CreateCustomLobby, event=event)
    click(ServerLocaltion, event=event)
    click(ServerLocaltion_Singapore, event=event)
    click(CreatePassLobby, event=event)
    pyautogui.write("asx")  # add password
    click(CreateGame, event=event)
    # time.sleep(4)
    click(StartGame, time_sleep=2, event=event)
    click(Accept, event=event)
    time.sleep(30)
    click(Confirm, time_sleep=2, event=event)
    # click(ChallengeMax, 2)
    click(Challenge, time_sleep=2, event=event)
    click(SelectCharacter, time_sleep=2, event=event)
    # py.moveTo(100, 100)
    click(Prepare, time_sleep=2, event=event)


def roll_game(event=threading.Event()):
    logger.info("Click {}".format(Roll.name))
    i = 0
    while True:
        if event.is_set():
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
            if i > 60:
                return False
            logger.debug(f"Dang tim hinh anh {Roll.name} so lan {i}/60")
            time.sleep(1)
        except Exception as e:
            logger.error(e)
            break


def click_procceed_to_round(event=threading.Event()):
    click(ProceedToRound, event=event)


def next_round():
    logger.info("Next round")
    click(ProceedToRound, event=event)
    check_proceed_to_round(event=event)


def bulk_disassembly(event=threading.Event()):
    """
    Perform bulk disassembly by clicking on the necessary buttons.
    """
    logger.info("Bat dau phan giai tat ca trang bi da nhat")
    try:
        click(Button_X, event=event)
        click(Hide, event=event)
        click(Equip, event=event)
        click(BulkDisassembly, event=event)
        click(BulkAll, event=event)
        click(ConfirmDisassemBingEquip, event=event)
        click(ClickToClose, event=event)
        return True
    except Exception as e:
        logger.error("Khong hoan thanh phan giai trang bi")
        logger.error(e)
        return False


def click_lock(name_item, box, event=threading.Event()):
    logger.info("Click lock")
    i = 0
    while True:
        if event.is_set():
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


def click_lock_hero(box, event=threading.Event()):
    logger.info("Click lock")
    i = 0
    # box=(828,169,296,348)
    # box = (687,237,158,276)
    while True:
        if event.is_set():
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
    pass
