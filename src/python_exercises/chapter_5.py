import random

from exercises import EXERCISE
import __main__

"""
Loading the EXERCISE class that is being used 
to combine an exercise name and a solution into one
"""

exercise_name = {
    110: "Exercise 110: Sorted Order",
    111: "Exercise 111: Reverse Order",
    112: "Exercise 112: Remove Outliers",
    113: "Exercise 113: Avoiding Duplicates",
    114: "Exercise 114: Negatives, Zeros and Positives",
    115: "Exercise 115: List of Proper Divisors",
    116: "Exercise 116: Perfect Numbers",
    117: "Exercise 117: Only the Words",
    118: "Exercise 118: Word by Word Palindromes",
    119: "Exercise 119: Below and Above Average",
    120: "Exercise 120: Formatting a List",
    121: "Exercise 121: Random Lottery Numbers",
    122: "Exercise 122: Pig Latin",
    123: "Exercise 123: Pig Latin Improved",
    124: "Exercise 124: Line of Best Fit",
    125: "Exercise 125: Shuffling a Deck of Cards",
    126: "Exercise 126: Dealing Hands of Cards",
    127: "Exercise 127: Is a List already in Sorted Order?",
    128: "Exercise 128: Count the Elements",
    129: "Exercise 129: Tokenizing a String",
    130: "Exercise 130: Unary and Binary Operators",
    131: "Exercise 131: Infix to Postfix",
    132: "Exercise 132: Evaluate Postfix",
    133: "Exercise 133: Does a List Contain a Sublist?",
    134: "Exercise 134: Generate All Sublists of a List",
    135: "Exercise 135: The Sieve of Eratosthenes"
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
    "https://doi.org/10.1257/11600-3-030-1113120-3"
)

COPYRIGHT = (
        STMP_1
        + "[ COPYRIGHT ]"
        + STMP_1
        + AUTHORS
        + STMP_2
)

EXERCISE_110_NAME = (STMP_1 + "%s" % exercise_name[110])
EXERCISE_111_NAME = (STMP_1 + "%s" % exercise_name[111])
EXERCISE_112_NAME = (STMP_1 + "%s" % exercise_name[112])
EXERCISE_113_NAME = (STMP_1 + "%s" % exercise_name[113])
EXERCISE_114_NAME = (STMP_1 + "%s" % exercise_name[114])
EXERCISE_115_NAME = (STMP_1 + "%s" % exercise_name[115])
EXERCISE_116_NAME = (STMP_1 + "%s" % exercise_name[116])
EXERCISE_117_NAME = (STMP_1 + "%s" % exercise_name[117])
EXERCISE_118_NAME = (STMP_1 + "%s" % exercise_name[118])
EXERCISE_119_NAME = (STMP_1 + "%s" % exercise_name[119])
EXERCISE_120_NAME = (STMP_1 + "%s" % exercise_name[120])
EXERCISE_121_NAME = (STMP_1 + "%s" % exercise_name[121])
EXERCISE_122_NAME = (STMP_1 + "%s" % exercise_name[122])
EXERCISE_123_NAME = (STMP_1 + "%s" % exercise_name[123])
EXERCISE_124_NAME = (STMP_1 + "%s" % exercise_name[124])
EXERCISE_125_NAME = (STMP_1 + "%s" % exercise_name[125])
EXERCISE_126_NAME = (STMP_1 + "%s" % exercise_name[126])
EXERCISE_127_NAME = (STMP_1 + "%s" % exercise_name[127])
EXERCISE_128_NAME = (STMP_1 + "%s" % exercise_name[128])
EXERCISE_129_NAME = (STMP_1 + "%s" % exercise_name[129])
EXERCISE_130_NAME = (STMP_1 + "%s" % exercise_name[130])
EXERCISE_131_NAME = (STMP_1 + "%s" % exercise_name[131])
EXERCISE_132_NAME = (STMP_1 + "%s" % exercise_name[132])
EXERCISE_133_NAME = (STMP_1 + "%s" % exercise_name[133])
EXERCISE_134_NAME = (STMP_1 + "%s" % exercise_name[134])
EXERCISE_135_NAME = (STMP_1 + "%s" % exercise_name[135])


def menu():
    """Creating chapter's 5 menu"""
    print("[-----------] Menu [-----------] ")
    print("[1111] COPYRIGHT ")
    print("[110] %s" % exercise_name[110])
    print("[111] %s" % exercise_name[111])
    print("[112] %s" % exercise_name[112])
    print("[113] %s" % exercise_name[113])
    print("[114] %s" % exercise_name[114])
    print("[115] %s" % exercise_name[115])
    print("[116] %s" % exercise_name[116])
    print("[117] %s" % exercise_name[117])
    print("[118] %s" % exercise_name[118])
    print("[119] %s" % exercise_name[119])
    print("[120] %s" % exercise_name[120])
    print("[121] %s" % exercise_name[121])
    print("[122] %s" % exercise_name[122])
    print("[123] %s" % exercise_name[123])
    print("[124] %s" % exercise_name[124])
    print("[125] %s" % exercise_name[125])
    print("[126] %s" % exercise_name[126])
    print("[127] %s" % exercise_name[127])
    print("[128] %s" % exercise_name[128])
    print("[129] %s" % exercise_name[129])
    print("[130] %s" % exercise_name[130])
    print("[131] %s" % exercise_name[131])
    print("[132] %s" % exercise_name[132])
    print("[133] %s" % exercise_name[133])
    print("[134] %s" % exercise_name[134])
    print("[135] %s" % exercise_name[135])
    print("[0] Exit to the main menu")
    option = int(input("Enter the number of an exercise: "))
    if option == 1111:
        print(COPYRIGHT)
    elif option == 0:
        __main__.menu()
    elif option == 110:
        problem110 = EXERCISE(EXERCISE_110_NAME)
        problem110.run(exercise_110_solution, menu)
    elif option == 111:
        problem111 = EXERCISE(EXERCISE_111_NAME)
        problem111.run(exercise_111_solution, menu)
    elif option == 112:
        problem112 = EXERCISE(EXERCISE_112_NAME)
        problem112.run(exercise_112_solution, menu)
    elif option == 113:
        problem113 = EXERCISE(EXERCISE_113_NAME)
        problem113.run(exercise_113_solution, menu)
    elif option == 114:
        problem114 = EXERCISE(EXERCISE_114_NAME)
        problem114.run(exercise_114_solution, menu)
    elif option == 115:
        problem115 = EXERCISE(EXERCISE_115_NAME)
        problem115.run(exercise_115_solution, menu)
    elif option == 116:
        problem116 = EXERCISE(EXERCISE_116_NAME)
        problem116.run(exercise_116_solution, menu)
    elif option == 117:
        problem117 = EXERCISE(EXERCISE_117_NAME)
        problem117.run(exercise_117_solution, menu)
    elif option == 118:
        problem118 = EXERCISE(EXERCISE_118_NAME)
        problem118.run(exercise_118_solution, menu)
    elif option == 119:
        problem119 = EXERCISE(EXERCISE_119_NAME)
        problem119.run(exercise_119_solution, menu)
    elif option == 120:
        problem120 = EXERCISE(EXERCISE_120_NAME)
        problem120.run(exercise_120_solution, menu)
    elif option == 121:
        problem121 = EXERCISE(EXERCISE_121_NAME)
        problem121.run(exercise_121_solution, menu)
    elif option == 122:
        problem122 = EXERCISE(EXERCISE_122_NAME)
        problem122.run(exercise_122_solution, menu)
    elif option == 123:
        problem123 = EXERCISE(EXERCISE_123_NAME)
        problem123.run(exercise_123_solution, menu)
    elif option == 124:
        problem124 = EXERCISE(EXERCISE_124_NAME)
        problem124.run(exercise_124_solution, menu)
    elif option == 125:
        problem125 = EXERCISE(EXERCISE_125_NAME)
        problem125.run(exercise_125_solution, menu)
    elif option == 126:
        problem126 = EXERCISE(EXERCISE_126_NAME)
        problem126.run(exercise_126_solution, menu)
    elif option == 127:
        problem127 = EXERCISE(EXERCISE_127_NAME)
        problem127.run(exercise_127_solution, menu)
    elif option == 128:
        problem128 = EXERCISE(EXERCISE_128_NAME)
        problem128.run(exercise_128_solution, menu)
    elif option == 129:
        problem129 = EXERCISE(EXERCISE_129_NAME)
        problem129.run(exercise_129_solution, menu)
    elif option == 130:
        problem130 = EXERCISE(EXERCISE_130_NAME)
        problem130.run(exercise_130_solution, menu)
    elif option == 131:
        problem131 = EXERCISE(EXERCISE_131_NAME)
        problem131.run(exercise_131_solution, menu)
    elif option == 132:
        problem132 = EXERCISE(EXERCISE_132_NAME)
        problem132.run(exercise_132_solution, menu)
    elif option == 133:
        problem133 = EXERCISE(EXERCISE_133_NAME)
        problem133.run(exercise_133_solution, menu)
    elif option == 134:
        problem134 = EXERCISE(EXERCISE_134_NAME)
        problem134.run(exercise_134_solution, menu)
    elif option == 135:
        problem135 = EXERCISE(EXERCISE_135_NAME)
        problem135.run(exercise_135_solution, menu)
    else:
        exit()


def exercise_110_solution():
    data = []
    line = ""
    while line != 0:
        line = int(input("Enter an integer: "))
        if line != 0:
            data.append(line)
    data.sort()
    n = len(data)
    for i in range(n):
        print(data[i])
    return 1


def exercise_111_solution():
    data = []
    line = ""
    while line != 0:
        line = int(input("Enter an integer: "))
        if line != 0:
            data.append(line)
    data.sort(reverse=True)
    n = len(data)
    for i in range(n):
        print(data[i])
    return 1


def exercise_112_solution():
    data = []
    line = ""
    while line != 0:
        line = int(input("Enter an integer: "))
        if line != 0:
            data.append(line)
        else:
            if len(data) < 4:
                return 0
    return print(remove_outliers(data))


def remove_outliers(data):
    data_copy = data
    data_copy.sort()
    first = data_copy[0]
    last = data_copy[len(data) - 1]
    data_copy.remove(first)
    data_copy.remove(last)
    return data_copy


def exercise_113_solution():
    data = []
    line = " "
    while line != "":
        line = input("Enter a word: ")
        if line != "":
            data.append(line)
    data.sort()
    return print(remove_duplicate(data))


def remove_duplicate(data):
    k = 0
    g = 0
    n = len(data)
    while g != n - 1:
        if g + 1 < n - 1:
            k = g + 1
        while k != len(data):
            if data[g] == data[k]:
                if data[g] != data[k]:
                    g += 1
                    break
                else:
                    data.pop(k)
                    break
            else:
                if data[g] != data[k]:
                    g += 1
                    break
                else:
                    data.pop(k)
                    break
        n = len(data)
    return data


def exercise_114_solution():
    data = []
    negative = []
    zero = []
    positive = []
    line = " "
    while line != "":
        line = input("Enter an integer: ")
        if line != "":
            if line[0] == "-":
                negative.append(line)
            elif line[0] == "0":
                zero.append(line)
            else:
                positive.append(line)
    for i in range(len(negative)):
        data.append(negative[i])
    for i in range(len(zero)):
        data.append(zero[i])
    for i in range(len(positive)):
        data.append(positive[i])
    print(data)


def exercise_115_solution():
    number = int(input("Enter an integer: "))
    return print(proper_divisors(number))


def proper_divisors(number):
    data = []
    d = 1
    while d < number:
        if number % d == 0:
            data.append(d)
        d += 1
    return data


def exercise_116_solution():
    for g in range(1, 10001):
        if perfect_number(g) is True:
            print(f"{g} is a perfect number.")
    return 1


def perfect_number(number):
    data = proper_divisors(number)
    n = len(data)
    sum_data = 0
    for i in range(n):
        sum_data += int(data[i])
    if sum_data == number:
        return True
    else:
        return False


def exercise_117_solution():
    line = input("Enter a text: ")
    return print(only_words(line))


def only_words(line):
    line_copy = ""
    n = len(line)
    for i in range(n):
        if (i != n - 1 and line[i] == "'" and line[i + 1] != " " and line[i + 1] != "'") or (
                line[i] == "'" and i == n - 1):
            line_copy += line[i].lower()
        elif line[i] != "'" and line[i] != "!" and line[i] != "?" and line[i] != "." \
                and line[i] != "," and line[i] != ":" and line[i] != ";" \
                and line[i] != "-" and line[i] != "_" and line[i] != "+":
            line_copy += line[i].lower()
    words = line_copy.split()
    return words


def exercise_118_solution():
    # line1 = "Herb the sage eats sage, the herb"
    # line2 = "Information school graduate seeks graduate school information"
    # line3 = "This is a wonderful day today."
    line = input("Enter a text: ")
    while line.strip() == "":
        line = input("Please, enter a text: ")
    return word_palindromes(line)


def word_palindromes(sentence):
    data = only_words(sentence)
    if len(data) % 2 == 1:
        n = len(data) // 2
        for i in range(n):
            end = len(data) - (i + 1)
            if data[i] == data[end] and i == n - 1:
                print("This is a palindrome. Wow!")
            elif data[i] == data[end]:
                print("This could be a palindrome. Checking next...")
            else:
                print("This is not a palindrome.")
                return 0
    else:
        print("This is not a palindrome.")
        return 0


def exercise_119_solution():
    numbers = []
    line = 0
    temp = 0
    while line != "":
        if line != "":
            try:
                line = input("Enter an integer: ")
                temp = int(line)
            except:
                print("This is not an integer. Please, try again.")
            if isinstance(temp, int) is True:
                numbers.append(temp)
        else:
            break
    average = 0
    n = len(numbers)
    for i in numbers:
        average += i
        if i == n - 1:
            average /= n
    print(f"The average value is: {average}")
    return below_and_above(average, numbers)


def below_and_above(average, data):
    data.sort()
    below_avg, equal_avg, above_avg = [], [], []
    for i in data:
        if i < average:
            below_avg.append(i)
        elif i == average:
            equal_avg.append(i)
        elif i > average:
            above_avg.append(i)
    if len(below_avg) > 0:
        print("Below average values:\n", below_avg)
    if len(equal_avg) > 0:
        print("Average values:\n", equal_avg)
    if len(above_avg) > 0:
        print("Above average values:\n", above_avg)
    return print("Your data is processed.")


def exercise_120_solution():
    my_list = []
    line = " "
    while line != "":
        line = input("Enter a word or number: ")
        if line.strip() != "":
            my_list.append(line)
    return format_list(my_list)


def format_list(data):
    line = ""
    n = len(data)
    for i in range(n):
        if i == 0 and n != 2 and n != 1:
            line += data[i] + ", "
        elif i == 0 and n == 1:
            line += data[i]
        elif i == 0 and n == 2:
            line += data[i] + " and "
        elif i == 1 and n == 2:
            line += data[i]
        elif i == n - 2 and n != 2:
            line += data[i] + " and "
        elif i == n - 1 and n != 2:
            line += data[i]
        elif i != 0 and i != n - 1 and i != n - 2 and n != 2:
            line += data[i] + ", "
    return print(line)


def exercise_121_solution():
    data = []
    while len(data) < 6:
        if len(data) == 0:
            number = random.randrange(0, 49)
            if number != 0 and len(data) == 0:
                data.append(number)
        else:
            flag = False
            number = random.randrange(0, 49)
            for i in range(len(data)):
                if data[i] == number:
                    flag = True
                if i == len(data) - 1 and flag is False:
                    data.append(number)
    data.sort()
    result = "The winning ticket contains: "
    for i in range(len(data)):
        result += str(data[i])
        if i == len(data) - 1:
            result += "."
        else:
            result += ", "
    return print(result)


def exercise_122_solution():
    text = "john young meets bill and eats apple"
    print(text)
    return print(pig_latin(text))


def pig_latin(text):
    data = only_words(text)
    result = ""
    n = len(data)
    for i in range(n):
        if check_vowel(data[i][0]) is True and data[i][0] != "y":
            data[i] += "way"
        else:
            j = 0
            end = ""
            while j < len(data[i]):
                if check_vowel(data[i][j]) is True:
                    data[i] += end
                    last = len(data[i]) - 1
                    if data[i][last] == "a":
                        data[i] += "y"
                    else:
                        data[i] += "ay"
                    break
                else:
                    end += data[i][j]
                    data[i] = remove_char(data[i], j)
        result += data[i] + " "
    return result


def remove_char(text, i):
    t = bytearray(text, 'utf-8')
    del t[i]
    return t.decode()


def check_vowel(letter):
    if letter == "a" or letter == "o" or letter == "i" \
            or letter == "e" or letter == "u" or letter == "y":
        return True
    else:
        return False


def exercise_123_solution():
    return print("Exercise body")


def exercise_124_solution():
    return print("Exercise body")


def exercise_125_solution():
    return print("Exercise body")


def exercise_126_solution():
    return print("Exercise body")


def exercise_127_solution():
    return print("Exercise body")


def exercise_128_solution():
    return print("Exercise body")


def exercise_129_solution():
    return print("Exercise body")


def exercise_130_solution():
    return print("Exercise body")


def exercise_131_solution():
    return print("Exercise body")


def exercise_132_solution():
    return print("Exercise body")


def exercise_133_solution():
    return print("Exercise body")


def exercise_134_solution():
    return print("Exercise body")


def exercise_135_solution():
    return print("Exercise body")
