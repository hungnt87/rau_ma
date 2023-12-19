import round as r
import win32gui
import win32con
import time
import button

app_name = "Dota 1"
new_x, new_y = -1, 0  # Tọa độ mới bạn muốn di chuyển cửa sổ đến


def get_app_window_handle(app_name):
    hwnd = win32gui.FindWindow(None, app_name)
    return hwnd


def move_window_to(handle, x, y):
    # Lấy kích thước hiện tại của cửa sổ
    _, _, width, height = win32gui.GetWindowRect(handle)

    # Thay đổi kích thước và vị trí của cửa sổ
    win32gui.SetWindowPos(handle, win32con.HWND_TOP, x, y, width, height, 0)


hwnd = get_app_window_handle(app_name)

if hwnd:
    time.sleep(1)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)
    move_window_to(hwnd, new_x, new_y)
    print(f"Tim thay cua so  '{app_name}'")

    for n in range(0, 10):
        print("Bat dau auto lan: ", n)
        time.sleep(1)
        r.round_1()

        r.round_2()

        r.round_3()

        r.round_4()

        r.round_5()
        r.round_6()

        r.round_7()

        r.round_8()

        r.round_9()

        r.round_10()
        r.round_11()

        r.round_12()

        r.round_13()

        r.round_14()

        r.round_15()
        r.round_16()

        r.round_17()

        r.round_18()

        r.round_19()

        r.round_20()
        # if button.check_not_money():
        #     print("false")

        # hero.buy_hero_Windranger(1)
        # item.buy_Investment_lv1_precise()
        # if item.check_item(item.ShopDiscount):
        #     print("co hang")
        # hero.buy_hero_infor(hero.WinterWyvern,5)
        # button.check_FindItem()
        button.exit_game()
        print("Ket thuc auto lan ", n)

        time.sleep(20)


else:
    print(f"Không tìm thấy cửa sổ có tên '{app_name}'")
