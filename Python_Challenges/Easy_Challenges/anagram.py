"""
Write a program that takes a word and a list of possible anagrams and selects
the correct sub-list that contains the anagrams of the word.

For example, given the word "listen" and a list of candidates like "enlists",
"google", "inlets", and "banana", the program should return a list containing
"inlets". Please read the test suite for the exact rules of anagrams.
"""


class Anagram:
    def __init__(self, word: str) -> None:
        self.word = word.lower()

    @staticmethod
    def get_char_counts(word: str) -> int:
        char_count = {}
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

    def match(self, words: list) -> list:
        word_char_counts = Anagram.get_char_counts(self.word)
        return [
            candidate for candidate in words
            if candidate.lower() != self.word and
            Anagram.get_char_counts(candidate.lower()) == word_char_counts
        ]
