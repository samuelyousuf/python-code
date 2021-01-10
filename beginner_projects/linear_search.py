# Basic linear search algorithm
def main(num, collection):
    """This function checks if an item is available within a sequential collection."""

    for index in range(len(collection)):
        if num == collection[index]:
            return True
    
    else:
        return False

