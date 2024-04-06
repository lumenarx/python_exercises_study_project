from exercises import EXERCISE
from chapter_6 import reverse_lookup
import __main__

"""
Loading the EXERCISE class that is being used 
to combine an exercise name and a solution into one
"""

exercise_name = {
    149: "Exercise 149: Display the Head of a File",
    150: "Exercise 150: Display the Tail of a File",
    151: "Exercise 151: Concatenate Multiple Files",
    152: "Exercise 152: Number the Lines in a File",
    153: "Exercise 153: Find the Longest Word in a File",
    154: "Exercise 154: Letter Frequencies",
    155: "Exercise 155: Words that Occur Most",
    156: "Exercise 156: Sum a Collection of Numbers",
    157: "Exercise 157: Both Letter Grades and Grade Points",
    158: "Exercise 158: Remove Comments",
    159: "Exercise 159: Two Word Random Password",
    160: "Exercise 160: Weird Words",
    161: "Exercise 161: What’s that Element Again?",
    162: "Exercise 162: A Book with No E...",
    163: "Exercise 163: Names that Reached Number One",
    164: "Exercise 164: Gender Neutral Names",
    165: "Exercise 165: Most Births in a given Time Period",
    166: "Exercise 166: Distinct Names",
    167: "Exercise 167: Spell Checker",
    168: "Exercise 168: Repeated Words",
    169: "Exercise 169: Redacting Text in a File",
    170: "Exercise 170: Missing Comments",
    171: "Exercise 171: Consistent Line Lengths",
    172: "Exercise 172: Words with Six Vowels in Order"
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
    "https://doi.org/10.1647/15500-3-030-1503159-3"
)

COPYRIGHT = (
        STMP_1
        + "[ COPYRIGHT ]"
        + STMP_1
        + AUTHORS
        + STMP_2
)

EXERCISE_149_NAME = (STMP_1 + "%s" % exercise_name[149])
EXERCISE_150_NAME = (STMP_1 + "%s" % exercise_name[150])
EXERCISE_151_NAME = (STMP_1 + "%s" % exercise_name[151])
EXERCISE_152_NAME = (STMP_1 + "%s" % exercise_name[152])
EXERCISE_153_NAME = (STMP_1 + "%s" % exercise_name[153])
EXERCISE_154_NAME = (STMP_1 + "%s" % exercise_name[154])
EXERCISE_155_NAME = (STMP_1 + "%s" % exercise_name[155])
EXERCISE_156_NAME = (STMP_1 + "%s" % exercise_name[156])
EXERCISE_157_NAME = (STMP_1 + "%s" % exercise_name[157])
EXERCISE_158_NAME = (STMP_1 + "%s" % exercise_name[158])
EXERCISE_159_NAME = (STMP_1 + "%s" % exercise_name[159])
EXERCISE_160_NAME = (STMP_1 + "%s" % exercise_name[160])
EXERCISE_161_NAME = (STMP_1 + "%s" % exercise_name[161])
EXERCISE_162_NAME = (STMP_1 + "%s" % exercise_name[162])
EXERCISE_163_NAME = (STMP_1 + "%s" % exercise_name[163])
EXERCISE_164_NAME = (STMP_1 + "%s" % exercise_name[164])
EXERCISE_165_NAME = (STMP_1 + "%s" % exercise_name[165])
EXERCISE_166_NAME = (STMP_1 + "%s" % exercise_name[166])
EXERCISE_167_NAME = (STMP_1 + "%s" % exercise_name[167])
EXERCISE_168_NAME = (STMP_1 + "%s" % exercise_name[168])
EXERCISE_169_NAME = (STMP_1 + "%s" % exercise_name[169])
EXERCISE_170_NAME = (STMP_1 + "%s" % exercise_name[170])
EXERCISE_171_NAME = (STMP_1 + "%s" % exercise_name[171])
EXERCISE_172_NAME = (STMP_1 + "%s" % exercise_name[172])


def menu():
    """Creating chapter's 7 menu"""
    print("[-----------] Menu [-----------] ")
    print("[1111] COPYRIGHT ")
    print("[149] %s" % exercise_name[149])
    print("[150] %s" % exercise_name[150])
    print("[151] %s" % exercise_name[151])
    print("[152] %s" % exercise_name[152])
    print("[153] %s" % exercise_name[153])
    print("[154] %s" % exercise_name[154])
    print("[155] %s" % exercise_name[155])
    print("[156] %s" % exercise_name[156])
    print("[157] %s" % exercise_name[157])
    print("[158] %s" % exercise_name[158])
    print("[159] %s" % exercise_name[159])
    print("[160] %s" % exercise_name[160])
    print("[161] %s" % exercise_name[161])
    print("[162] %s" % exercise_name[162])
    print("[163] %s" % exercise_name[163])
    print("[164] %s" % exercise_name[164])
    print("[165] %s" % exercise_name[165])
    print("[166] %s" % exercise_name[166])
    print("[167] %s" % exercise_name[167])
    print("[168] %s" % exercise_name[168])
    print("[169] %s" % exercise_name[169])
    print("[170] %s" % exercise_name[170])
    print("[171] %s" % exercise_name[171])
    print("[172] %s" % exercise_name[172])
    print("[0] Exit to the main menu")
    option = int(input("Enter the number of an exercise: "))
    if option == 1111:
        print(COPYRIGHT)
    elif option == 0:
        __main__.menu()
    elif option == 149:
        problem149 = EXERCISE(EXERCISE_149_NAME)
        problem149.run(exercise_149_solution, menu)
    elif option == 150:
        problem150 = EXERCISE(EXERCISE_150_NAME)
        problem150.run(exercise_150_solution, menu)
    elif option == 151:
        problem151 = EXERCISE(EXERCISE_151_NAME)
        problem151.run(exercise_151_solution, menu)
    elif option == 152:
        problem152 = EXERCISE(EXERCISE_152_NAME)
        problem152.run(exercise_152_solution, menu)
    elif option == 153:
        problem153 = EXERCISE(EXERCISE_153_NAME)
        problem153.run(exercise_153_solution, menu)
    elif option == 154:
        problem154 = EXERCISE(EXERCISE_154_NAME)
        problem154.run(exercise_154_solution, menu)
    elif option == 155:
        problem155 = EXERCISE(EXERCISE_155_NAME)
        problem155.run(exercise_155_solution, menu)
    elif option == 156:
        problem156 = EXERCISE(EXERCISE_156_NAME)
        problem156.run(exercise_156_solution, menu)
    elif option == 157:
        problem157 = EXERCISE(EXERCISE_157_NAME)
        problem157.run(exercise_157_solution, menu)
    elif option == 158:
        problem158 = EXERCISE(EXERCISE_158_NAME)
        problem158.run(exercise_158_solution, menu)
    elif option == 159:
        problem159 = EXERCISE(EXERCISE_159_NAME)
        problem159.run(exercise_159_solution, menu)
    elif option == 160:
        problem160 = EXERCISE(EXERCISE_160_NAME)
        problem160.run(exercise_160_solution, menu)
    elif option == 161:
        problem161 = EXERCISE(EXERCISE_161_NAME)
        problem161.run(exercise_161_solution, menu)
    elif option == 162:
        problem162 = EXERCISE(EXERCISE_162_NAME)
        problem162.run(exercise_162_solution, menu)
    elif option == 163:
        problem163 = EXERCISE(EXERCISE_163_NAME)
        problem163.run(exercise_163_solution, menu)
    elif option == 164:
        problem164 = EXERCISE(EXERCISE_164_NAME)
        problem164.run(exercise_164_solution, menu)
    elif option == 165:
        problem165 = EXERCISE(EXERCISE_165_NAME)
        problem165.run(exercise_165_solution, menu)
    elif option == 166:
        problem166 = EXERCISE(EXERCISE_166_NAME)
        problem166.run(exercise_166_solution, menu)
    elif option == 167:
        problem167 = EXERCISE(EXERCISE_167_NAME)
        problem167.run(exercise_167_solution, menu)
    elif option == 168:
        problem168 = EXERCISE(EXERCISE_168_NAME)
        problem168.run(exercise_168_solution, menu)
    elif option == 169:
        problem169 = EXERCISE(EXERCISE_169_NAME)
        problem169.run(exercise_169_solution, menu)
    elif option == 170:
        problem170 = EXERCISE(EXERCISE_170_NAME)
        problem170.run(exercise_170_solution, menu)
    elif option == 171:
        problem171 = EXERCISE(EXERCISE_171_NAME)
        problem171.run(exercise_171_solution, menu)
    elif option == 172:
        problem172 = EXERCISE(EXERCISE_172_NAME)
        problem172.run(exercise_172_solution, menu)
    else:
        exit()


def exercise_149_solution():
    filename = input("Enter the file location: ")
    file_opened = False
    while file_opened is False:
        try:
            file_object = open(filename, 'r')
            file_opened = True
            line = file_object.readline()
            for i in range(10):
                line = line.rstrip()
                print(line)
                line = file_object.readline()
        except FileNotFoundError:
            print(f"'{filename}' wasn't found. Please try again.")
            filename = input("Enter the file name: ")
    return 1


def exercise_150_solution():
    filename = input("Enter the file name: ")
    file_opened = False
    while file_opened is False:
        try:
            file_object = open(filename, 'r')
            file_opened = True
            tail = []
            line = file_object.readline()
            while line != '':
                line = line.rstrip()
                if len(tail) < 10:
                    tail.append(line)
                else:
                    tail.pop(0)
                    tail.append(line)
                line = file_object.readline()
            for i in range(10):
                print(tail[i])
        except FileNotFoundError:
            print(f"'{filename}' wasn't found. Please try again.")
            filename = input("Enter the file name: ")
    return 1


def exercise_151_solution():
    location = input("Enter the name of the files as: [file 1] [file 2]: ")
    files = location.split()
    files_opened = False
    while files_opened is False:
        try:
            file_1 = open(files[0], 'r')
            file_2 = open(files[1], 'r')
            files_opened = True
            line = file_1.readline()
            while line != '':
                line = line.rstrip()
                print(line)
                line = file_1.readline()
            line = file_2.readline()
            while line != '':
                line = line.rstrip()
                print(line)
                line = file_2.readline()
        except FileNotFoundError:
            print(f"Files weren't found. Please try again.")
            location = input("Enter the name of the files as: [file 1] [file 2]: ")
            files = location.split()
    return 1


def exercise_152_solution():
    filename = input("Enter the file name: ")
    file_opened = False
    while file_opened is False:
        try:
            file_1 = open(filename, 'r')
            file_opened = True
            file_2 = open('E:/elements2.txt', 'w')
            line = file_1.readline()
            i = 1
            while line != '':
                line = line.rstrip()
                new_line = f'{i} ' + line + '\n'
                i += 1
                file_2.write(new_line)
                print(f'[OLD] {line}\n'
                      f'[NEW] {new_line}')
                line = file_1.readline()
        except FileNotFoundError:
            print(f"'{filename}' wasn't found. Please try again.")
            filename = input("Enter the file name: ")
    return 1


def exercise_153_solution():
    filename = input("Enter the file name: ")
    file_opened = False
    while file_opened is False:
        try:
            file_object = open(filename, 'r')
            file_opened = True
            line = file_object.readline()
            n = 0
            word = ''
            while line != '':
                line = line.rstrip()
                if len(line) > n:
                    n = len(line)
                    word = line
                line = file_object.readline()
            print(n, word)
        except FileNotFoundError:
            print(f"'{filename}' wasn't found. Please try again.")
            filename = input("Enter the file name: ")
    return 1


def exercise_154_solution():
    characters = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                  'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                  'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    filename = input("Enter the file name: ")
    file_opened = False
    while file_opened is False:
        try:
            file_object = open(filename, 'r')
            file_opened = True
            line = file_object.readline()
            while line != '':
                line = line.rstrip()
                for i in range(len(line)):
                    characters[line[i].upper()] += 1
                line = file_object.readline()
            k = 1
            for i in characters:
                if k % 3 == 0:
                    print(f"'{i}': {characters[i]}", end=",\n")
                    k = 1
                elif i == 'Z':
                    print(f"'{i}': {characters[i]}")
                else:
                    print(f"'{i}': {characters[i]}", end=", ")
                    k += 1
        except FileNotFoundError:
            print(f"'{filename}' wasn't found. Please try again.")
            filename = input("Enter the file name: ")
    return 1


def exercise_155_solution():
    data = ['John eats breakfast with Maria', 'John works as a real estate manager at John Forest',
            'John has been married for 6 years',
            'Maria works as a school teacher', 'Maria eats dinner with John', 'Maria walks with a dog',
            'Maria can drive a school bus']
    wordlist = open('E:/wordlist.txt', 'w')
    for i in data:
        line = i + '\n'
        wordlist.write(line)
    wordlist.close()
    # filename = input("Enter the file name: ")
    filename = 'E:/wordlist.txt'
    file_opened = False
    words = {}
    while file_opened is False:
        try:
            file_object = open(filename, 'r')
            file_opened = True
            line = file_object.readline()
            while line != '':
                line = line.rstrip()
                line = line.split()
                print(line)
                # REMOVE PUNCTUATION AND SPACES FROM THE LIST
                for i in line:
                    try:
                        words[i] += 1
                    except KeyError:
                        words[i] = 1
                line = file_object.readline()
            frequency = 0
            for i in words:
                if int(words[i]) > frequency:
                    frequency = int(words[i])
            top_words = reverse_lookup(words, frequency)
            print("The most frequent word(s): ", end='')
            for i in range(len(top_words)):
                if i == len(top_words) - 1:
                    print(f"'{top_words[i]}'")
                else:
                    print(f"'{top_words[i]}'", end=', ')

        except FileNotFoundError:
            print(f"'{filename}' wasn't found. Please try again.")
            filename = input("Enter the file name: ")
    return 1


def exercise_156_solution():
    return print("Exercise body")


def exercise_157_solution():
    return print("Exercise body")


def exercise_158_solution():
    return print("Exercise body")


def exercise_159_solution():
    return print("Exercise body")


def exercise_160_solution():
    return print("Exercise body")


def exercise_161_solution():
    return print("Exercise body")


def exercise_162_solution():
    return print("Exercise body")


def exercise_163_solution():
    return print("Exercise body")


def exercise_164_solution():
    return print("Exercise body")


def exercise_165_solution():
    return print("Exercise body")


def exercise_166_solution():
    return print("Exercise body")


def exercise_167_solution():
    return print("Exercise body")


def exercise_168_solution():
    return print("Exercise body")


def exercise_169_solution():
    return print("Exercise body")


def exercise_170_solution():
    return print("Exercise body")


def exercise_171_solution():
    return print("Exercise body")


def exercise_172_solution():
    return print("Exercise body")
