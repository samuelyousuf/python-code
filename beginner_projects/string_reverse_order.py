# Return a string in reverse order.

def reverse_string(this_str):
    """This function returns a string with the words in reverse order."""

    # split the string input by each space to make a new list of strings
    new_str = this_str.split()

    # reverse the order of the list of string elements
    new_str = new_str[::-1]

    # join back the word elements using spaces between them
    new_str = " ".join(new_str)

    return new_str

