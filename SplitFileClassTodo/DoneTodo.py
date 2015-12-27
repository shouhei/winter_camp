from File import File
from Todo import Todo
import tempfile

if "__main__" == __name__:
    file = File("sample.todo")
    todo_list = Todo("sample")
    for line in file.read():
        todo_list.add(line)
    temp_file_name = str(tempfile.mkstemp(dir=".")[1])
    tmp_file = File(temp_file_name)
    todo_list.remove(3)
    for todo in todo_list.get_all():
        tmp_file.write_line(todo)
    tmp_file.rename(file.get_file_name())
