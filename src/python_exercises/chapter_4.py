from time import sleep
from random import randrange
from exercises import EXERCISE
import __main__
from math import sqrt

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
    """Creating chapter's 4 menu"""
    print("[-----------] Menu [-----------] ")
    print("[1111] COPYRIGHT ")
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
    if option == 1111:
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
    c = sqrt(a ** 2 + b ** 2)
    return print(f"The hypotenuse equals {c}")


def exercise_86_solution():
    base = 4.00
    fare = 0.25
    distance = float(input("Enter the distance: "))
    total_fare = base + (distance / 140) * fare
    return print(f"The total fate is ${total_fare}")


def exercise_87_solution():
    rate = 10.95
    subsequent = 2.95
    number = int(input("Enter the number of goods: "))
    while number < 1:
        number = int(input("Enter the number of goods (1 or more): "))
    if number == 1:
        total_cost = rate
    else:
        total_cost = rate + number * subsequent
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
    present_list = ""
    presents = {
        1: "A partridge in a pear tree.",
        2: "Two turtle doves,\n",
        3: "Three French hens,\n",
        4: "Four calling birds,\n",
        5: "Five gold rings,\n",
        6: "Six geese a - laying,\n",
        7: "Seven swans a-swimming,\n",
        8: "Eight maids a-milking,\n",
        9: "Nine ladies dancing,\n",
        10: "Ten lords a-leaping,\n",
        11: "Eleven pipers piping,\n",
        12: "Twelve drummers drumming,\n"
    }
    for n in range(1, 13):
        present_list += presents[n]
        sleep(0.80)
        if n == 1:
            print(f"On the {ordinal[n]} day of Christmas\n"
                  f"my true love sent to me:\n"
                  f"{present_list}")
        else:
            print(f"\n\n"
                  f"On the {ordinal[n]} day of Christmas\n"
                  f"my true love sent to me:\n"
                  f"{present_list}"
                  f"And a partridge in a pear tree.")


def exercise_91_solution():
    day = int(input("Enter a day of the month: "))
    month = int(input("Enter a month: "))
    year = int(input("Enter a year: "))
    c_date = ordinal_date(day, month, year)
    print(c_date)


def leap_year(year):
    if year % 400 == 0:
        return True
    else:
        if year % 100 == 0:
            return False
        else:
            if year % 4 == 0:
                return True
            else:
                return False


def ordinal_date(day, month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    c_date = 0
    leap = leap_year(year)
    if leap:
        for i in range(0, month - 1):
            c_date += days_in_month[i]
        c_date += day
        if c_date >= 59:
            c_date += 1
    else:
        for i in range(0, month - 1):
            c_date += days_in_month[i]
        c_date += day
    return c_date


def exercise_92_solution():
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
              'september', 'october', 'november', 'december']
    year = int(input("Enter a year: "))
    o_date = int(input("Enter an ordinal date: "))
    arr = gregorian_date(year, o_date)
    index = arr[0]
    day = arr[1]
    return print("Date: %d %s, %d" % (day, months[index], year))


def gregorian_date(year, o_date):
    mm_dd = []
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    k = 0
    leap = leap_year(year)
    if leap:
        days_in_month[1] = 29
    while o_date > 0:
        if o_date - days_in_month[k] > 0:
            o_date -= days_in_month[k]
            k += 1
        else:
            mm_dd = [k, o_date]
            break
    return mm_dd


def exercise_93_solution():
    line = input("Enter the string content: ")
    window = int(input("Enter a width of the window: "))
    if len(line) >= window:
        return print(line)
    else:
        spaces = (window - len(line)) // 2
        new_line = "_" * spaces + line + "_" * spaces
        return print(new_line)


def exercise_94_solution():
    a = float(input("Enter the first side of the triangle."))
    b = float(input("Enter the second side of the triangle."))
    c = float(input("Enter the third side of the triangle."))
    flag = triangle_validation(a, b, c)
    if flag:
        return print("A triangle can be formed from given sides.")
    else:
        return print("You can not form a triangle from given sides.")


def triangle_validation(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and b + c > a and c + a > b:
        return True


def exercise_95_solution():
    line = input("Enter a string content: ")
    n = len(line)
    line_list = list(line)
    for i in range(n):
        if ((line[i - 1] == "." or line[i - 1] == "!" or line[i - 1] == "?") or
                (line[i - 2] == "." or line[i - 2] == "!" or line[i - 2] == "?") and (line[i - 1] == " ")):
            buff = line_list[i].upper()
            line_list[i] = buff
        if line[i] == "i" and line[i - 1] == " " and (line[i + 1] == "'" or line[i + 1] == " "):
            buff = line_list[i].upper()
            line_list[i] = buff
    new_line = "".join(line_list)
    return print(new_line)


def exercise_96_solution():
    line = input("Enter a string: ")
    if is_integer(line):
        return print(f"The string {line} contents an integer.")
    else:
        return print(f"The string {line} does not content an integer.")


def is_integer(string):
    line = str(string.strip(" "))
    if len(line) > 1 and line.isdigit() is True:
        return True
    elif len(line) > 1 and (line[0] == "+" or line[0] == "-"):
        line2 = str(line.strip("+- "))
        if len(line2) > 1 and line2.isdigit() is True:
            return True
    else:
        return False


def exercise_97_solution():
    line = input("Enter the string content: ")
    result = precedence(line)
    while result == -1:
        line = input("Incorrect input. Please, enter a math operator: ")
        result = precedence(line)
        if result != -1:
            return print(precedence(line), line)


def precedence(line):
    n = len(line)
    for i in range(n):
        if line[i] == "+" or line[i] == "-":
            return 1
        elif line[i] == "*" or line[i] == "/":
            return 2
        elif line[i] == "^":
            return 3
    else:
        return -1


def exercise_98_solution():
    n = int(input("Enter an integer: "))
    if prime_number(n):
        return print("This is a prime number.")
    else:
        return print("This is not a prime number.")


def prime_number(n):
    table = [True] * (n + 1)
    table[0] = False
    table[1] = False
    d = 2
    while d * d <= n:
        if table[d]:
            for i in range(d * d, n + 1, d):
                table[i] = False
        d += 1
    g = len(table) - 1
    if table[g]:
        return True
    else:
        return False


def exercise_99_solution():
    n = int(input("Enter an integer: "))
    return print(next_prime(n))


def next_prime(n):
    g = n + 1
    while prime_number(g) is not True:
        g = g + 1
    return g


def exercise_100_solution():
    for i in range(10):
        print(generate_password())
    return 1


def generate_password():
    password = ""
    length = randrange(7, 11)
    for i in range(length):
        symbol_ascii = randrange(33, 127)
        password += chr(symbol_ascii)
    return password


def exercise_101_solution():
    number = int(input("Enter a number of plates to generate: "))
    for i in range(number):
        print(generate_plate())
    return 1


def generate_plate():
    plate = ""
    for i in range(7):
        if i <= 3:
            n = randrange(0, 10)
            plate += str(n)
        else:
            n = randrange(65, 91)
            plate += chr(n)
    return plate


def exercise_102_solution():
    password = input("Enter a password: ")
    password_check(password)
    if password_check(password):
        return print("This password is good.")
    else:
        return print("This password is weak.")


def password_check(password):
    length = False
    lower_case = False
    upper_case = False
    number = False
    if len(password) >= 8:
        length = True
    for i in range(len(password)):
        if password[i].islower() and lower_case is False:
            lower_case = True
        elif password[i].isupper() and upper_case is False:
            upper_case = True
        elif password[i].isdigit() and number is False:
            number = True
    if length and lower_case and upper_case and number:
        return True
    else:
        return False


def exercise_103_solution():
    password = ""
    validation = False
    attempts = 0
    while validation is False:
        password = generate_password()
        validation = password_check(password)
        attempts += 1
    print(F"{password} is good password which was made on {attempts} attempt(s).")


def exercise_104_solution():
    line = input("Enter an integer: ")
    number1 = int_to_hex(line)
    number2 = hex_to_int(number1)
    print(number1)
    print(number2)


def hex_to_int(hex_number):
    base = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    int_number = 0
    result = ""
    n = len(hex_number)
    if hex_number[0] == "+" or hex_number[0] == "-":
        d = len(hex_number) - 2
        result += hex_number[0]
        for i in range(1, n):
            upper_case = hex_number[i].upper()
            int_number += base[upper_case] * 16 ** d
            d -= 1
    else:
        d = len(hex_number) - 1
        for i in range(n):
            upper_case = hex_number[i].upper()
            int_number += base[upper_case] * 16 ** d
            d -= 1
    result += str(int_number)
    return result


def int_to_hex(int_number):
    base = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    hex_number = ""
    reversed_number = []
    if int_number[0] == "+" or int_number[0] == "-":
        number = int(int_number.strip("+-"))
        hex_number += int_number[0]
    else:
        number = int(int_number)
    while number != 0:
        g = number % 16
        reversed_number.append(g)
        number //= 16
    h = len(reversed_number) - 1
    for i in range(h, -1, -1):
        hex_number += base[reversed_number[i]].lower()
    return hex_number


def exercise_105_solution():
    line = input("Enter an integer: ")
    base = int(input("Enter the base (from 2 to 16): "))
    if not (2 <= base <= 16):
        print("The base of %d is incorrect." % base)
        return 0
    new_base = int(input("Enter a new base (from 2 to 16): "))
    if not (2 <= new_base <= 16):
        print("The base of %d is incorrect." % new_base)
        return 0
    return print(converter(line, base, new_base))


def converter(initial_number, initial_base, new_base):
    base_char = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    base_int = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    int_number = 0
    decimal_base = ""
    reversed_number = []
    result = ""
    n = len(initial_number)
    if initial_base != 10:
        if initial_number[0] == "+" or initial_number[0] == "-":
            d = len(initial_number) - 2
            decimal_base += initial_number[0]
            for i in range(1, n):
                upper_case = initial_number[i].upper()
                int_number += base_char[upper_case] * initial_base ** d
                d -= 1
        else:
            d = len(initial_number) - 1
            for i in range(n):
                upper_case = initial_number[i].upper()
                int_number += base_char[upper_case] * initial_base ** d
                d -= 1
        decimal_base += str(int_number)
    else:
        decimal_base = initial_number
    if decimal_base[0] == "+" or decimal_base[0] == "-":
        new_number = int(decimal_base.strip("+-"))
        result += decimal_base[0]
    else:
        new_number = int(decimal_base)
    while new_number != 0:
        g = new_number % new_base
        reversed_number.append(g)
        new_number //= new_base
    h = len(reversed_number) - 1
    for i in range(h, -1, -1):
        result += base_int[reversed_number[i]].lower()
    return result


def exercise_106_solution():
    year = int(input("Enter a year: "))
    month = int(input("Enter a month number: "))
    while not (1 <= month <= 12):
        month = int(input("Please, enter the correct month number (1 to 12): "))
    n = days_by_month(month, year)
    return print(f"The number of days in this month is {n}.")


def days_by_month(month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = leap_year(year)
    if leap:
        days_in_month[1] = 29
    n = month - 1
    return days_in_month[n]


def exercise_107_solution():
    number_1 = int(input("Enter the first integer: "))
    number_2 = int(input("Enter the second integer: "))
    return print(reduce_fraction(number_1, number_2))


def reduce_fraction(numerator, denominator):
    if numerator > denominator:
        divisor = numerator
    else:
        divisor = denominator
    while numerator % divisor != 0 or denominator % divisor != 0:
        divisor -= 1
    new_numerator = numerator // divisor
    new_denominator = denominator // divisor
    result = "The reduced fraction is %d / %d" % (new_numerator, new_denominator)
    return result


def exercise_108_solution():
    quantity = int(input("Enter the number of units: "))
    measure = int(input("Enter the unit of measure [1 - cup, 2 - tablespoon, 3 - teaspoon]: "))
    while not (measure == 1 or measure == 2 or measure == 3):
        measure = int(input("Enter the unit of measure [1 - cup, 2 - tablespoon, 3 - teaspoon]: "))
    return print(imperial_volume(quantity, measure))


def imperial_volume(quantity, measure):
    teaspoons = 0
    tablespoons = 0
    cups = 0
    result = ""
    if measure == 1:
        cups = quantity
    if measure == 2:
        if quantity >= 16:
            cups = quantity // 16
            tablespoons = quantity % 16
    if measure == 3:
        if quantity >= 3:
            tablespoons = quantity // 3
            teaspoons = quantity % 3
        if tablespoons >= 16:
            cups = tablespoons // 16
            tablespoons = tablespoons % 16
    if cups > 1:
        text_cups = "cups"
    else:
        text_cups = "cup"
    if tablespoons > 1:
        text_tablespoons = "tablespoons"
    else:
        text_tablespoons = "tablespoon"
    if teaspoons > 1:
        text_teaspoons = "teaspoons"
    else:
        text_teaspoons = "teaspoon"
    if cups > 0:
        result += "%d %s " % (cups, text_cups)
    if tablespoons > 0:
        result += "%d %s " % (tablespoons, text_tablespoons)
    if teaspoons > 0:
        result += "%d %s " % (teaspoons, text_teaspoons)
    return result


def exercise_109_solution():
    month = int(input("Enter a month number: "))
    day = int(input("Enter a day: "))
    year = int(input("Enter a year: "))
    if magic_date(day, month, year):
        print(f"{month}.{day}.{year} is a magic date.")
    else:
        print(f"{month}.{day}.{year} is NOT a magic date.")
    magic_list = int(input("Do you want to see the list of magic dates in XX century? [1 = Yes, 0 - No]: "))
    if magic_list == 1:
        arr1 = []
        k = 0
        for i in range(1, 13):
            for j in range(1, 32):
                result = j * i
                year = 1900 + result
                if magic_date(j, i, year) is True:
                    arr1.insert(k, [j, i, year])
                    k += 1
        n = len(arr1)
        k = 1
        for i in range(n):
            dd = arr1[i][0]
            mm = arr1[i][1]
            yy = arr1[i][2]
            print(f"The {i + 1} magic date is {mm}.{dd}.{yy}")
    else:
        return 1


def magic_date(day, month, year):
    remainder = year % 100
    if day * month == remainder:
        return True
    else:
        return False

