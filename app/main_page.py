import tkinter as tk
from tkinter import *
from app.add_todo import AddTodo
from db_service import DBService

class MainPage:
    def __init__(self, mainroot):
        self.mainPageRoot = mainroot

        self.dbService = DBService()
        todos = self.dbService.get_todos()

        todoFrame = tk.Frame(self.mainPageRoot)
        todoFrame.pack(expand=True)

        for todo in todos:
            var = tk.IntVar()
            chk = tk.Checkbutton(todoFrame, text=todo, variable=var,
                                 command=lambda lToDo=todo, lVar=var: self.updateTodo(lToDo, lVar))
            chk.pack(anchor="w")

        formButton = tk.Button(todoFrame, text="Add ToDo", command=self.on_button_click)
        formButton.pack()
        clearButton = Button(self, text="Clear", command= lambda: self.clear_todos())
        clearButton.pack()

    def updateTodo(self, todo, var):
        print(var.get())
        self.dbService.update_todo(todo, var.get())

    def on_button_click(self):
        AddTodo(self.mainPageRoot)

    def clear_todos(self):
        pass