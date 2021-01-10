# Compares two lists and then returns a third list of the same elements.

def check_two_lists(a, b):
    """This function checks two lists and returns a third list of the same elements, without duplicates."""

    # Empty list to hold the same elements of both lists
    c = []

    for item in a:
        if item in b:
            c.append(item)

    return list(set(c))

