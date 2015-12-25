import tempfile
import os


def write_todo(file_name, todo):
    with open(file_name+".todo","a") as file:
        file.write(todo+"\n")


def read_todo(file_name):
    with open(file_name+".todo","r") as file:
        data_raw = file.read()
        data_list = data_raw.split("\n")
        for data in data_list:
            if data != "":
                print(data)


def done_todo(file_name, todo_index):
    with open(file_name+'.todo') as file:
        raw_data = file.read()
        data_list = raw_data.split("\n")
        if data_list[todo_index]:
            del data_list[todo_index]
        temp_file_name = str(tempfile.mkstemp(dir=".")[1])
        with open(temp_file_name, "w") as temp_file:
            for data in data_list:
                if data != "":
                    temp_file.write(data + "\n")
            os.rename(temp_file_name, file_name + ".todo")