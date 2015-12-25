import os


class File:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_file_name(self):
        return self.file_name

    def write_line(self, data):
        with open(self.file_name,"a") as file:
            file.write(data+"\n")

    def read(self):
        with open(self.file_name, "r") as file:
            data_raw = file.read()
        if data_raw:
            data_list = data_raw.split("\n")
            if data_list[-1] == "":
                del data_list[-1]
            return data_list
        else:
            return []

    def override_file(self, other_file_name):
        os.rename(self.file_name, other_file_name)