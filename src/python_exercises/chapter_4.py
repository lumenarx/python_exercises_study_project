import time

from exercises import EXERCISE
import __main__
import math

"""
Loading the EXERCISE class that is being used 
to combine an exercise name and a solution into one
"""

exercise_name = {
    85: "Exercise 85: Compute the Hypotenuse",
    86: "Exercise 86: Taxi Fare",
    87: "Exercise 87: Shipping Calculator",
    88: "Exercise 88: Median of Three Values",
    89: "Exercise 89: Convert an Integer to Its Ordinal Number",
    90: "Exercise 90: The Twelve Days of Christmas",
    91: "Exercise 91: Gregorian Date to Ordinal Date",
    92: "Exercise 92: Ordinal Date to Gregorian Date",
    93: "Exercise 93: Center a String in the Terminal Window",
    94: "Exercise 94: Is It a Valid Triangle?",
    95: "Exercise 95: Capitalize It",
    96: "Exercise 96: Does a String Represent an Integer?",
    97: "Exercise 97: Operator Precedence",
    98: "Exercise 98: Is a Number Prime?",
    99: "Exercise 99: Next Prime",
    100: "Exercise 100: Random Password",
    101: "Exercise 101: Random License Plate",
    102: "Exercise 102: Check a Password",
    103: "Exercise 103: Random Good Password",
    104: "Exercise 104: Hexadecimal and Decimal Digits",
    105: "Exercise 105: Arbitrary Base Conversions",
    106: "Exercise 106: Days in a Month",
    107: "Exercise 107: Reduce a Fraction to Lowest Terms",
    108: "Exercise 108: Reduce Measures",
    109: "Exercise 109: Magic Dates"
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
    "https://doi.org/10.1007/9100-3-030-18895-3"
)

COPYRIGHT = (
        STMP_1
        + "[ COPYRIGHT ]"
        + STMP_1
        + AUTHORS
        + STMP_2
)

EXERCISE_85_NAME = (STMP_1 + "%s" % exercise_name[85])
EXERCISE_86_NAME = (STMP_1 + "%s" % exercise_name[86])
EXERCISE_87_NAME = (STMP_1 + "%s" % exercise_name[87])
EXERCISE_88_NAME = (STMP_1 + "%s" % exercise_name[88])
EXERCISE_89_NAME = (STMP_1 + "%s" % exercise_name[89])
EXERCISE_90_NAME = (STMP_1 + "%s" % exercise_name[90])
EXERCISE_91_NAME = (STMP_1 + "%s" % exercise_name[91])
EXERCISE_92_NAME = (STMP_1 + "%s" % exercise_name[92])
EXERCISE_93_NAME = (STMP_1 + "%s" % exercise_name[93])
EXERCISE_94_NAME = (STMP_1 + "%s" % exercise_name[94])
EXERCISE_95_NAME = (STMP_1 + "%s" % exercise_name[95])
EXERCISE_96_NAME = (STMP_1 + "%s" % exercise_name[96])
EXERCISE_97_NAME = (STMP_1 + "%s" % exercise_name[97])
EXERCISE_98_NAME = (STMP_1 + "%s" % exercise_name[98])
EXERCISE_99_NAME = (STMP_1 + "%s" % exercise_name[99])
EXERCISE_100_NAME = (STMP_1 + "%s" % exercise_name[100])
EXERCISE_101_NAME = (STMP_1 + "%s" % exercise_name[101])
EXERCISE_102_NAME = (STMP_1 + "%s" % exercise_name[102])
EXERCISE_103_NAME = (STMP_1 + "%s" % exercise_name[103])
EXERCISE_104_NAME = (STMP_1 + "%s" % exercise_name[104])
EXERCISE_105_NAME = (STMP_1 + "%s" % exercise_name[105])
EXERCISE_106_NAME = (STMP_1 + "%s" % exercise_name[106])
EXERCISE_107_NAME = (STMP_1 + "%s" % exercise_name[107])
EXERCISE_108_NAME = (STMP_1 + "%s" % exercise_name[108])
EXERCISE_109_NAME = (STMP_1 + "%s" % exercise_name[109])


def menu():
    """Creating chapter's 3 menu"""
    print("[-----------] Menu [-----------] ")
    print("[111] COPYRIGHT ")
    print("[85] %s" % exercise_name[85])
    print("[86] %s" % exercise_name[86])
    print("[87] %s" % exercise_name[87])
    print("[88] %s" % exercise_name[88])
    print("[89] %s" % exercise_name[89])
    print("[90] %s" % exercise_name[90])
    print("[91] %s" % exercise_name[91])
    print("[92] %s" % exercise_name[92])
    print("[93] %s" % exercise_name[93])
    print("[94] %s" % exercise_name[94])
    print("[95] %s" % exercise_name[95])
    print("[96] %s" % exercise_name[96])
    print("[97] %s" % exercise_name[97])
    print("[98] %s" % exercise_name[98])
    print("[99] %s" % exercise_name[99])
    print("[100] %s" % exercise_name[100])
    print("[101] %s" % exercise_name[101])
    print("[102] %s" % exercise_name[102])
    print("[103] %s" % exercise_name[103])
    print("[104] %s" % exercise_name[104])
    print("[105] %s" % exercise_name[105])
    print("[106] %s" % exercise_name[106])
    print("[107] %s" % exercise_name[107])
    print("[108] %s" % exercise_name[108])
    print("[109] %s" % exercise_name[109])
    print("[0] Exit to the main menu")
    option = int(input("Enter the number of an exercise: "))
    if option == 111:
        print(COPYRIGHT)
    elif option == 0:
        __main__.menu()
    elif option == 85:
        problem85 = EXERCISE(EXERCISE_85_NAME)
        problem85.run(exercise_85_solution, menu)
    elif option == 86:
        problem86 = EXERCISE(EXERCISE_86_NAME)
        problem86.run(exercise_86_solution, menu)
    elif option == 87:
        problem87 = EXERCISE(EXERCISE_87_NAME)
        problem87.run(exercise_87_solution, menu)
    elif option == 88:
        problem88 = EXERCISE(EXERCISE_88_NAME)
        problem88.run(exercise_88_solution, menu)
    elif option == 89:
        problem89 = EXERCISE(EXERCISE_89_NAME)
        problem89.run(exercise_89_solution, menu)
    elif option == 90:
        problem90 = EXERCISE(EXERCISE_90_NAME)
        problem90.run(exercise_90_solution, menu)
    elif option == 91:
        problem91 = EXERCISE(EXERCISE_91_NAME)
        problem91.run(exercise_91_solution, menu)
    elif option == 92:
        problem92 = EXERCISE(EXERCISE_92_NAME)
        problem92.run(exercise_92_solution, menu)
    elif option == 93:
        problem93 = EXERCISE(EXERCISE_93_NAME)
        problem93.run(exercise_93_solution, menu)
    elif option == 94:
        problem94 = EXERCISE(EXERCISE_94_NAME)
        problem94.run(exercise_94_solution, menu)
    elif option == 95:
        problem95 = EXERCISE(EXERCISE_95_NAME)
        problem95.run(exercise_95_solution, menu)
    elif option == 96:
        problem96 = EXERCISE(EXERCISE_96_NAME)
        problem96.run(exercise_96_solution, menu)
    elif option == 97:
        problem97 = EXERCISE(EXERCISE_97_NAME)
        problem97.run(exercise_97_solution, menu)
    elif option == 98:
        problem98 = EXERCISE(EXERCISE_98_NAME)
        problem98.run(exercise_98_solution, menu)
    elif option == 99:
        problem99 = EXERCISE(EXERCISE_99_NAME)
        problem99.run(exercise_99_solution, menu)
    elif option == 100:
        problem100 = EXERCISE(EXERCISE_100_NAME)
        problem100.run(exercise_100_solution, menu)
    elif option == 101:
        problem101 = EXERCISE(EXERCISE_101_NAME)
        problem101.run(exercise_101_solution, menu)
    elif option == 102:
        problem102 = EXERCISE(EXERCISE_102_NAME)
        problem102.run(exercise_102_solution, menu)
    elif option == 103:
        problem103 = EXERCISE(EXERCISE_103_NAME)
        problem103.run(exercise_103_solution, menu)
    elif option == 104:
        problem104 = EXERCISE(EXERCISE_104_NAME)
        problem104.run(exercise_104_solution, menu)
    elif option == 105:
        problem105 = EXERCISE(EXERCISE_105_NAME)
        problem105.run(exercise_105_solution, menu)
    elif option == 106:
        problem106 = EXERCISE(EXERCISE_106_NAME)
        problem106.run(exercise_106_solution, menu)
    elif option == 107:
        problem107 = EXERCISE(EXERCISE_107_NAME)
        problem107.run(exercise_107_solution, menu)
    elif option == 108:
        problem108 = EXERCISE(EXERCISE_108_NAME)
        problem108.run(exercise_108_solution, menu)
    elif option == 109:
        problem109 = EXERCISE(EXERCISE_109_NAME)
        problem109.run(exercise_109_solution, menu)
    else:
        exit()


def exercise_85_solution():
    a = float(input("Enter the first shorter side of a right triangle: "))
    b = float(input("Enter the first shorter side of a right triangle: "))
    c = math.sqrt(a ** 2 + b ** 2)
    return print(f"The hypotenuse equals {c}")


def exercise_86_solution():
    base = 4.00
    fare = 0.25
    distance = float(input("Enter the distance: "))
    total_fare = base + (distance / 140) * 0.25
    return print(f"The total fate is ${total_fare}")


def exercise_87_solution():
    rate = 10.95
    subsequent = 2.95
    total_cost = 0
    number = int(input("Enter the number of goods: "))
    if number >= 2:
        total_cost = rate + number * subsequent
    elif number == 1:
        total_cost = rate
    else:
        number = int(input("Enter the number of goods (1 or more): "))
    return print(f"Total cost: ${total_cost}")


def exercise_88_solution():
    names = ["first", "second", "third"]
    arr = []
    for i in range(3):
        n = float(input(f"Enter the {names[i]} with spaces: "))
        arr.append(n)
    if arr[0] < arr[1] < arr[2] or arr[0] > arr[1] > arr[2]:
        return print(f"The median is {arr[1]}")
    elif arr[1] < arr[2] < arr[0] or arr[1] > arr[2] > arr[0]:
        return print(f"The median is {arr[2]}")
    elif arr[2] < arr[0] < arr[1] or arr[2] > arr[0] > arr[1]:
        return print(f"The median is {arr[0]}")


def exercise_89_solution():
    ordinal = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "sevens",
        8: "eights",
        9: "nines",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    n = int(input("Enter an integer number: "))
    if n < 1 or n > 12:
        return print("Empty")
    else:
        return print(f"{n}: {ordinal[n]}")


def exercise_90_solution():
    return print("Exercise body")


def exercise_91_solution():
    return print("Exercise body")


def exercise_92_solution():
    return print("Exercise body")


def exercise_93_solution():
    return print("Exercise body")


def exercise_94_solution():
    return print("Exercise body")


def exercise_95_solution():
    return print("Exercise body")


def exercise_96_solution():
    return print("Exercise body")


def exercise_97_solution():
    return print("Exercise body")


def exercise_98_solution():
    return print("Exercise body")


def exercise_99_solution():
    return print("Exercise body")


def exercise_100_solution():
    return print("Exercise body")


def exercise_101_solution():
    return print("Exercise body")


def exercise_102_solution():
    return print("Exercise body")


def exercise_103_solution():
    return print("Exercise body")


def exercise_104_solution():
    return print("Exercise body")


def exercise_105_solution():
    return print("Exercise body")


def exercise_106_solution():
    return print("Exercise body")


def exercise_107_solution():
    return print("Exercise body")


def exercise_108_solution():
    return print("Exercise body")


def exercise_109_solution():
    return print("Exercise body")
