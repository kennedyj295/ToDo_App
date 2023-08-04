from decouple import config
import pyodbc


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

    def add_todo(self):
        self.cursor

    def delete_todo(self, todo_id):
        self.cursor.execute("DELETE FROM todos WHERE ID = " + str(todo_id))
        self.conn.commit()
