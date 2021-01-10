# This program is a basic Mad Libs game.

libs = 1

while libs < 3:
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    random = int(input("Enter a random number: "))

    first_sentence = "My favorite noun is {}.".format(noun)
    second_sentence = "My favorite verb is {}.".format(verb)
    third_sentence = "My favorite adjective is {}.".format(adjective)
    fourth_sentence = "My favorite random number is {}.".format(random)

    print(first_sentence, second_sentence, third_sentence, fourth_sentence)

    libs += 1
