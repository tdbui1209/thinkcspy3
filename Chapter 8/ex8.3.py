def count_letter(string, letter):
    """Return the number of characters in a string
    with given string and letter.
    """
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count
