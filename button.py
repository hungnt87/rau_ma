import pyautogui
import time


class bt_infor():
    def __init__(self, para_name):
        self.name = para_name
        self.img = "data\\image\\"+para_name+".png"


Back = bt_infor("Back")
Disconnect = bt_infor("Disconnect")
LeaveGame = bt_infor("LeaveGame")
CreateCustomLobby = bt_infor("CreateCustomLobby")
CreateCustomLobby = bt_infor("CreateCustomLobby")
ServerLocaltion = bt_infor("ServerLocaltion")
ServerLocaltion_Singapore = bt_infor("ServerLocaltion_Singapore")
CreatePassLobby = bt_infor("CreatePassLobby")
CreateGame = bt_infor("CreateGame")
StartGame = bt_infor("StartGame")
Accept = bt_infor("Accept")
Confirm = bt_infor("Confirm")
Challenge = bt_infor("Challenge")
ChallengeMax= bt_infor("ChallengeMax")
SelectCharacter = bt_infor("SelectCharacter")
Prepare = bt_infor("Prepare")
ProceedToRound2 = bt_infor("ProceedToRound2")
Roll = bt_infor("Roll")
ProceedToRound = bt_infor("ProceedToRound")
ProceedToRound3 = bt_infor("ProceedToRound3")
ProceedToRound4 = bt_infor("ProceedToRound4")
ProceedToRound5 = bt_infor("ProceedToRound5")
ProceedToRound6 = bt_infor("ProceedToRound6")
ProceedToRound7 = bt_infor("ProceedToRound7")
ProceedToRound8 = bt_infor("ProceedToRound8")
ProceedToRound9 = bt_infor("ProceedToRound9")
ProceedToRound10 = bt_infor("ProceedToRound10")
ProceedToRound11 = bt_infor("ProceedToRound11")
ProceedToRound12 = bt_infor("ProceedToRound12")
ProceedToRound13 = bt_infor("ProceedToRound13")
ProceedToRound14 = bt_infor("ProceedToRound14")
ProceedToRound15 = bt_infor("ProceedToRound15")
ProceedToRound16 = bt_infor("ProceedToRound16")
ProceedToRound17 = bt_infor("ProceedToRound17")
ProceedToRound18 = bt_infor("ProceedToRound18")
ProceedToRound19 = bt_infor("ProceedToRound19")
ProceedToRound20 = bt_infor("ProceedToRound20")
Resurrect = bt_infor("Resurrect")
NotMoney = bt_infor("NotMoney")
Recycle = bt_infor("Recycle")
Abandon=bt_infor("Abandon")


def click(bt_infor, time_sleep=0):

    i = 0
    while True:
        try:
            

            res = pyautogui.locateOnScreen(
                bt_infor.img, confidence=0.8, region=(0, 0, 1916, 1134))
            if res is not None and time_sleep>0:
                print("Cho xuat hien {} trong thoi gian {}".format(bt_infor.name,time_sleep))
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
            i = i+1
            if i > 120:
                break
            print("Đang tìm hình ảnh button {} so lan {}".format(bt_infor.name, i))
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
            i = i+1
            if i > 2:
                break
            print("Đang kiem tra ban co tien khong so lan ", i)
            time.sleep(0.2)


def check_FindItem():
    i=0   
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
            i = i+1
            if i > 2:
                break
            print("Đang kiem tra co ruong do rot ko ", i)
            time.sleep(0.2)

def check_Resurrect(time_wait=10):
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
            i = i+1
            if i > time_wait:
                break
            print("cho xuat hien Resurrect", i)
            time.sleep(1)
def check_Abandon(time_wait=2):
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
            i = i+1
            if i > time_wait:
                break
            print("cho xuat hien Abandon", i)
            time.sleep(1)
def check_ProceedToRound():
    check_Resurrect()    
    i = 0
    while True:
        try:
            check_Abandon()
            res = pyautogui.locateOnScreen(
                ProceedToRound.img, confidence=0.8, region=(0, 0, 1916, 1134))
            if res is not None:
                print("Cho xuat hien {} lan {}".format(ProceedToRound.name,i))
                time.sleep(1)
                return True                     
        except pyautogui.ImageNotFoundException:
            check_FindItem()            
            i = i+1
            if i > 200:
                break
            print("Cho xuat hien {} lan {}".format(ProceedToRound.name,i))
            time.sleep(1)
def exit_game():
    click(Back, 0)
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
    click(Prepare,0)


def roll_game():
    click(Roll, 0)


def next_round():
    click(ProceedToRound)
    check_ProceedToRound()
