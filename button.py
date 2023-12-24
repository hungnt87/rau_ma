import pyautogui
import time
import pyscreeze
from log import logger


class ButtonInfor:
    def __init__(self, para_name):
        self.name = para_name
        self.img = "data\\image\\" + para_name + ".png"


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


def click(ButtonInfor, time_sleep=0):
    logger.info("Click {}".format(ButtonInfor.name))
    i = 0
    while True:
        try:
            res = pyautogui.locateCenterOnScreen(
                ButtonInfor.img, confidence=0.9, region=(0, 0, 1936, 1119), grayscale=True
            )
            if res is not None and time_sleep > 0:
                logger.info(
                    "Cho xuat hien {} trong thoi gian {}".format(
                        ButtonInfor.name, time_sleep
                    )
                )
                time.sleep(time_sleep)
            
            # time.sleep(1)
            pyautogui.moveTo(res)
            time.sleep(1)
            pyautogui.click(res)
            time.sleep(1)
            pyautogui.moveTo(200, 200)
            break
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > 60:
                break
            logger.debug("Dang tim hinh anh {} so lan {}".format(ButtonInfor.name, i))
            time.sleep(1)
        except TypeError:
            logger.error("Khong tim thay hinh anh {}".format(ButtonInfor.name))


def check_not_money():
    i = 0
    while True:
        try:
            pyautogui.locateCenterOnScreen(
                NotMoney.img, confidence=0.9, region=(0, 0, 1936, 1119), grayscale=False
            )
            return True
        except pyautogui.ImageNotFoundException:
            i = i + 1
            logger.debug("Dang kiem tra ban co tien khong so lan {}".format(i))
            time.sleep(0.2)
            if i >= 2:
                return False
        except TypeError:
            logger.error("Khong tim thay hinh anh {}".format(NotMoney.name))
            return False


def check_find_item():
    i = 0
    while True:
        try:
            res = pyautogui.locateCenterOnScreen(
                Recycle.img, confidence=0.9, region=(0, 0, 1936, 1119), grayscale=False
            )
           
            pyautogui.moveTo(res)
            pyautogui.click(res)
            pyautogui.moveTo(200, 200)
            logger.info("Khong lay item")
            break
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > 2:
                break
            logger.debug("Cho xuat hien Recycle so lan {}".format(i))
            time.sleep(1)
        except TypeError:
            logger.error("Khong tim thay hinh anh {}".format(Recycle.name))
            break


def check_resurrect(time_wait=10):
    i = 0
    while True:
        try:
            res = pyautogui.locateCenterOnScreen(
                Resurrect.img, confidence=0.9, region=(0, 0, 1920, 1135), grayscale=False
            )            
            time.sleep(1)
            pyautogui.moveTo(res)
            pyautogui.click(res)
            logger.info("Chon Resurrect ")
            break
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > time_wait:
                break
            logger.debug("Cho xuat hien Resurrect {}".format(i))
            time.sleep(1)
        except TypeError:
            logger.error("Khong tim thay hinh anh {}".format(Resurrect.name))


def check_abandon(time_wait=2):
    logger.info("Kiem tra Abandon")
    i = 0
    while True:
        try:
            res = pyautogui.locateCenterOnScreen(
                Abandon.img, confidence=0.9, region=(0, 0, 1936, 1119), grayscale=False
            )           
            time.sleep(1)
            pyautogui.moveTo(res)
            time.sleep(1)
            pyautogui.click(res)
            break
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > time_wait:
                break
            logger.debug("Cho xuat hien Abandon so lan {}".format(i))
            time.sleep(1)
        except TypeError:
            logger.error("Khong tim thay hinh anh {}".format(Abandon.name))
            break


def check_proceed_to_round():
    check_resurrect()
    i = 0
    while True:
        try:
            res = pyautogui.locateCenterOnScreen(
                ProceedToRound.img, confidence=0.9, region=(0, 0, 1936, 1119), grayscale=False
            )
            time.sleep(1)
            return True
        except pyautogui.ImageNotFoundException:
            # check_resurrect(2)
            check_abandon()
            check_find_item()
            i = i + 1
            if i > 20:
                return False
            logger.debug("Cho xuat hien {} lan {}".format(ProceedToRound.name, i))
            time.sleep(1)
        except pyscreeze.ImageNotFoundException:
            logger.error("khong tim thay hinh anh")

        except TypeError:
            logger.error("Khong tim thay hinh anh {}".format(ProceedToRound.name))
            return False


def exit_game():
    logger.info("Thoat game")
    click(Back, 0)
    click(Disconnect, 0)
    click(LeaveGame, 0)


def exit_game_round20():
    logger.info("Thoat game round 20")
    click(Back_On_Round20, 0)
    click(Disconnect, 0)
    click(LeaveGame, 0)


def enter_game():
    logger.info("Vao game")
    click(CreateCustomLobby, 1)
    click(ServerLocaltion, 1)
    click(ServerLocaltion_Singapore, 1)
    click(CreatePassLobby, 1)
    pyautogui.write("asx")  # add password
    click(CreateGame, 2)
    # time.sleep(4)
    click(StartGame, 2)
    click(Accept, 2)
    time.sleep(30)
    click(Confirm, 10)
    # click(ChallengeMax, 2)
    click(Challenge, 2)
    click(SelectCharacter, 2)
    pyautogui.moveTo(100, 100)
    click(Prepare, 2)


def roll_game():
    click(Roll, 0)


def click_procceed_to_round():
    click(ProceedToRound)


def next_round():
    logger.info("Next round")
    click(ProceedToRound)
    check_proceed_to_round()
