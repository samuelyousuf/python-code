import datetime

def get100_bday():
    """This function returns the year when the user turns 100 years old."""
    
    name_entered = input("What is your name? ")
    age_entered = int(input("What is your current age? "))

    print(name_entered)
    print(age_entered)
    
    time_delta = 100 - age_entered
    calculate_year = datetime.datetime.now().year + time_delta

    print("In year {0:}, you will turn 100 years old!".format(calculate_year))

