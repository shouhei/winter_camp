from File import File
import os
from unittest import TestCase

class FileTestCase(TestCase):
    def setUp(self):
        with open('test.txt','a') as test_file:
            test_file.write("hoge\n")
            test_file.write("huga\n")
            test_file.write("piyo\n")

    def test_read(self):
        file = File("test.txt")
        data = file.read()
        self.assertListEqual(data, ["hoge","huga", "piyo",""])

    def test_write(self):
        file = File("test.txt")
        file.write_line("puyo")
        self.assertListEqual(file.read(), ["hoge", "huga", "piyo", "puyo",""])

    def tearDown(self):
        os.remove("test.txt")