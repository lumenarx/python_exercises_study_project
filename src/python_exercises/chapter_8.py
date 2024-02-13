from exercises import EXERCISE
import __main__

"""
Loading the EXERCISE class that is being used 
to combine an exercise name and a solution into one
"""

exercise_name = {
    173: "Exercise 173: Total the Values",
    174: "Exercise 174: Greatest Common Divisor",
    175: "Exercise 175: Recursive Decimal to Binary",
    176: "Exercise 176: The NATO Phonetic Alphabet",
    177: "Exercise 177: Roman Numerals",
    178: "Exercise 178: Recursive Palindrome",
    179: "Exercise 179: Recursive Square Root",
    180: "Exercise 180: String Edit Distance",
    181: "Exercise 181: Possible Change",
    182: "Exercise 182: Spelling with Element Symbols",
    183: "Exercise 183: Element Sequences",
    184: "Exercise 184: Flatten a List",
    185: "Exercise 185: Run-Length Decoding",
    186: "Exercise 186: Run-Length Encoding"
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
    "https://doi.org/10.1257/17900-3-030-1743183-3"
)

COPYRIGHT = (
        STMP_1
        + "[ COPYRIGHT ]"
        + STMP_1
        + AUTHORS
        + STMP_2
)

EXERCISE_173_NAME = (STMP_1 + "%s" % exercise_name[173])
EXERCISE_174_NAME = (STMP_1 + "%s" % exercise_name[174])
EXERCISE_175_NAME = (STMP_1 + "%s" % exercise_name[175])
EXERCISE_176_NAME = (STMP_1 + "%s" % exercise_name[176])
EXERCISE_177_NAME = (STMP_1 + "%s" % exercise_name[177])
EXERCISE_178_NAME = (STMP_1 + "%s" % exercise_name[178])
EXERCISE_179_NAME = (STMP_1 + "%s" % exercise_name[179])
EXERCISE_180_NAME = (STMP_1 + "%s" % exercise_name[180])
EXERCISE_181_NAME = (STMP_1 + "%s" % exercise_name[181])
EXERCISE_182_NAME = (STMP_1 + "%s" % exercise_name[182])
EXERCISE_183_NAME = (STMP_1 + "%s" % exercise_name[183])
EXERCISE_184_NAME = (STMP_1 + "%s" % exercise_name[184])
EXERCISE_185_NAME = (STMP_1 + "%s" % exercise_name[185])
EXERCISE_186_NAME = (STMP_1 + "%s" % exercise_name[186])


def menu():
    """Creating chapter's 8 menu"""
    print("[-----------] Menu [-----------] ")
    print("[174] COPYRIGHT ")
    print("[173] %s" % exercise_name[173])
    print("[174] %s" % exercise_name[174])
    print("[175] %s" % exercise_name[175])
    print("[176] %s" % exercise_name[176])
    print("[177] %s" % exercise_name[177])
    print("[178] %s" % exercise_name[178])
    print("[179] %s" % exercise_name[179])
    print("[180] %s" % exercise_name[180])
    print("[181] %s" % exercise_name[181])
    print("[182] %s" % exercise_name[182])
    print("[183] %s" % exercise_name[183])
    print("[184] %s" % exercise_name[184])
    print("[185] %s" % exercise_name[185])
    print("[186] %s" % exercise_name[186])
    print("[0] Exit to the main menu")
    option = int(input("Enter the number of an exercise: "))
    if option == 174:
        print(COPYRIGHT)
    elif option == 0:
        __main__.menu()
    elif option == 173:
        problem173 = EXERCISE(EXERCISE_173_NAME)
        problem173.run(exercise_173_solution, menu)
    elif option == 174:
        problem174 = EXERCISE(EXERCISE_174_NAME)
        problem174.run(exercise_174_solution, menu)
    elif option == 175:
        problem175 = EXERCISE(EXERCISE_175_NAME)
        problem175.run(exercise_175_solution, menu)
    elif option == 176:
        problem176 = EXERCISE(EXERCISE_176_NAME)
        problem176.run(exercise_176_solution, menu)
    elif option == 177:
        problem177 = EXERCISE(EXERCISE_177_NAME)
        problem177.run(exercise_177_solution, menu)
    elif option == 178:
        problem178 = EXERCISE(EXERCISE_178_NAME)
        problem178.run(exercise_178_solution, menu)
    elif option == 179:
        problem179 = EXERCISE(EXERCISE_179_NAME)
        problem179.run(exercise_179_solution, menu)
    elif option == 180:
        problem180 = EXERCISE(EXERCISE_180_NAME)
        problem180.run(exercise_180_solution, menu)
    elif option == 181:
        problem181 = EXERCISE(EXERCISE_181_NAME)
        problem181.run(exercise_181_solution, menu)
    elif option == 182:
        problem182 = EXERCISE(EXERCISE_182_NAME)
        problem182.run(exercise_182_solution, menu)
    elif option == 183:
        problem183 = EXERCISE(EXERCISE_183_NAME)
        problem183.run(exercise_183_solution, menu)
    elif option == 184:
        problem184 = EXERCISE(EXERCISE_184_NAME)
        problem184.run(exercise_184_solution, menu)
    elif option == 185:
        problem185 = EXERCISE(EXERCISE_185_NAME)
        problem185.run(exercise_185_solution, menu)
    elif option == 186:
        problem186 = EXERCISE(EXERCISE_186_NAME)
        problem186.run(exercise_186_solution, menu)
    else:
        exit()


def exercise_173_solution():
    return print("Exercise body")


def exercise_174_solution():
    return print("Exercise body")


def exercise_175_solution():
    return print("Exercise body")


def exercise_176_solution():
    return print("Exercise body")


def exercise_177_solution():
    return print("Exercise body")


def exercise_178_solution():
    return print("Exercise body")


def exercise_179_solution():
    return print("Exercise body")


def exercise_180_solution():
    return print("Exercise body")


def exercise_181_solution():
    return print("Exercise body")


def exercise_182_solution():
    return print("Exercise body")


def exercise_183_solution():
    return print("Exercise body")


def exercise_184_solution():
    return print("Exercise body")


def exercise_185_solution():
    return print("Exercise body")


def exercise_186_solution():
    return print("Exercise body")
