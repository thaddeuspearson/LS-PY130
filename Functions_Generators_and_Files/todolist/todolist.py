from todo import Todo


class TodoList:
    """collection class for Todo instances"""

    def __init__(self, title: str) -> None:
        self._title = title
        self.todos = []

    def __str__(self):
        heading = f"----- {self.title} -----\n"
        return heading + "\n".join(str(todo) for todo in self.todos)

    def __len__(self):
        return len(self.todos)

    @property
    def title(self) -> str:
        return self._title

    @property
    def todos(self) -> list:
        return self._todos

    @todos.setter
    def todos(self, todos):
        self._todos = todos

    def add(self, todo: Todo) -> None:
        if not isinstance(todo, Todo):
            raise TypeError
        self._todos.append(todo)

    def first(self) -> Todo:
        first = self.todos[0]
        if not first:
            raise IndexError("Got it!")
        return first

    def last(self) -> Todo:
        last = self.todos[len(self.todos) - 1]
        if not last:
            raise IndexError("Got it!")
        return last

    def to_list(self) -> list:
        return self.todos.copy()

    def todo_at(self, index: int) -> Todo:
        return self.todos[index]

    def mark_done_at(self, index: int) -> None:
        self.todos[index].done = True

    def mark_undone_at(self, index: int) -> None:
        self.todos[index].done = False

    def remove_at(self, index: int) -> None:
        self.todos.pop(index)

    def mark_all_done(self) -> None:
        for idx in range(len(self)):
            self.mark_done_at(idx)

    def mark_all_undone(self) -> None:
        if self.todos:
            for idx in range(len(self) - 1, -1, -1):
                self.mark_undone_at(idx)

    def all_done(self) -> bool:
        return all(todo.done for todo in self.todos)

    def each(self, callback) -> None:
        for todo in self.todos:
            callback(todo)

    def select(self, callback):
        new_list = TodoList(self.title)

        self.each(
            lambda todo:
            new_list.add(todo) if callback(todo)
            else None
        )
        return new_list

    def find_by_title(self, title: str):
        return self.select(lambda todo: todo.title == title).todos[0]

    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)

    def mark_done(self, title: str) -> None:
        self.find_by_title(title).done = True


def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list


def line(num: int) -> str:
    return f"\n--------------------------------- Step {num}\n"


def step_1():
    print(line(1))
    todo_list = setup()

    try:
        todo_list.add(1)
    except TypeError:
        print('TypeError detected')

    for todo in todo_list.todos:
        print(todo)


def step_2():
    print(line(2))
    todo_list = setup()
    print(todo_list)


def step_3(empty_todo_list: Todo):
    print(line(3))
    todo_list = setup()

    assert len(todo_list) == 3
    assert len(empty_todo_list) == 0


def step_4(empty_todo_list):
    print(line(4))
    todo_list = setup()

    assert str(todo_list.first()) == "[ ] Buy milk"
    assert str(todo_list.last()) == "[ ] Go to gym"

    try:
        empty_todo_list.first()
    except IndexError:
        print('Expected IndexError: Got it!')

    try:
        empty_todo_list.last()
    except IndexError:
        print('Expected IndexError: Got it!')


def step_5(empty_todo_list):
    print(line(5))
    todo_list = setup()

    print(empty_todo_list.to_list())

    todos = todo_list.to_list()
    assert type(todos).__name__ == "list"
    assert todos is not todo_list

    for todo in todos:
        print(todo)


def step_6():
    print(line(6))
    todo_list = setup()

    assert str(todo_list.todo_at(0)) == "[ ] Buy milk"
    assert str(todo_list.todo_at(1)) == "[X] Clean room"
    assert str(todo_list.todo_at(2)) == "[ ] Go to gym"

    try:
        todo_list.todo_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

    # Ensure we have a reference
    assert todo_list.todo_at(1) is todo_list.todo_at(1)


def step_7():
    print(line(7))
    todo_list = setup()

    todo_list.mark_done_at(0)
    print(todo_list)

    todo_list.mark_done_at(1)
    print(todo_list)

    todo_list.mark_done_at(2)
    print(todo_list)

    try:
        todo_list.mark_done_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')

    todo_list.mark_undone_at(0)
    print(todo_list)

    todo_list.mark_undone_at(1)
    print(todo_list)

    todo_list.mark_undone_at(2)
    print(todo_list)

    try:
        todo_list.mark_undone_at(3)
    except IndexError:
        print('Expected IndexError: Got it!')


def step_8():
    print(line(8))
    todo_list = setup()

    print(todo_list)
    todo_list.mark_all_done()
    print(todo_list)

    todo_list.mark_all_undone()
    print(todo_list)


def step_9(empty_todo_list):
    print(line(9))
    todo_list = setup()

    assert not todo_list.all_done()

    todo_list.mark_all_done()
    assert todo_list.all_done()

    todo_list.mark_undone_at(1)
    assert not todo_list.all_done()
    assert empty_todo_list.all_done()


def step_10():
    print(line(10))
    todo_list = setup()

    print(todo_list)

    todo_list.remove_at(1)
    print(todo_list)

    todo_list.remove_at(1)
    print(todo_list)

    try:
        todo_list.remove_at(1)
    except IndexError:
        print('Expected IndexError: Got it!')

    todo_list.remove_at(0)
    print(todo_list)


def step_11():
    print(line(11))
    todo_list = setup()

    todo_list.mark_all_undone()
    print(todo_list)

    def done_if_y_in_title(todo):
        if 'y' in todo.title:
            todo.done = True

    todo_list.each(done_if_y_in_title)
    print(todo_list)

    todo_list.each(lambda todo: print('>>>', todo))


def step_12():
    print(line(12))
    todo_list = setup()

    def y_in_title(todo):
        return 'y' in todo.title

    print(todo_list.select(y_in_title))

    print(todo_list.select(lambda todo: todo.done))


def step_13():
    print(line(13))
    todo_list = setup()

    todo_list.add(Todo('Clean room'))
    print(todo_list)

    found = todo_list.find_by_title('Go to gym')
    print(found)

    found = todo_list.find_by_title('Clean room')
    print(found)

    try:
        todo_list.find_by_title('Feed cat')
    except IndexError:
        print('Expected IndexError: Got it!')


def step_14(empty_todo_list):
    print(line(14))
    todo_list = setup()

    done = todo_list.done_todos()
    print(done)

    undone = todo_list.undone_todos()
    print(undone)

    done = empty_todo_list.done_todos()
    print(done)

    undone = empty_todo_list.undone_todos()
    print(undone)


def step_15():
    print(line(15))
    todo_list = setup()

    todo_list.mark_done('Go to gym')
    print(todo_list)

    try:
        todo_list.mark_done('Feed cat')
    except IndexError:
        print('Expected IndexError: Got it!')


def tests():
    empty_todo_list = TodoList('Nothing Doing')
    step_1()
    step_2()
    step_3(empty_todo_list)
    step_4(empty_todo_list)
    step_5(empty_todo_list)
    step_6()
    step_7()
    step_8()
    step_9(empty_todo_list)
    step_10()
    step_11()
    step_12()
    step_13()
    step_14(empty_todo_list)
    step_15()


if __name__ == "__main__":
    tests()
