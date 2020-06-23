#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return (0)

    Dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    q = 0

    for i in range(0, len(roman_string)):
        if i > 0 and Dict[roman_string[i]] > Dict[roman_string[i - 1]]:
            q += Dict[roman_string[i]] - Dict[roman_string[i - 1]] * 2
        else:
            q += Dict[roman_string[i]]
    return (q)
