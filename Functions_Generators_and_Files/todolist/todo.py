class Todo:
    """base component of a todo list"""
    COMPLETED = "X"
    INCOMPLETE = " "

    def __init__(self, title: str) -> None:
        self._title = title
        self._done = False

    def __str__(self):
        marker = Todo.COMPLETED if self.done else Todo.INCOMPLETE
        return f"[{marker}] {self.title}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Todo):
            return NotImplemented
        return (
            self.title == other.title and
            self.done == other.done
        )

    @property
    def title(self) -> str:
        return self._title

    @property
    def done(self) -> bool:
        return self._done

    @done.setter
    def done(self, done: bool):
        self._done = done


# Tests
def test_todo():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')
    todo4 = Todo('Clean room')

    assert str(todo1) == "[ ] Buy milk"
    assert str(todo2) == "[ ] Clean room"
    assert str(todo3) == "[ ] Go to gym"
    assert str(todo4) == "[ ] Clean room"

    assert todo2 == todo4
    assert not todo1 == todo2
    assert not todo4.done

    todo1.done = True
    todo4.done = True

    assert todo1.done
    assert todo4.done

    assert str(todo1) == "[X] Buy milk"
    assert str(todo2) == "[ ] Clean room"
    assert str(todo3) == "[ ] Go to gym"
    assert str(todo4) == "[X] Clean room"

    assert todo2 != todo4

    todo4.done = False

    assert not todo4.done
    assert str(todo4) == "[ ] Clean room"


if __name__ == "__main__":
    test_todo()
