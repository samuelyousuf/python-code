# Populate a list with a string, integer, and float values.

def populate_list():
    """This function starts with an empty list and takes three inputs from the user to populate that list."""
    
    empty_List = []

    input_1 = input("Enter your string here: ")

    input_2 = float(input("Enter your floating point number here: "))

    input_3 = int(input("Enter your integer number here: "))


    empty_List.append(input_1)
    empty_List.append(input_2)
    empty_List.append(input_3)

    return empty_List

