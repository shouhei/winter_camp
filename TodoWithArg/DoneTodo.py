import tempfile
import os
import sys

if "__main__" == __name__:
    if sys.argv[1]:
        file_name = sys.argv[1]
    else:
        file_name = 'sample'
    if sys.argv[2]:
        # 配列に対する操作なので、人間解釈的には-1必要
        todo_number = int(sys.argv[2]) - 1
    else:
        todo_number = 0
    with open(file_name+'.todo') as file:
        raw_data = file.read()
        data_list = raw_data.split("\n")
        if data_list[todo_number]:
            del data_list[todo_number]
        temp_file_name = str(tempfile.mkstemp(dir=".")[1])
        with open(temp_file_name, "w") as temp_file:
            for data in data_list:
                if data != "":
                    temp_file.write(data + "\n")
            os.rename(temp_file_name, file_name + ".todo")