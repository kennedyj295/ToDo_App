import pyodbc
from decouple import config
from todo import ToDo


class DBService:

    def __init__(self):
        self.UID = config('UID')
        self.PWD = config('PWD')
        self.SRV = config('SRV')
        self.DTB = config('DTB')

        self.conn_str = (
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            fr'SERVER={self.SRV};'
            fr'DATABASE={self.DTB};'
            fr'UID={self.UID};'
            fr'PWD={self.PWD}'
        )

        self.conn = pyodbc.connect(self.conn_str)
        self.cursor = self.conn.cursor()

    def get_todos(self):
        self.cursor.execute("SELECT * FROM todos")

        for row in self.cursor.fetchall():
            print(row)

    def add_todo(self, todo):
        self.cursor.execute(
            "INSERT INTO todos (title, body, status) VALUES (?,?,?)",
            (todo.title, todo.body, todo.status)
        )
        self.conn.commit()


    def delete_todo(self, todo_id):
        self.cursor.execute("DELETE FROM todos WHERE ID = " + str(todo_id))
        self.conn.commit()

    def update_todo(self, status, todo_id):
        self.cursor.execute(
            "UPDATE todos SET status = ? WHERE id = ?",
            (status, todo_id)
        )
        self.conn.commit()
