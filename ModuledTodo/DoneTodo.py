import sys
import Todo

if "__main__" == __name__:
    if sys.argv[1]:
        file_name = sys.argv[1]
    else:
        file_name = 'sample'
    if sys.argv[2]:
        # 配列に対する操作なので、人間解釈的には-1必要
        todo_index = int(sys.argv[2]) - 1
    else:
        todo_index = 0
    Todo.done_todo(file_name, todo_index)