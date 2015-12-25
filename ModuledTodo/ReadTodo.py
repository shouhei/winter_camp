import sys
import Todo

if '__main__' == __name__:
    if sys.argv[1]:
        file_name = sys.argv[1]
    else:
        file_name = 'sample'
    Todo.read_todo(file_name)