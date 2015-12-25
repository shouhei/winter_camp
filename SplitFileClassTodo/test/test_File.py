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
        self.assertListEqual(data, ["hoge","huga", "piyo"])

    def test_write(self):
        file = File("test.txt")
        file.write_line("puyo")
        self.assertListEqual(file.read(), ["hoge", "huga", "piyo", "puyo"])

    def test_rename(self):
        huga = File("huga.txt")
        huga.write_line("1")
        huga.write_line("2")
        huga.rename("piyo.txt")
        piyo = File("piyo.txt")
        self.assertListEqual(piyo.read(),["1", "2"])
        os.remove("piyo.txt")

    def tearDown(self):
        os.remove("test.txt")