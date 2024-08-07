import json
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser

def center_window(root):
    """
    این تابع پنجره را در مرکز صفحه قرار می‌دهد.
    """
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 512
    window_height = 256
    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

def read_json_and_display(file_path, icon_path):
    """
    این تابع فایل JSON را خوانده و متن را در پنجره نمایش می‌دهد.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        message = data['message']  # فرض می‌کنیم پیام در فیلد 'message' فایل JSON قرار دارد

    root = tk.Tk()
    root.title("واحد فناوری اطلاعات")
    root.resizable(False, False)  # غیرفعال کردن دکمه ماکزیمایز
    center_window(root)

    # تنظیم آیکون پنجره
    icon = Image.open(icon_path)
    photo = ImageTk.PhotoImage(icon)
    root.iconphoto(False, photo)

    # ایجاد یک برچسب برای نمایش متن فارسی
    label = tk.Label(root, text=message, font=("B Nazanin", 13), wraplength=480)
    label.pack(fill=tk.BOTH, expand=True)

    # ایجاد دکمه لینک به گیت‌هاب
    github_button = tk.Button(root, text="Copyright © MIT License with ❤️in GitHub", command=lambda: webbrowser.open_new("https://github.com/farzadrahimi/Send-Alarm"))
    github_button.pack(pady=10)

    # همیشه روی پنجره‌های دیگر قرار بگیرد
    root.attributes('-topmost', True)

    root.mainloop()

# جایگزین کنید با مسیر فایل JSON خود، آدرس گیت‌هاب و مسیر آیکون
file_path = "message_fa.json"
icon_path = "icon.ico"  # جایگزین کنید با مسیر آیکون دلخواه
read_json_and_display(file_path, icon_path)