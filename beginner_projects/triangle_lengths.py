# Triangle lengths algorithm

def triangle_lengths():
    """This program takes three number values and determines whether or not the triangle is an equilateral triangle."""
    
    print("This program asks you to submit three lengths for a triangle, and then determine whether all lengths are equal.")
    
    length_one = int(input("Enter a length for side one: "))
    length_two = int(input("Enter a length for side two: "))
    length_three = int(input("Enter a length for side three: "))

    if length_one and length_two == length_three:
        return "This is an equilateral triangle!"
    else:
        return "This is not an equilateral triangle. Try again!"

