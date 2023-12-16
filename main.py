import round as r
import win32gui
import time

def get_app_window_handle(app_name):
    hwnd = win32gui.FindWindow(None, app_name)
    return hwnd

app_name = "Dota 2"
new_x, new_y = 0, 0  # Tọa độ mới bạn muốn di chuyển cửa sổ đến

hwnd = get_app_window_handle(app_name)

if hwnd:
    time.sleep(1)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)
   
else:
    print(f"Không tìm thấy cửa sổ có tên '{app_name}'")

#r.round_1()
#r.click_image(button.bt_Prepare)
#r.get_round(button.bt_ProceedToRound2)
r.buy_hero_Luna(1)
