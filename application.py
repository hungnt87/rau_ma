import win32gui
import win32con
import win32api
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
   
else:
    print(f"Không tìm thấy cửa sổ có tên '{app_name}'")