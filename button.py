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
SelectCharacter = bt_infor("SelectCharacter")
Prepare = bt_infor("Prepare")
ProceedToRound2 = bt_infor("ProceedToRound2")
Roll = bt_infor("Roll")
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
NotMoney=bt_infor("NotMoney")


def click(bt_infor):
    i = 0
    while True:
        try:
            res = pyautogui.locateOnScreen(
                bt_infor.img, confidence=0.8, region=(0, 0, 1916, 1134))
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
            #res_center = pyautogui.center(res)
            #stime.sleep(1)   

            print("Ko du tien")
            return True
        except pyautogui.ImageNotFoundException:
            i = i+1
            if i > 5:
                break
            print("Đang kiem tra ban co tien khong so lan ", i)
            time.sleep(0.2)


    
def exit_game():
    click(Back)
    click(Disconnect)
    click(LeaveGame)


def enter_game():
    click(CreateCustomLobby)
    click(ServerLocaltion)
    click(ServerLocaltion_Singapore)
    click(CreatePassLobby)
    pyautogui.write("as")  # add password
    click(CreateGame)
    # time.sleep(4)
    click(StartGame)
    click(Accept)  # start game
    click(Confirm)
    click(Challenge)
    click(SelectCharacter)
    pyautogui.moveTo(100, 100)
    click(Prepare)


def roll_game():
    click(Roll)


def next_round_2():
    click(ProceedToRound2)


def next_round_3():
    click(ProceedToRound3)


def next_round_4():
    click(ProceedToRound4)


def next_round_5():
    click(ProceedToRound5)


def next_round_6():
    click(ProceedToRound6)


def next_round_7():
    click(ProceedToRound7)


def next_round_8():
    click(ProceedToRound8)
