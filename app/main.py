import tkinter as tk
from main_page import MainPage
from db_service import DBService
from todo import ToDo
from decouple import config


root = tk.Tk()
root.title("ToDo App")

path = config('PTH')
imgPath = f'{path}icon.png'
root.iconbitmap(imgPath)

root.geometry("800x600")

main_page = MainPage(root)
mainFrame = tk.Frame(root)
root.mainloop()