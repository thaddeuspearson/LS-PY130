"""
Write a program that prints the longest sentence in a string based on the
number of words. You should also print the number of words in the longest
sentence.

Sentences may end with periods (.), exclamation points (!), or question marks
(?). You should treat any sequence of characters that are not spaces or
sentence-ending characters as a word. Thus, -- should count as a word. Log the
longest sentence and its word count. Pay attention to the expected output, and
be sure you preserve the punctuation from the end of the sentence.
"""


def longest_sentence(text: str) -> str:
    """
    Finds the longest sentence in a given text, where ending punctuation
    is a `!`, `.`, or `?`. Also returns the word count of the longest sentence
    """
    longest = ''
    longest_count = 0
    punctuation = {".", "!", "?"}
    text_length = len(text)
    beginning = 0
    end = 0

    while True:
        while text[end] not in punctuation:
            end += 1

        curr_sentence = text[beginning:end+1]
        curr_sentence_word_count = len(curr_sentence.split(" "))

        if curr_sentence_word_count > longest_count:
            longest = curr_sentence
            longest_count = curr_sentence_word_count

        if end < text_length - 1:
            end += 2
            beginning = end
        else:
            break

    return longest, f"The longest sentence has {longest_count} words."


long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)


result = longest_sentence(long_text)
assert result[0] == (
    "Four score and seven years ago our fathers brought forth on this"
    " continent a new nation, conceived in liberty, and dedicated to"
    " the proposition that all men are created equal."
)
assert result[1] == "The longest sentence has 30 words."

result = longest_sentence(longer_text)
assert result[0] == (
    "It is rather for us to be here dedicated to the great task remaining"
    " before us -- that from these honored dead we take increased devotion to"
    " that cause for which they gave the last full measure of devotion -- that"
    " we here highly resolve that these dead shall not have died in vain --"
    " that this nation, under God, shall have a new birth of freedom -- and"
    " that government of the people, by the people, for the people, shall not"
    " perish from the earth."
)
assert result[1] == "The longest sentence has 86 words."

result = longest_sentence("Where do you think you're going? What's up, Doc?")
assert result[0] == "Where do you think you're going?"
assert result[1] == "The longest sentence has 6 words."

result = longest_sentence("To be or not to be! Is that the question?")
assert result[0] == "To be or not to be!"
assert result[1] == "The longest sentence has 6 words."
