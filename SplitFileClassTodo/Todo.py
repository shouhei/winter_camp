import tempfile
import os


class Todo:

    def __init__(self, list_name="sample"):
        self.__list_name = list_name
        self.__todo = []

    def get_list_name(self):
        return self.__list_name

    def add(self, todo):
        self.__todo.append(todo)

    def get_all(self):
        return self.__todo

    def get_at(self,index):
        if len(self.__todo):
            return self.__todo[index]

    def remove(self, todo_index):
        del self.__todo[todo_index]