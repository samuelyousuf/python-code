# This program copies the content of one file into another file.

first_ask = input("Enter a first filename: ")
second_ask = input("Enter a second filename: ")

first_file = open(first_ask, "r")
second_file = open(second_ask, "w")

lines = first_file.readlines()
second_file.writelines(lines)

first_file.close()
second_file.close()
