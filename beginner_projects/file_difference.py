# Program checks the contents of two files.

first_file = input("Enter a first filename: ")
second_file = input("Enter a second filename: ")

first_Handle = open(first_file, "r")
second_Handle = open(second_file, "r")

for line1 in first_Handle.readlines():
    for line2 in second_Handle.readlines():
        if line2 == line1:
            print("Identical.")
        else:
            print("Different.")

first_Handle.close()
second_Handle.close()

