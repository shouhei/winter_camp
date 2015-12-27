from Todo import Todo
from unittest import TestCase

class TodoTestCase(TestCase):

    def test_get_all(self):
        todo = Todo("test")
        self.assertListEqual(todo.get_all(), [])

    def test_add(self):
        todo = Todo("test")
        todo.add("hoge")
        self.assertListEqual(todo.get_all(), ["hoge"])

    def test_remove(self):
        todo = Todo("test")
        todo.add("hoge")
        todo.add("fuga")
        todo.add("piyo")
        todo.remove(1)
        self.assertListEqual(todo.get_all(), ["hoge", "piyo"])

    def test_get_at(self):
        todo = Todo("test")
        todo.add("hoge")
        todo.add("fuga")
        todo.add("piyo")
        self.assertEqual(todo.get_at(0), "hoge")

    def test_get_list_name(self):
        todo = Todo("test")
        self.assertEqual(todo.get_list_name(), "test")

    def test_get_list_name_default(self):
        todo = Todo()
        self.assertEqual(todo.get_list_name(), "sample")