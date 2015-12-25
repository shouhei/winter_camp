import sys
if "__main__" == __name__:
    if sys.argv[0]:
        file_name = sys.argv[1]
    else:
        file_name = 'sample'
    with open(file_name+".todo","r") as file:
        data_raw = file.read()
        data_list = data_raw.split("\n")
        for data in data_list:
            if data != "":
                print(data)