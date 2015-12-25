from urllib import request
import json

if "__main__" == __name__:
    raw_data = request.urlopen("https://api.github.com/users/shouhei/events")
    utf8_data = raw_data.read().decode()
    dict_data = json.loads(utf8_data)
    print(dict_data[0]['created_at'] + ' :' + dict_data[0]['type'])
    print(dict_data[0]['repo']['url'])