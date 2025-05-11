"""
Create a custom set type.

Sometimes it is necessary to define a custom data structure of some type. In
some languages, including Python, there is a built-in Set type. For this
problem, you're expected to implement your own custom set type. How it works
internally doesn't matter, as long as it behaves like a set of unique elements
that can be manipulated in several well defined ways. Once you've reached a
solution, feel free to play around with using the built-in implementation of
Set.

For simplicity, you may assume that all elements of a set must be numbers.
"""


class CustomSet:
    def __init__(self, elements: list = None) -> None:
        self.elements = elements

    def __str__(self):
        return f"{{{', '.join(str(e) for e in self.elements.keys())}}}"

    def __eq__(self, other: "CustomSet") -> bool:
        return self.is_same(other)

    def __hash__(self):
        return hash(sorted(self.elements.keys()))

    @property
    def elements(self) -> dict:
        return self._elements

    @elements.setter
    def elements(self, elements: list) -> None:
        if not isinstance(elements, list | None):
            raise TypeError("elements must be a list or None")
        elements = {e: True for e in elements} if elements else {}
        self._elements = elements

    def is_empty(self) -> bool:
        return not self.elements

    def contains(self, element: int) -> bool:
        return element in self.elements if self.elements else False

    def is_subset(self, superset: "CustomSet") -> bool:
        if not isinstance(superset, CustomSet):
            return NotImplemented
        return all(superset.contains(elem) for elem in self.elements)

    def is_disjoint(self, other: "CustomSet") -> bool:
        if not isinstance(other, CustomSet):
            return NotImplemented
        return not any(other.contains(elem) for elem in self.elements)

    def is_same(self, other: "CustomSet") -> bool:
        if not isinstance(other, CustomSet):
            return NotImplemented
        return self.is_subset(other) and other.is_subset(self)

    def add(self, element: int) -> None:
        if not isinstance(element, int):
            return NotImplemented
        self.elements.setdefault(element, True)

    def intersection(self, other: "CustomSet") -> "CustomSet":
        if not isinstance(other, CustomSet):
            return NotImplemented
        return CustomSet(
            sorted([elem for elem in self.elements if other.contains(elem)])
        )

    def difference(self, other: "CustomSet") -> "CustomSet":
        if not isinstance(other, CustomSet):
            return NotImplemented
        return CustomSet(
            sorted([elem for elem in self.elements if not other.contains(elem)])
        )

    def union(self, other: "CustomSet") -> "CustomSet":
        if not isinstance(other, CustomSet):
            return NotImplemented
        return CustomSet(
            list((self.elements | other.elements).keys())
        )
