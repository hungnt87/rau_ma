import round as r
import win32gui
import win32con
import time
import keyboard
import button
import item
import hero

def get_app_window_handle(app_name):
    hwnd = win32gui.FindWindow(None, app_name)
    return hwnd
def move_window_to(handle, x, y):
    # Lấy kích thước hiện tại của cửa sổ
    _, _, width, height = win32gui.GetWindowRect(handle)

    # Thay đổi kích thước và vị trí của cửa sổ
    win32gui.SetWindowPos(handle, win32con.HWND_TOP, x, y, width, height, 0)
app_name = "Dota 2"
new_x, new_y = 0, 0  # Tọa độ mới bạn muốn di chuyển cửa sổ đến

hwnd = get_app_window_handle(app_name)

if hwnd:
    time.sleep(1)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)
    move_window_to(hwnd,new_x,new_y)
    print(f"Tim thay cua so  '{app_name}'")
    print("Bat dau auto")
    time.sleep(1)
    #r.round_1()
  
    # r.round_2()
  
    # r.round_3()

    # r.round_4()

    # r.round_5()


    #hero.buy_hero_Windranger(1)
    #item.buy_Investment_lv1_precise()
    # if item.check_item(item.ShopDiscount):
    #     print("co hang")
    #hero.buy_hero_infor(hero.WinterWyvern,5)
    button.exit_game()
    print("Ket thuc auto")

   
else:
    print(f"Không tìm thấy cửa sổ có tên '{app_name}'")

