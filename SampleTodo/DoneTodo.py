import tempfile
import os

if "__main__" == __name__:
    with open("sample.todo") as file:
        raw_data = file.read()
        data_list = raw_data.split("\n")
        if data_list[4]:
            del data_list[4]
        temp_file_name = str(tempfile.mkstemp(dir=".")[1])
        with open(temp_file_name, "w") as temp_file:
            for data in data_list:
                if data != "":
                    temp_file.write(data + "\n")
            os.rename(temp_file_name, "sample.todo")