from Todo import Todo
from File import File

if "__main__" == __name__:
    file = File("sample.todo")
    todo_list = Todo("sample")
    for line in file.read():
        todo_list.add(line)
    for todo in todo_list.get_all():
        print(todo)
