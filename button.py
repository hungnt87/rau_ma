import pyautogui
import time


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
Back_On_Round20= ButtonInfor("Back_On_Round20")

def click(ButtonInfor, time_sleep=0):
    i = 0
    while True:
        try:

            res = pyautogui.locateOnScreen(
                ButtonInfor.img, confidence=0.8, region=(0, 0, 1916, 1134))
            if res is not None and time_sleep > 0:
                print("Cho xuat hien {} trong thoi gian {}".format(ButtonInfor.name, time_sleep))
                time.sleep(time_sleep)
            res_center = pyautogui.center(res)
            time.sleep(1)
            pyautogui.moveTo(res_center)
            pyautogui.click(res_center)
            time.sleep(0.2)
            pyautogui.moveTo(200, 200)
            # pyautogui.moveTo(0, 0)
            # print("I can see it")
            break
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > 120:
                break
            print("Đang tìm hình ảnh button {} so lan {}".format(ButtonInfor.name, i))
            time.sleep(0.5)


def check_not_money():
    i = 0
    while True:
        try:
            res = pyautogui.locateOnScreen(
                NotMoney.img, confidence=0.8, region=(0, 0, 1916, 1134))
            # res_center = pyautogui.center(res)
            # stime.sleep(1)

            print("Ko du tien")
            return True
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > 2:
                break
            print("Đang kiem tra ban co tien khong so lan ", i)
            time.sleep(0.2)


def check_find_item():
    i = 0
    while True:
        try:
            res = pyautogui.locateOnScreen(
                Recycle.img, confidence=0.8, region=(0, 0, 1916, 1134))
            res_center = pyautogui.center(res)
            pyautogui.moveTo(res_center)
            pyautogui.click(res_center)
            time.sleep(0.2)
            pyautogui.moveTo(200, 200)
            print("Khong lay item")
            return True
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > 2:
                break
            print("Đang kiem tra co ruong do rot ko ", i)
            time.sleep(0.2)


def check_resurrect(time_wait=10):
    i = 0
    while True:
        try:
            res = pyautogui.locateOnScreen(
                Resurrect.img, confidence=0.8, region=(0, 0, 1916, 1134))
            res_center = pyautogui.center(res)
            time.sleep(1)
            pyautogui.moveTo(res_center)
            pyautogui.click(res_center)
            print("Chon Resurrect ")

            for x in range(0, time_wait):
                print(" cho van dau", x)
                time.sleep(1)
            break
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > time_wait:
                break
            print("cho xuat hien Resurrect", i)
            time.sleep(1)


def check_abandon(time_wait=2):
    i = 0
    while True:
        try:
            res = pyautogui.locateOnScreen(
                Abandon.img, confidence=0.8, region=(0, 0, 1916, 1134))
            res_center = pyautogui.center(res)
            pyautogui.moveTo(res_center)
            pyautogui.click(res_center)
            print("Chon Abandon")
            for x in range(0, time_wait):
                print(" cho van dau", x)
                time.sleep(1)
            break
        except pyautogui.ImageNotFoundException:
            i = i + 1
            if i > time_wait:
                break
            print("cho xuat hien Abandon", i)
            time.sleep(1)


def check_proceed_to_round():
    check_resurrect()
    i = 0
    while True:
        try:
            check_abandon()
            res = pyautogui.locateOnScreen(
                ProceedToRound.img, confidence=0.8, region=(0, 0, 1916, 1134))
            if res is not None:
                print("Cho xuat hien {} lan {}".format(ProceedToRound.name, i))
                time.sleep(1)
                return True
        except pyautogui.ImageNotFoundException:
            check_find_item()
            i = i + 1
            if i > 200:
                break
            print("Cho xuat hien {} lan {}".format(ProceedToRound.name, i))
            time.sleep(1)


def exit_game():
    click(Back, 0)
    click(Disconnect, 0)
    click(LeaveGame, 0)
def exit_game_round20():
    click(Back_On_Round20,0)
    click(Disconnect, 0)
    click(LeaveGame, 0)


def enter_game():
    click(CreateCustomLobby)
    click(ServerLocaltion)
    click(ServerLocaltion_Singapore, 0)
    click(CreatePassLobby, 0)
    pyautogui.write("as")  # add password
    click(CreateGame, 0)
    # time.sleep(4)
    click(StartGame, 0)
    click(Accept, 0)

    click(Confirm, 10)
    click(ChallengeMax)
    click(Challenge, 0)
    click(SelectCharacter, 0)
    pyautogui.moveTo(100, 100)
    click(Prepare, 0)


def roll_game():
    click(Roll, 0)


def click_procceed_to_round():
    click(ProceedToRound)


def next_round():
    click(ProceedToRound)
    check_proceed_to_round()
