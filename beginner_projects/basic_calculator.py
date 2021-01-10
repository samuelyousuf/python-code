# Basic calculator

def basic_calculator(x, y):
    """This function mimics a basic calculator."""

    print("You will be asked to enter an arithmetic operator. For example: +, -, *, or /")
    ask_user = input("Enter an arithmetic operator here: ")

    if ask_user == "+":
        return x + y

    elif ask_user == "-":
        return x - y

    elif ask_user == "*":
        return x * y

    elif ask_user == "/":
        return x / y

    else:
        return "Wrong. Try again!"

