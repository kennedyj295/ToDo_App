import tkinter as tk
from main_page import MainPage
from db_service import DBService


dbService = DBService()
dbService.delete_todo(1)

# root = tk.Tk()
# root.geometry("1200x800")
# main_page = MainPage(root)
