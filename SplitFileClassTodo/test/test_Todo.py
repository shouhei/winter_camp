from Todo import Todo
from unittest import TestCase

class TodoTestCase(TestCase):

    def test_read(self):
        todo = Todo()
        self.assertListEqual(todo.read(), [])

    def test_add(self):
        todo = Todo()
        todo.add("hoge")
        self.assertListEqual(todo.read(), ["hoge"])

    def test_remove(self):
        todo = Todo()
        todo.add("hoge")
        todo.add("fuga")
        todo.add("piyo")
        todo.remove(1)
        self.assertListEqual(todo.read(), ["hoge", "piyo"])