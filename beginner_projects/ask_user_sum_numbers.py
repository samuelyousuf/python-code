# This program asks the user for a series of numbers, and then returns their sum and average.

total_sum = 0
count = 0

while True:
    ask_input = input("Enter a series of numbers here, with a ',' to separate each number: ")

    if ask_input == "q" or ask_input == "":
        print("Exiting the program...")
        break

    else:
        new_list = ask_input.split(",")
        for i in new_list:
            total_sum += int(i)
            count += 1

    average = total_sum / count
    print("The total sum for your series of numbers is {}.".format(total_sum))
    print("The average for your series of numbers is {}.".format(average))

