from exercises import EXERCISE
from random import randrange
from chapter_5 import check_punctuation
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
    dic1 = {}
    for i in range(2, 13):
        dic1[str(i)] = 0
    print(dic1)
    dic2 = {
        "2": 2.78,
        "3": 5.56,
        "4": 8.33,
        "5": 11.11,
        "6": 13.89,
        "7": 16.67,
        "8": 13.89,
        "9": 11.11,
        "10": 8.33,
        "11": 5.56,
        "12": 2.78
    }
    for i in range(1000):
        k = str(dice())
        dic1[k] += 1
    n = len(dic1)
    print("Total    Simulated    Expected")
    print("           Percent     Percent")
    for i in dic1:
        if int(i) < 10:
            x = " " + i
        else:
            x = i
        temp = dic1[i] / 10
        if temp < 10:
            y = " " + str(temp)
        else:
            y = str(temp)
        if (dic2[i] < 10 and int(i) < 10 and temp < 10) or (dic2[i] < 10 and temp < 10):
            z = " " + str(dic2[i])
        else:
            z = str(dic2[i])
        print(f"{x}            {y}       {z}")
    return 1


def dice():
    dice_1 = randrange(1, 7)
    dice_2 = randrange(1, 7)
    result = dice_1 + dice_2
    return result


def exercise_138_solution():
    buttons = {1: ".,?!:",
               2: "ABC",
               3: "DEF",
               4: "GHI",
               5: "JKL",
               6: "MNO",
               7: "PQRS",
               8: "TUV",
               9: "WXYZ",
               0: " "}
    text = "Hello, world!"
    print(text)
    result = ""
    for k in range(len(text)):
        for i in buttons:
            for j in range(len(buttons[i])):
                if text[k].lower() == buttons[i][j].lower():
                    result += str(i) * (j + 1)
    return print(result)


def exercise_139_solution():
    morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
             'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
             'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
             'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
             '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.'}
    text = "Hello, world!"
    text_to_morse = ""
    for i in text:
        if i == " ":
            text_to_morse += i
        else:
            if check_punctuation(i) is False:
                text_to_morse += morse[i.upper()]
    return print(f"'{text}' in Morse code: {text_to_morse}")


def exercise_140_solution():
    postal_code = ''
    while postal_code == '' and len(postal_code) != 6 and check_template(postal_code) is False:
        if postal_code == '':
            postal_code = input('Enter a postal code (G4A1B3 or similar): ')
            if check_template(postal_code) is False:
                postal_code = ''
    explain_postal_code(postal_code)
    return 1


def check_template(postal_code):
    if postal_code == '':
        return False
    elif len(postal_code) != 6 and postal_code != '':
        print('The postal code must be 6 characters long.')
        return False
    elif len(postal_code) == 6:
        for i in postal_code:
            if i.islower() is True:
                print('The postal code is invalid.')
                return False
    if postal_code[0].isalpha() is False or postal_code[2].isalpha() is False or postal_code[4].isalpha() is False:
        print(f'The postal code is invalid. 1st, 3rd and 5th characters must be letters.')
        return False
    if postal_code[1].isnumeric() is False or postal_code[3].isnumeric() is False or postal_code[
        5].isnumeric() is False:
        print(f'The postal code is invalid. 2nd, 4th and 6th characters must be numbers.')
        return False
    else:
        return True


def explain_postal_code(postal_code):
    provinces = {'A': 'Newfoundland', 'B': 'Nova Scotia', 'C': 'Prince Edward Island', 'E': 'New Brunswick',
                 'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec', 'K': 'Ontario', 'L': 'Ontario', 'M': 'Ontario',
                 'N': 'Ontario', 'P': 'Ontario', 'R': 'Manitoba', 'S': 'Saskatchewan', 'T': 'Alberta',
                 'V': 'British Columbia', 'X': 'Nunavut or Northwest Territories', 'Y': 'Yukon'}
    result = ''
    if provinces[postal_code[0].upper()]:
        result += 'Province/Territory: ' + provinces[postal_code[0]] + '\n'
    else:
        return print(f'The postal code is invalid. There is no region with {postal_code[0]} code.')
    if postal_code[1] == '0':
        result += 'Area: rural'
    else:
        result += 'Area: urban'
    return print(result)


def exercise_141_solution():
    numbers = [7, 13, 19, 25, 78, 80, 91, 101, 123, 216, 888, 976]
    print("SHOWCASE")
    for n in numbers:
        print(n, '-', write_out_number(n))
    print("END OF SHOWCASE")
    try:
        number = int(input("Enter an integer: "))
        print(number, '-', write_out_number(number))
    except TypeError:
        print("Incorrect input. Try again...")

    return 1


def write_out_number(number):
    words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
             10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
             17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
             60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred', 200: 'two hundred',
             300: 'three hundred', 400: 'four hundred', 500: 'five hundred', 600: 'six hundred', 700: 'seven hundred',
             800: 'eight hundred', 900: 'nine hundred'}
    n = len(str(number))
    new_number = ''
    decomposed = []
    a = (number // 100) * 100
    b = (number % 100) - ((number % 100) % 10)
    c = (number % 100) % 10
    if n > 1 and 10 < number % 100 < 20:
        b += c
        c = 0
    if a != 0:
        decomposed.append(a)
    if b != 0:
        decomposed.append(b)
    if c != 0:
        decomposed.append(c)
    n = len(decomposed)
    for i in range(n):
        if i == 0 and number % 100 > 0 and number // 100 > 0:
            new_number += words[decomposed[i]] + ' and '
        else:
            new_number += words[decomposed[i]] + ' '
    return new_number


def exercise_142_solution():
    text = "Hello, world!"
    unique_characters(text)
    return 1


def unique_characters(text):
    characters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
                  'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
                  'w': 0, 'x': 0, 'y': 0, 'z': 0, ',': 0, '.': 0, '!': 0, '?': 0, ':': 0, ';': 0, '@': 0,
                  '#': 0, '$': 0, '%': 0, '*': 0, "'": 0, '"': 0, '0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
                  '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '-': 0, '+': 0, '=': 0, '_': 0, ' ': 0
                  }
    n = len(text)
    unique = 0
    for i in text:
        characters[i.lower()] += 1
    for i in characters:
        if characters[i] > 0:
            unique += 1
    return print(f"'{text}' has {unique} unique characters")


def exercise_143_solution():
    word = ['live', 'fundamental']
    anagram = ['evil', 'talnemdunfa']
    n = len(word)
    for i in range(n):
        print(f'Word {i + 1}: {word[i]};\nAnagram {i + 1}: {anagram[i]};')
        if anagrams(word[i], anagram[i]):
            print(f'Answer: {anagram[i]} is an anagram.')
        else:
            print(f'Answer: {anagram[i]} is NOT an anagram.')
    return 1


def anagrams(text1, text2):
    word1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
             'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
             'w': 0, 'x': 0, 'y': 0, 'z': 0}
    word2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
             'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
             'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for i in text1:
        word1[i.lower()] += 1
    for j in text2:
        word2[j.lower()] += 1
    if word1 == word2:
        return True
    else:
        return False


def exercise_144_solution():
    word = ['William Shakespeare', 'Software Developer']
    anagram = ['I am a weakish speller', 'Project Manager']
    n = len(word)
    for i in range(n):
        print(f'Word {i + 1}: {word[i]};\nAnagram {i + 1}: {anagram[i]};')
        if anagrams_extended(word[i], anagram[i]):
            print(f'Answer: {anagram[i]} is an anagram.\n')
        else:
            print(f'Answer: {anagram[i]} is NOT an anagram.\n')
    return 1


def remove_spaces(text):
    new_text = ''
    for i in range(len(text)):
        if text[i] != " ":
            new_text += text[i]
    return new_text


def anagrams_extended(text1, text2):
    word1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
             'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
             'w': 0, 'x': 0, 'y': 0, 'z': 0}
    word2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
             'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
             'w': 0, 'x': 0, 'y': 0, 'z': 0}
    new_text1 = remove_spaces(text1)
    new_text2 = remove_spaces(text2)
    for i in new_text1:
        word1[i.lower()] += 1
    for j in new_text2:
        word2[j.lower()] += 1
    if word1 == word2:
        return True
    else:
        return False


def exercise_145_solution():
    return print("Exercise body")


def exercise_146_solution():
    return print("Exercise body")


def exercise_147_solution():
    return print("Exercise body")


def exercise_148_solution():
    return print("Exercise body")
