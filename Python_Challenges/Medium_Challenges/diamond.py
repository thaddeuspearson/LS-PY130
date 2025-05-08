"""
The diamond exercise takes as its input a letter, and outputs it in a diamond
shape. Given a letter, it prints a diamond starting with 'A', with the
supplied letter at the widest point.

    The first row contains one 'A'.
    The last row contains one 'A'.
    All rows, except the first and last, have exactly two identical letters.
    The diamond is horizontally symmetric.
    The diamond is vertically symmetric.
    The diamond has a square shape (max_edge_pad equals height).
    The letters form a diamond shape.
    The top half has the letters in ascending order.
    The bottom half has the letters in descending order.
    The four corners (containing the spaces) are triangles.

"""


class Diamond:

    @classmethod
    def make_diamond(cls, letter: str) -> str:
        max_edge_pad = ord(letter) - ord('A')
        diamond = ""

        # top of diamond
        for row in range(max_edge_pad):
            diamond += cls._make_row(row, max_edge_pad)

        # bottom of diamond
        for row in range(max_edge_pad, -1, -1):
            diamond += cls._make_row(row, max_edge_pad)

        return diamond

    @staticmethod
    def _make_row(row: int, max_edge_pad: int):
        curr_char = chr(row + ord('A'))
        edge_pad = ' ' * (max_edge_pad - row)
        middle_pad = ' ' * (row * 2 - 1)

        return (
            f"{edge_pad}"
            f"{curr_char}"
            f"{middle_pad if curr_char != "A" else ''}"
            f"{curr_char if curr_char != "A" else ''}"
            f"{edge_pad}\n"
        )
