import tempfile
import os


class Todo:

    def __init__(self):
        self._todo = []

    def add(self, todo):
        self._todo.append(todo)

    def read(self):
        return self._todo

    def remove(self, todo_index):
        del self._todo[todo_index]