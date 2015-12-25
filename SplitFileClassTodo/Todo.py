import tempfile
import os


class Todo:

    def __init__(self):
        self.todo = []

    def add(self, todo):
        self.todo.append(todo)

    def read(self):
        return self.todo

    def remove(self, todo_index):
        del self.todo[todo_index]