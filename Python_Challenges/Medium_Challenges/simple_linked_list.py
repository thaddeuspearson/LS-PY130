"""
Write a simple linked list implementation. The linked list is a fundamental
data structure in computer science, often used in the implementation of other
data structures.

The simplest kind of linked list is a singly linked list. Each element in the
list contains data and a "next" field pointing to the next element in the list
of elements. This variant of linked lists is often used to represent sequences
or push-down stacks (also called a LIFO stack; Last In, First Out).

Let's create a singly linked list whose elements may contain a range of data
such as the numbers 1-10. Provide methods to reverse the linked list and
convert a linked list to and from a list.
"""


class Element:
    def __init__(self, datum, next_elem: "Element" = None) -> None:
        self.datum = datum
        self.next = next_elem

    @property
    def datum(self):
        return self._datum

    @datum.setter
    def datum(self, datum) -> None:
        self._datum = datum

    @property
    def next(self) -> "Element":
        return self._next

    @next.setter
    def next(self, next: "Element") -> None:
        if next is not None and not isinstance(next, Element):
            raise TypeError("next must be an Element or None")
        self._next = next

    def is_tail(self) -> bool:
        return not self.next


class SimpleLinkedList:
    def __init__(self):
        self.head = None

    @classmethod
    def from_list(cls, lst: list) -> "SimpleLinkedList":
        new_llst = cls()
        if lst:
            for elem in reversed(lst):
                new_llst.push(elem)
        return new_llst

    @property
    def head(self) -> "Element":
        return self._head

    @head.setter
    def head(self, head) -> None:
        if head is not None and not isinstance(head, Element):
            raise TypeError("next must be an Element or None")
        self._head = head

    @property
    def size(self):
        elem_count = 0
        next_elem = self.head

        while next_elem:
            elem_count += 1
            next_elem = next_elem.next

        return elem_count

    def push(self, datum):
        next_elem = self.head if self.head else None
        self.head = Element(datum, next_elem)

    def peek(self):
        return self.head.datum if self.head else None

    def pop(self):
        if self.head:
            popped = self.head.datum
            self.head = self.head.next
            return popped
        return None

    def to_list(self) -> list:
        new_lst = []
        curr_elem = self.head
        while curr_elem:
            new_lst.append(curr_elem.datum)
            curr_elem = curr_elem.next
        return new_lst

    def reverse(self) -> "SimpleLinkedList":
        reversed_llst = SimpleLinkedList()
        curr_elem = self.head

        while curr_elem:
            reversed_llst.push(curr_elem.datum)
            curr_elem = curr_elem.next
        return reversed_llst

    def is_empty(self) -> bool:
        return not self.head
