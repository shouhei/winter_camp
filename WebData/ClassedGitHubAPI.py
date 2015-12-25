from urllib import request
import json


class GitHubAPI:
    _URL = "https://api.github.com/users"

    def __init__(self, user_name):
        self._user_name = user_name
        self._user_events = None

    def get_user_events(self, refresh=False):
        if refresh or self._user_events is None:
            raw_data = request.urlopen("https://api.github.com/users/"+self._user_name+"/events")
            self._user_events = json.loads(raw_data.read().decode())
        return self._user_events


if "__main__" == __name__:
    github = GitHubAPI('shouhei')
    dict_data = github.get_user_events()
    print(dict_data[0]['created_at'] + ' :' + dict_data[0]['type'])
    print(dict_data[0]['repo']['url'])