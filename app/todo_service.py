from db_service import DBService

class ToDoService:
    def __init__(self):
        self.dbService = DBService()

    def add_todo(self, todo):
        self.dbService.add_todo(todo)

    def get_todos(self):
        return self.dbService.get_todos()

    def delete_todo(self, todo_id):
        return self.dbService.delete_todo(todo_id)

