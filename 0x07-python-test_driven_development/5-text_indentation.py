#!/usr/bin/python3
"""
Text identation
"""


def text_indentation(text):
    """
    text: variable

    Return: None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        i = 0
        for letter in text:
            if i == 0:
                if letter == "":
                    continue
                else:
                    i = 1

            if i == 1:
                if letter == '.' or letter == '?' or letter == ':':
                    print(letter)
                    print()
                    i = 0
                else:
                    print(letter, end="")
