import sys
import Todo

if '__main__' == __name__:
    if sys.argv[1]:
        file_name = sys.argv[1]
    else:
        file_name = 'sample'
    if sys.argv[2]:
        todo = sys.argv[2]
    else:
        todo = 'new todo'
    Todo.write_todo(file_name, todo)