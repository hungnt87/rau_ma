import psutil
import win32process, win32gui

hwnd = win32gui.GetForegroundWindow()
_,pid = win32process.GetWindowThreadProcessId(hwnd)
process = psutil.Process(pid)

process_name = process.name()
print(process_name)
from pynput.keyboard import HotKey, Key, KeyCode, Listener


def function_1():
    click_image(button.bt_CreateCustomLobby)
    click_image(button.bt_ServerLocaltion)
    click_image(button.bt_ServerLocaltion_Singapore)
    click_image(button.bt_CreatePassLobby)
    click_image(button.bt_CreateGame)
    click_image(button.bt_StartGame)

def function_2():
    print('Function 2 activated')


hotkey1 = HotKey(
    [Key.ctrl, KeyCode(char='p')],
    function_1
)

hotkey2 = HotKey(
    [Key.ctrl, KeyCode(char='t')],
    function_1
)

hotkey3 = HotKey(
    [Key.alt, Key.ctrl, KeyCode(char='y')],
    function_2
)

hotkeys = [hotkey1, hotkey2, hotkey3]


def signal_press_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.press(l.canonical(key))

def signal_release_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.release(l.canonical(key))

with Listener(on_press=signal_press_to_hotkeys, on_release=signal_release_to_hotkeys) as l:
    l.join()