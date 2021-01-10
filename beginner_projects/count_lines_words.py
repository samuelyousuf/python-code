# Count words and lines in a file.

def count_words(filename):
    """This function counts the occurances of lines and words in a file."""
    
    # Open the file and set it to a variable
    with open(filename, "r") as the_file:
        
        # Two variables to count the occurances
        total_lines = 0
        total_words = 0

        for line in the_file:
            words = line.strip().split(" ")
            total_words += len(words)
            total_lines += 1

    return "The total number of words is {}, and the total number of lines is {}.".format(total_words, total_lines)

