"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    for item in items:
        string_item = str(item)
        if string_item in frequencies:
            frequencies[string_item] += 1
        else:
            frequencies[string_item] = 1
    return frequencies
