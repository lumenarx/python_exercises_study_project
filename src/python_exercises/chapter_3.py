from exercises import EXERCISE
import __main__
import math
"""
Loading the EXERCISE class that is being used 
to combine an exercise name and a solution into one
"""

exercise_name = {
    63: "Exercise 63: Average",
    64: "Exercise 64: Discount Table ",
    65: "Exercise 65: Temperature Conversion Table",
    66: "Exercise 66: No More Pennies",
    67: "Exercise 67: Compute the Perimeter of a Polygon",
    68: "Exercise 68: Compute a Grade Point Average",
    69: "Exercise 69: Admission Price",
    70: "Exercise 70: Parity Bits",
    71: "Exercise 71: Approximate pi",
    72: "Exercise 72: Fizz-Buzz",
    73: "Exercise 73: Caesar Cipher",
    74: "Exercise 74: Square Root",
    75: "Exercise 75: Is a String a Palindrome?",
    76: "Exercise 76: Multiple Word Palindromes",
    77: "Exercise 77: Multiplication Table",
    78: "Exercise 78: The Collatz Conjecture",
    79: "Exercise 79: Greatest Common Divisor ",
    80: "Exercise 80: Prime Factors",
    81: "Exercise 81: Binary to Decimal ",
    82: "Exercise 82: Decimal to Binary ",
    83: "Exercise 83: Maximum Integer",
    84: "Exercise 84: Coin Flip Simulation"
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
    "https://doi.org/10.1007/978-3-030-18873-3"
)

COPYRIGHT = (
    STMP_1
    + "[ COPYRIGHT ]"
    + STMP_1
    + AUTHORS
    + STMP_2
)

EXERCISE_63_NAME = (STMP_1 + "%s" % exercise_name[63])
EXERCISE_64_NAME = (STMP_1 + "%s" % exercise_name[64])
EXERCISE_65_NAME = (STMP_1 + "%s" % exercise_name[65])
EXERCISE_66_NAME = (STMP_1 + "%s" % exercise_name[66])
EXERCISE_67_NAME = (STMP_1 + "%s" % exercise_name[67])
EXERCISE_68_NAME = (STMP_1 + "%s" % exercise_name[68])
EXERCISE_69_NAME = (STMP_1 + "%s" % exercise_name[69])
EXERCISE_70_NAME = (STMP_1 + "%s" % exercise_name[70])
EXERCISE_71_NAME = (STMP_1 + "%s" % exercise_name[71])
EXERCISE_72_NAME = (STMP_1 + "%s" % exercise_name[72])
EXERCISE_73_NAME = (STMP_1 + "%s" % exercise_name[73])
EXERCISE_74_NAME = (STMP_1 + "%s" % exercise_name[74])
EXERCISE_75_NAME = (STMP_1 + "%s" % exercise_name[75])
EXERCISE_76_NAME = (STMP_1 + "%s" % exercise_name[76])
EXERCISE_77_NAME = (STMP_1 + "%s" % exercise_name[77])
EXERCISE_78_NAME = (STMP_1 + "%s" % exercise_name[78])
EXERCISE_79_NAME = (STMP_1 + "%s" % exercise_name[79])
EXERCISE_80_NAME = (STMP_1 + "%s" % exercise_name[80])
EXERCISE_81_NAME = (STMP_1 + "%s" % exercise_name[81])
EXERCISE_82_NAME = (STMP_1 + "%s" % exercise_name[82])
EXERCISE_83_NAME = (STMP_1 + "%s" % exercise_name[83])
EXERCISE_84_NAME = (STMP_1 + "%s" % exercise_name[84])


def menu():
    """Creating chapter's 3 menu"""
    print("[-----------] Menu [-----------] ")
    print("[111] COPYRIGHT ")
    print("[63] %s" % exercise_name[63])
    print("[64] %s" % exercise_name[64])
    print("[65] %s" % exercise_name[65])
    print("[66] %s" % exercise_name[66])
    print("[67] %s" % exercise_name[67])
    print("[68] %s" % exercise_name[68])
    print("[69] %s" % exercise_name[69])
    print("[70] %s" % exercise_name[70])
    print("[71] %s" % exercise_name[71])
    print("[72] %s" % exercise_name[72])
    print("[73] %s" % exercise_name[73])
    print("[74] %s" % exercise_name[74])
    print("[75] %s" % exercise_name[75])
    print("[76] %s" % exercise_name[76])
    print("[77] %s" % exercise_name[77])
    print("[78] %s" % exercise_name[78])
    print("[79] %s" % exercise_name[79])
    print("[80] %s" % exercise_name[80])
    print("[81] %s" % exercise_name[81])
    print("[82] %s" % exercise_name[82])
    print("[83] %s" % exercise_name[83])
    print("[84] %s" % exercise_name[84])
    print("[0] Exit to the main menu")
    option = int(input("Enter the number of a chapter: "))
    if option == 111:
        print(COPYRIGHT)
    elif option == 0:
        __main__.menu()
    elif option == 63:
        problem63 = EXERCISE(EXERCISE_63_NAME)
        problem63.run(exercise_63_solution, menu)
    elif option == 64:
        problem64 = EXERCISE(EXERCISE_64_NAME)
        problem64.run(exercise_64_solution, menu)
    elif option == 65:
        problem65 = EXERCISE(EXERCISE_65_NAME)
        problem65.run(exercise_65_solution, menu)
    elif option == 66:
        problem66 = EXERCISE(EXERCISE_66_NAME)
        problem66.run(exercise_66_solution, menu)
    elif option == 67:
        problem67 = EXERCISE(EXERCISE_67_NAME)
        problem67.run(exercise_67_solution, menu)
    elif option == 68:
        problem68 = EXERCISE(EXERCISE_68_NAME)
        problem68.run(exercise_68_solution, menu)
    elif option == 69:
        problem69 = EXERCISE(EXERCISE_69_NAME)
        problem69.run(exercise_69_solution, menu)
    elif option == 70:
        problem70 = EXERCISE(EXERCISE_70_NAME)
        problem70.run(exercise_70_solution, menu)
    elif option == 71:
        problem71 = EXERCISE(EXERCISE_71_NAME)
        problem71.run(exercise_71_solution, menu)
    elif option == 72:
        problem72 = EXERCISE(EXERCISE_72_NAME)
        problem72.run(exercise_72_solution, menu)
    elif option == 73:
        problem73 = EXERCISE(EXERCISE_73_NAME)
        problem73.run(exercise_73_solution, menu)
    elif option == 74:
        problem74 = EXERCISE(EXERCISE_74_NAME)
        problem74.run(exercise_74_solution, menu)
    elif option == 75:
        problem75 = EXERCISE(EXERCISE_75_NAME)
        problem75.run(exercise_75_solution, menu)
    elif option == 76:
        problem76 = EXERCISE(EXERCISE_76_NAME)
        problem76.run(exercise_76_solution, menu)
    elif option == 77:
        problem77 = EXERCISE(EXERCISE_77_NAME)
        problem77.run(exercise_77_solution, menu)
    elif option == 78:
        problem78 = EXERCISE(EXERCISE_78_NAME)
        problem78.run(exercise_78_solution, menu)
    elif option == 79:
        problem79 = EXERCISE(EXERCISE_79_NAME)
        problem79.run(exercise_79_solution, menu)
    elif option == 80:
        problem80 = EXERCISE(EXERCISE_80_NAME)
        problem80.run(exercise_80_solution, menu)
    elif option == 81:
        problem81 = EXERCISE(EXERCISE_81_NAME)
        problem81.run(exercise_81_solution, menu)
    elif option == 82:
        problem82 = EXERCISE(EXERCISE_82_NAME)
        problem82.run(exercise_82_solution, menu)
    elif option == 83:
        problem83 = EXERCISE(EXERCISE_83_NAME)
        problem83.run(exercise_83_solution, menu)
    elif option == 84:
        problem84 = EXERCISE(EXERCISE_84_NAME)
        problem84.run(exercise_84_solution, menu)
    else:
        exit()


def exercise_63_solution():
    arr = []
    average = 0
    number = int(input("Enter a number (enter zero to complete the input): "))
    if number != 0:
        arr.append(number)
        while number != 0:
            number = int(input("Enter a number (enter zero to complete the input): "))
            if number != 0:
                arr.append(number)
        k = len(arr)
        for i in range(k):
            average = average + arr[i]
        average = average / k
    else:
        while number == 0:
            number = int(input("Enter the correct number (enter zero to complete the input): "))
            if number != 0:
                arr.append(number)
    return print(f"Array: {list(arr)}\n"
                 f"Average: {int(average)}")


def exercise_64_solution():
    price = [4.95, 9.95, 14.95, 19.95, 24.95]
    n = len(price)
    for i in range(n):
        discounted_price = price[i] * 0.4
        print(f"~~~~~~ [ Shelf {i}] ~~~~~~\n"
              "Original price: %.2f\n"
              "Discounted price: %.2f\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~" % (price[i], discounted_price))
    return 1


def exercise_65_solution():
    for celsius in range(0, 101, 10):
        fahrenheit = celsius * (9/5) + 32
        print(f"Celsius: {celsius}, Fahrenheit: {fahrenheit}")
    return print("~~~ The END of table ~~~")


def exercise_66_solution():
    total_bill = 0
    item_price = -1
    items = []
    while item_price != "":
        item_price = input("Enter the item's price: ")
        if item_price != "":
            items.append(item_price)
            total_bill += float(item_price)
    if total_bill % 0.05 > 0.025:
        total_bill = total_bill - (total_bill % 0.05) + 0.05
        round(total_bill, 2)
    else:
        total_bill = total_bill - (total_bill % 0.05)
        round(total_bill, 2)
    n = len(items)
    for i in range(n):
        print(f"Item {i}; Price: {items[i]}")
    return print(f"Total bill: {total_bill}")


def exercise_67_solution():
    x = float(input("Enter the first x-coordinate: "))
    y = float(input("Enter the first y-coordinate: "))
    perimeter = 0
    coordinates = [[x, y]]
    k = 0
    while str(x) != "":
        x = input("Enter the next x-coordinate (blank to quit): ")
        if x == "":
            perimeter += math.sqrt(
                (coordinates[k][0] - coordinates[0][0]) ** 2 + (coordinates[k][1] - coordinates[0][1]) ** 2)
            break
        else:
            x = float(x)
            y = float(input("Enter the next y-coordinate: "))
            k += 1
            coordinates.append([x, y])
            perimeter += math.sqrt(
                (coordinates[k][0] - coordinates[k - 1][0]) ** 2 + (coordinates[k][1] - coordinates[k - 1][1]) ** 2)
    return print(f"The perimeter of that polygon is {perimeter}")


def exercise_68_solution():
    grade_letters = ['A', 'B', 'C', 'D', 'F']
    grade_coefficients = [4, 3, 2, 1, 0]
    new_grade = 0
    k = 0
    row = 0
    average = 0
    grade = " "
    grade_list = []
    print(len(grade))
    while grade != "":
        grade = input("Enter a next letter grade: ")
        if grade != "":
            grade_list.append(grade)
            for i in range(5):
                if grade[0] == grade_letters[i]:
                    new_grade = float(grade_coefficients[i])
                    if grade.endswith('+'):
                        new_grade += 0.3
                    elif grade.endswith('-') and grade[0] != 'F':
                        new_grade -= 0.3
                    elif grade.endswith('++'):
                        new_grade += 0.6
                    elif grade.endswith('--') and grade[0] != 'F':
                        new_grade -= 0.6
            row += new_grade
            k += 1
        else:
            average = row / k
    return print(f"Grades: {list(grade_list)}\n"
                 f"Grades' count: {k}\n"
                 f"Average grade: {round(average, 2)}")


def exercise_69_solution():
    group_ages = []
    ticket_price = [14.00, 23.00, 18.00]
    age = " "
    summary = ""
    k = 1
    (age_0_to_2, age_3_to_11, age_12_to_65, age_66_to_120) = 0, 0, 0, 0
    while age != "":
        age = input(f"Enter the age of guest {k}: ")
        if age != "":
            group_ages.append(int(age))
            k += 1
        else:
            n = len(group_ages)
            for i in range(n):
                if 0 <= group_ages[i] <= 2:
                    age_0_to_2 += 1
                elif 3 <= group_ages[i] <= 11:
                    age_3_to_11 += 1
                elif 12 <= group_ages[i] <= 65:
                    age_12_to_65 += 1
                elif 66 <= group_ages[i]:
                    age_66_to_120 += 1
    if age_0_to_2 > 0:
        summary += (f"Age 0 to 2: {age_0_to_2} person(s); "
                    f"One ticket price: FREE\n")
    if age_3_to_11 > 0:
        summary += (f"Age 3 to 11: {age_3_to_11} person(s); "
                    f"One ticket price: ${ticket_price[0]}\n")
    if age_12_to_65 > 0:
        summary += (f"Age 12 to 65: {age_12_to_65} person(s) ;"
                    f"One ticket price: ${ticket_price[1]}\n")
    if age_66_to_120 > 0:
        summary += (f"Age 66 to 120: {age_66_to_120} person(s); "
                    f"One ticket price: ${ticket_price[2]}\n")
    admission_cost = age_3_to_11 * ticket_price[0] + age_12_to_65 * ticket_price[1] + age_66_to_120 * ticket_price[2]
    summary += f"Admission cost: ${admission_cost}"
    return print(summary)


def exercise_70_solution():
    message = " "
    while message != "":
        if message != "":
            message = input("Enter 8 bits: ")
            if message.count("0") + message.count("1") != 8 or len(message) != 8:
                message = input("Please, enter 8 bits: ")
            n = message.count("1")
            if n % 2 == 1:
                print("The parity bit is 1")
            else:
                print("The parity bit is 0")
    return 1


def exercise_71_solution():
    d1 = 0
    pi = 3
    for i in range(1, 16):
        d1 += 2
        d2 = d1 + 1
        d3 = d1 + 2
        block = d1 * d2 * d3
        if i % 2 == 1:
            pi += (4 / block)
        else:
            pi -= (4 / block)
        print(f"{pi} is the {i} approximation of pi")


def exercise_72_solution():
    number = 1
    while number != 100:
        if number % 3 == 0 and number % 5 != 0:
            print(f"{number}. Answer: Fizz")
        elif number % 5 == 0 and number % 3 != 0:
            print(f"{number}. Answer: Buzz")
        elif number % 3 == 0 and number % 5 == 0:
            print(f"{number}. Answer: Fizz-Buzz")
        else:
            print(f"{number}. Answer: {number}")
        number += 1


def exercise_73_solution():
    alphabet_number = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
        6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
        11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
        16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
        21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
        26: 'z'
    }
    alphabet_letter = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26
    }
    uncoded_message = input("Enter the message: ")
    coded_message = ""
    shift = input("Enter the shift amount: ")
    n = len(uncoded_message)
    for i in range(n):
        if uncoded_message[i] != " ":
            index = alphabet_letter[str.lower(uncoded_message[i])]
            index += int(shift)
            print(f"Uncoded: {uncoded_message[i]}\n"
                  f"Index shifted: {index}")
            if index > 26:
                index -= 26
            if uncoded_message[i].islower():
                coded_message += alphabet_number[index]
            else:
                coded_message += str.upper(alphabet_number[index])
            print(f"New letter: {alphabet_number[index]}")
        else:
            coded_message += " "
    print(f"Coded: {coded_message}")


def exercise_74_solution():
    return print("Exercise body")


def exercise_75_solution():
    return print("Exercise body")


def exercise_76_solution():
    return print("Exercise body")


def exercise_77_solution():
    return print("Exercise body")


def exercise_78_solution():
    return print("Exercise body")


def exercise_79_solution():
    return print("Exercise body")


def exercise_80_solution():
    return print("Exercise body")


def exercise_81_solution():
    return print("Exercise body")


def exercise_82_solution():
    return print("Exercise body")


def exercise_83_solution():
    return print("Exercise body")


def exercise_84_solution():
    return print("Exercise body")
