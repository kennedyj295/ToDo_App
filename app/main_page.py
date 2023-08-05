import tkinter as tk
from tkinter import *
from db_service import DBService

class MainPage:
    def __init__(self, mainroot):
        mainPageRoot = mainroot

        self.dbService = DBService()
        todos = self.dbService.get_todos()

        todoFrame = tk.Frame(mainPageRoot)
        todoFrame.pack(expand=True)

        for todo in todos:
            # todoList.insert('end', todo)
            var = tk.IntVar()
            chk = tk.Checkbutton(todoFrame, text=todo, variable=var,
                                 command=lambda lToDo=todo, lVar=var: self.updateTodo(lToDo, lVar))
            chk.pack(anchor="w")

    def updateTodo(self, todo, var):
        self.dbService.update_todo(todo, var.get())

