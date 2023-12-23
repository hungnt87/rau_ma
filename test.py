import pygetwindow as gw

def get_app_resolution(app_name):
    try:
        app = gw.getWindowsWithTitle(app_name)[0]
        app_resolution = (app.width, app.height)
        return app_resolution
    except IndexError:
        print(f"Không tìm thấy ứng dụng có tên là '{app_name}'")
        return None

if __name__ == "__main__":
    app_name = "Dota 2"  # Thay thế bằng tên của ứng dụng bạn muốn kiểm tra
    resolution = get_app_resolution(app_name)

    if resolution:
        print(f"Độ phân giải của ứng dụng '{app_name}': {resolution[0]} x {resolution[1]} pixels")