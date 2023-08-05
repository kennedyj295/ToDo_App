import tkinter as tk
from tkinter import *
from db_service import DBService
from app.todo import ToDo


class AddTodo(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.dbService = DBService()

        self.title("Add ToDo")
        self.geometry('800x600')

        self.heading_var = StringVar()
        self.body_var = StringVar()

        Label(self, text="Heading").pack()
        heading_entry = Entry(self, textvariable=self.heading_var)
        heading_entry.pack()

        Label(self, text="Body").pack()
        body_entry = Entry(self, textvariable=self.body_var)
        body_entry.pack()

        Button(self, text="Submit", command=lambda: self.submit_data(self.heading_var.get(), self.body_var.get())).pack()


    def submit_data(self, head, body):
        todo = ToDo(head, body)
        self.dbService.add_todo(todo)
