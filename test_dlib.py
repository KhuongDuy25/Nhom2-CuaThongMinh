import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()  # Ẩn cửa sổ chính

name = simpledialog.askstring("Nhập tên", "Bạn tên là gì?")
print(f"Tên bạn là: {name}")
