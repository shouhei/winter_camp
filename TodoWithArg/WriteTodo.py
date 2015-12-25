import sys
if "__main__" == __name__:
    if sys.argv[1]:
        file_name = sys.argv[1]
    else:
        file_name = 'sample'
    if sys.argv[2]:
        todo = sys.argv[2]
    else:
        todo = 'new todo'
    with open(file_name+".todo","a") as file:
        file.write(todo+"\n")