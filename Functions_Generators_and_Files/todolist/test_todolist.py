import unittest
from todolist import Todo, TodoList


class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        self.assertIsInstance(self.todos.to_list(), list)
        self.assertEqual([self.todo1, self.todo2, self.todo3],
                         self.todos.to_list())

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())

    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())

    def test_all_done(self):
        self.assertFalse(self.todos.all_done())

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add("Billy Bob Thornton")

    def test_todo_at(self):
        with self.assertRaises(IndexError):
            self.todos.todo_at(4)

    def test_mark_done_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(5)
        self.todos.mark_done_at(1)
        self.assertTrue(self.todo2.done)

    def test_mark_undone_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(5)
        self.todos.mark_undone_at(1)
        self.assertFalse(self.todo2.done)

    def test_mark_all_done(self):
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done())

    def test_remove_at(self):
        with self.assertRaises(IndexError):
            self.todos.remove_at(5)
        todo = self.todos.remove_at(2)
        self.assertEqual(2, len(self.todos))
        self.todos.add(todo)

    def test_str(self):
        expected = (
            "----- Today's Todos -----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym"
        )
        self.assertEqual(expected, str(self.todos))

    def test_str_done_todo(self):
        self.todos.mark_done_at(0)
        expected = "[X] Buy milk"
        self.assertEqual(expected, str(self.todos.first()))
        self.todos.mark_undone_at(0)

    def test_str_all_done_todos(self):
        self.todos.mark_all_done()
        expected = (
            "----- Today's Todos -----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[X] Go to the gym"
        )
        self.assertEqual(expected, str(self.todos))
        self.todos.mark_all_undone()

    def test_each(self):
        expected = []
        self.todos.each(lambda t: expected.append(isinstance(t, Todo)))
        self.assertTrue(all(expected))

    def test_select(self):
        self.todos.mark_done_at(0)
        expected = self.todos.select(lambda t: t.done)
        self.assertEqual(self.todos.first(), expected.first())


if __name__ == "__main__":
    unittest.main()
