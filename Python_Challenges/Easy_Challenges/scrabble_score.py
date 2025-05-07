"""
Write a program that, given a word, computes the Scrabble score for that word.

Letter Values

You'll need the following tile scores:

    Letter 	                        Value
    A, E, I, O, U, L, N, R, S, T 	1
    D, G 	                        2
    B, C, M, P 	                    3
    F, H, V, W, Y 	                4
    K 	                            5
    J, X 	                        8
    Q, Z 	                        10

How to Score:

Sum the values of all the tiles used in each word. For instance, lets consider
the word CABBAGE which has the following letters and point values:

    3 points for C
    1 point for each A (there are two)
    3 points for B (there are two)
    2 points for G
    1 point for E

Thus, to compute the final total (14 points), we count:

    3 + 2*1 + 2*3 + 2 + 1
    => 3 + 2 + 6 + 3
    => 5 + 9
    => 14

"""


class Scrabble:
    LETTER_POINTS = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
        'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    def __init__(self, word: str) -> None:
        self.word = word if word else ""

    def score(self) -> int:
        return sum([
            Scrabble.LETTER_POINTS[letter.upper()]
            for letter in self.word
            if letter.isalpha()
        ])

    @classmethod
    def calculate_score(cls, word) -> int:
        return cls(word).score()
