from exercises import EXERCISE
import __main__

"""
Loading the EXERCISE class that is being used 
to combine an exercise name and a solution into one
"""

exercise_name = {
    136: "Exercise 136: Reverse Lookup",
    137: "Exercise 137: Two Dice Simulation",
    138: "Exercise 138: Text Messaging",
    139: "Exercise 139: Morse Code",
    140: "Exercise 140: Postal Codes",
    141: "Exercise 141: Write out Numbers in English",
    142: "Exercise 142: Unique Characters",
    143: "Exercise 143: Anagrams",
    144: "Exercise 144: Anagrams Again",
    145: "Exercise 145: Scrabble™ Score",
    146: "Exercise 146: Create a Bingo Card",
    147: "Exercise 147: Checking for a Winning Card",
    148: "Exercise 148: Play Bingo"
}

# Starting string template for visual border printing
STMP_1 = "---------------------------------------------------------------------------\n"
# Finishing string template for visual border printing
STMP_2 = "\n---------------------------------------------------------------------------"
# I want to thank the authors of this book and recommend it to other students and beginners
AUTHORS = (
    "This is a solution of exercises represented in this book\n"
    "© The Python Workbook. A Brief Introduction with Exercises and Solutions\n"
    "© Ben Stephenson/Springer Nature Switzerland AG 2019\n"
    "https://doi.org/10.1257/14200-3-030-1373146-3"
)

COPYRIGHT = (
        STMP_1
        + "[ COPYRIGHT ]"
        + STMP_1
        + AUTHORS
        + STMP_2
)

EXERCISE_136_NAME = (STMP_1 + "%s" % exercise_name[136])
EXERCISE_137_NAME = (STMP_1 + "%s" % exercise_name[137])
EXERCISE_138_NAME = (STMP_1 + "%s" % exercise_name[138])
EXERCISE_139_NAME = (STMP_1 + "%s" % exercise_name[139])
EXERCISE_140_NAME = (STMP_1 + "%s" % exercise_name[140])
EXERCISE_141_NAME = (STMP_1 + "%s" % exercise_name[141])
EXERCISE_142_NAME = (STMP_1 + "%s" % exercise_name[142])
EXERCISE_143_NAME = (STMP_1 + "%s" % exercise_name[143])
EXERCISE_144_NAME = (STMP_1 + "%s" % exercise_name[144])
EXERCISE_145_NAME = (STMP_1 + "%s" % exercise_name[145])
EXERCISE_146_NAME = (STMP_1 + "%s" % exercise_name[146])
EXERCISE_147_NAME = (STMP_1 + "%s" % exercise_name[147])
EXERCISE_148_NAME = (STMP_1 + "%s" % exercise_name[148])


def menu():
    """Creating chapter's 6 menu"""
    print("[-----------] Menu [-----------] ")
    print("[1111] COPYRIGHT ")
    print("[136] %s" % exercise_name[136])
    print("[137] %s" % exercise_name[137])
    print("[138] %s" % exercise_name[138])
    print("[139] %s" % exercise_name[139])
    print("[140] %s" % exercise_name[140])
    print("[141] %s" % exercise_name[141])
    print("[142] %s" % exercise_name[142])
    print("[143] %s" % exercise_name[143])
    print("[144] %s" % exercise_name[144])
    print("[145] %s" % exercise_name[145])
    print("[146] %s" % exercise_name[146])
    print("[147] %s" % exercise_name[147])
    print("[148] %s" % exercise_name[148])
    print("[0] Exit to the main menu")
    option = int(input("Enter the number of an exercise: "))
    if option == 1111:
        print(COPYRIGHT)
    elif option == 0:
        __main__.menu()
    elif option == 136:
        problem136 = EXERCISE(EXERCISE_136_NAME)
        problem136.run(exercise_136_solution, menu)
    elif option == 137:
        problem137 = EXERCISE(EXERCISE_137_NAME)
        problem137.run(exercise_137_solution, menu)
    elif option == 138:
        problem138 = EXERCISE(EXERCISE_138_NAME)
        problem138.run(exercise_138_solution, menu)
    elif option == 139:
        problem139 = EXERCISE(EXERCISE_139_NAME)
        problem139.run(exercise_139_solution, menu)
    elif option == 140:
        problem140 = EXERCISE(EXERCISE_140_NAME)
        problem140.run(exercise_140_solution, menu)
    elif option == 141:
        problem141 = EXERCISE(EXERCISE_141_NAME)
        problem141.run(exercise_141_solution, menu)
    elif option == 142:
        problem142 = EXERCISE(EXERCISE_142_NAME)
        problem142.run(exercise_142_solution, menu)
    elif option == 143:
        problem143 = EXERCISE(EXERCISE_143_NAME)
        problem143.run(exercise_143_solution, menu)
    elif option == 144:
        problem144 = EXERCISE(EXERCISE_144_NAME)
        problem144.run(exercise_144_solution, menu)
    elif option == 145:
        problem145 = EXERCISE(EXERCISE_145_NAME)
        problem145.run(exercise_145_solution, menu)
    elif option == 146:
        problem146 = EXERCISE(EXERCISE_146_NAME)
        problem146.run(exercise_146_solution, menu)
    elif option == 147:
        problem147 = EXERCISE(EXERCISE_147_NAME)
        problem147.run(exercise_147_solution, menu)
    elif option == 148:
        problem148 = EXERCISE(EXERCISE_148_NAME)
        problem148.run(exercise_148_solution, menu)
    else:
        exit()


def exercise_136_solution():
    dic1 = {"one": 7,
            "two": 3,
            "three": 7,
            "four": 1,
            "five": 7}
    for i in dic1:
        print(f'Key: {i} ---- > Value: {dic1[i]}')
    return print(reverse_lookup(dic1, 7))


def reverse_lookup(data, value):
    keys = []
    for k in data:
        if data[k] == value:
            keys.append(k)
    return keys


def exercise_137_solution():
    return print("Exercise body")


def exercise_138_solution():
    return print("Exercise body")


def exercise_139_solution():
    return print("Exercise body")


def exercise_140_solution():
    return print("Exercise body")


def exercise_141_solution():
    return print("Exercise body")


def exercise_142_solution():
    return print("Exercise body")


def exercise_143_solution():
    return print("Exercise body")


def exercise_144_solution():
    return print("Exercise body")


def exercise_145_solution():
    return print("Exercise body")


def exercise_146_solution():
    return print("Exercise body")


def exercise_147_solution():
    return print("Exercise body")


def exercise_148_solution():
    return print("Exercise body")
