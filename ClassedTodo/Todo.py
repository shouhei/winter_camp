import tempfile
import os


class Todo:
    ext = ".todo"

    def __init__(self, file_name):
        self.file_name = file_name

    def write_todo(self, todo):
        with open(self.file_name + self.ext,"a") as file:
            file.write(todo+"\n")

    def read_todo(self):
        with open(self.file_name + self.ext,"r") as file:
            data_raw = file.read()
            data_list = data_raw.split("\n")
            for data in data_list:
                if data != "":
                    print(data)

    def done_todo(self, todo_index):
        with open(self.file_name + self.ext) as file:
            raw_data = file.read()
            data_list = raw_data.split("\n")
            if data_list[todo_index]:
                del data_list[todo_index]
            temp_file_name = str(tempfile.mkstemp(dir=".")[1])
            with open(temp_file_name, "w") as temp_file:
                for data in data_list:
                    if data != "":
                        temp_file.write(data + "\n")
                os.rename(temp_file_name, self.file_name + self.ext)