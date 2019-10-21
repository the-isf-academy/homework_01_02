# Homework 01_02 Practice with functions
# Author: Your name

from pathlib import Path

def get_words():
    """
    Reads the 10,000 most common English words from a file and returns them as a list.
    input: none
    output: a list of strings
    """
    filename = "10k_english_words.txt"
    return Path(filename).read_text().split()

def has_five_letters(word):
    """
    Checks whether the word has five letters
    input: str
    output: bool
    """
    pass

def count_five_letter_words(list_of_words):
    """
    Counts how many of list_of_words have five letters.
    input: list of str
    output: int
    """
    pass

def average(list_of_numbers):
    """
    Returns the average (mean) of a list of numbers.
    input: list of ints (or floats)
    output: float
    """
    pass

def average_word_length(list_of_words):
    """
    Returns the average word length of a list of words.
    input: list of str
    output: float
    """
    pass


if __name__ == "__main__":
    words = get_words()
    print("Useless facts about the 10,000 most common words in English:")
    print("{} of these words have five letters.".format(count_five_letter_words(words)))
    print("The average word length is {}".format(average_word_length(words)))
