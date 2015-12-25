from ClassedGitHubAPI import GitHubAPI
from unittest import TestCase, mock
from http.client import HTTPResponse

class GitHubAPITestCase(TestCase):

    def test_get_users_events(self):
        github = GitHubAPI("shouhei")
        with mock.patch('urllib.request.urlopen') as m:
            raw_data = m.return_value
            raw_data.read.return_value = "{}".encode()
            self.assertDictEqual(github.get_user_events(), {})
