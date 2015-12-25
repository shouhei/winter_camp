if "__main__" == __name__:
    with open("sample.todo","r") as file:
        data_raw = file.read()
        data_list = data_raw.split("\n")
        for data in data_list:
            print(data)