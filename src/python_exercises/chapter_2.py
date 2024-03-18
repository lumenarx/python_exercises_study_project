from exercises import EXERCISE
import __main__
from math import sqrt, floor
from random import randrange
"""
Loading the EXERCISE class that is being used 
to combine an exercise name and a solution into one
"""

exercise_name = {
    35: "Exercise 35: Even or Odd?",
    36: "Exercise 36: Dog Years",
    37: "Exercise 37: Vowel or Consonant",
    38: "Exercise 38: Name That Shape",
    39: "Exercise 39: Month Name to Number of Days",
    40: "Exercise 40: Sound Levels",
    41: "Exercise 41: Classifying Triangles",
    42: "Exercise 42: Note to Frequency",
    43: "Exercise 43: Frequency to Note",
    44: "Exercise 44: Faces on Money",
    45: "Exercise 45: Date to Holiday Name",
    46: "Exercise 46: What Color Is That Square?",
    47: "Exercise 47: Season from Month and Day",
    48: "Exercise 48: Birth Date to Astrological Sign",
    49: "Exercise 49: Chinese Zodiac",
    50: "Exercise 50: Richter Scale",
    51: "Exercise 51: Roots of a Quadratic Function",
    52: "Exercise 52: Letter Grade to Grade Points",
    53: "Exercise 53: Grade Points to Letter Grade",
    54: "Exercise 54: Assessing Employees",
    55: "Exercise 55: Wavelengths of Visible Light",
    56: "Exercise 56: Frequency to Name",
    57: "Exercise 57: Cell Phone Bill",
    58: "Exercise 58: Is It a Leap Year?",
    59: "Exercise 59: Next day",
    60: "Exercise 60: What Day of the Week Is January 1?",
    61: "Exercise 61: Is a License Plate Valid?",
    62: "Exercise 62: Roulette Payouts"
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

EXERCISE_35_NAME = (STMP_1 + "%s" % exercise_name[35])
EXERCISE_36_NAME = (STMP_1 + "%s" % exercise_name[36])
EXERCISE_37_NAME = (STMP_1 + "%s" % exercise_name[37])
EXERCISE_38_NAME = (STMP_1 + "%s" % exercise_name[38])
EXERCISE_39_NAME = (STMP_1 + "%s" % exercise_name[39])
EXERCISE_40_NAME = (STMP_1 + "%s" % exercise_name[40])
EXERCISE_41_NAME = (STMP_1 + "%s" % exercise_name[41])
EXERCISE_42_NAME = (STMP_1 + "%s" % exercise_name[42])
EXERCISE_43_NAME = (STMP_1 + "%s" % exercise_name[43])
EXERCISE_44_NAME = (STMP_1 + "%s" % exercise_name[44])
EXERCISE_45_NAME = (STMP_1 + "%s" % exercise_name[45])
EXERCISE_46_NAME = (STMP_1 + "%s" % exercise_name[46])
EXERCISE_47_NAME = (STMP_1 + "%s" % exercise_name[47])
EXERCISE_48_NAME = (STMP_1 + "%s" % exercise_name[48])
EXERCISE_49_NAME = (STMP_1 + "%s" % exercise_name[49])
EXERCISE_50_NAME = (STMP_1 + "%s" % exercise_name[50])
EXERCISE_51_NAME = (STMP_1 + "%s" % exercise_name[51])
EXERCISE_52_NAME = (STMP_1 + "%s" % exercise_name[52])
EXERCISE_53_NAME = (STMP_1 + "%s" % exercise_name[53])
EXERCISE_54_NAME = (STMP_1 + "%s" % exercise_name[54])
EXERCISE_55_NAME = (STMP_1 + "%s" % exercise_name[55])
EXERCISE_56_NAME = (STMP_1 + "%s" % exercise_name[56])
EXERCISE_57_NAME = (STMP_1 + "%s" % exercise_name[57])
EXERCISE_58_NAME = (STMP_1 + "%s" % exercise_name[58])
EXERCISE_59_NAME = (STMP_1 + "%s" % exercise_name[59])
EXERCISE_60_NAME = (STMP_1 + "%s" % exercise_name[60])
EXERCISE_61_NAME = (STMP_1 + "%s" % exercise_name[61])
EXERCISE_62_NAME = (STMP_1 + "%s" % exercise_name[62])


def menu():
    """Creating chapter's 1 menu"""
    print("[-----------] Menu [-----------] ")
    print("[1111] COPYRIGHT ")
    print("[35] %s" % exercise_name[35])
    print("[36] %s" % exercise_name[36])
    print("[37] %s" % exercise_name[37])
    print("[38] %s" % exercise_name[38])
    print("[39] %s" % exercise_name[39])
    print("[40] %s" % exercise_name[40])
    print("[41] %s" % exercise_name[41])
    print("[42] %s" % exercise_name[42])
    print("[43] %s" % exercise_name[43])
    print("[44] %s" % exercise_name[44])
    print("[45] %s" % exercise_name[45])
    print("[46] %s" % exercise_name[46])
    print("[47] %s" % exercise_name[47])
    print("[48] %s" % exercise_name[48])
    print("[49] %s" % exercise_name[49])
    print("[50] %s" % exercise_name[50])
    print("[51] %s" % exercise_name[51])
    print("[52] %s" % exercise_name[52])
    print("[53] %s" % exercise_name[53])
    print("[54] %s" % exercise_name[54])
    print("[55] %s" % exercise_name[55])
    print("[56] %s" % exercise_name[56])
    print("[57] %s" % exercise_name[57])
    print("[58] %s" % exercise_name[58])
    print("[59] %s" % exercise_name[59])
    print("[60] %s" % exercise_name[60])
    print("[61] %s" % exercise_name[61])
    print("[62] %s" % exercise_name[62])
    print("[0] Exit to the main menu")
    option = int(input("Enter the number of an exercise: "))
    if option == 1111:
        print(COPYRIGHT)
    elif option == 0:
        __main__.menu()
    elif option == 35:
        problem35 = EXERCISE(EXERCISE_35_NAME)
        problem35.run(exercise_35_solution, menu)
    elif option == 36:
        problem35 = EXERCISE(EXERCISE_35_NAME)
        problem35.run(exercise_35_solution, menu)
    elif option == 37:
        problem37 = EXERCISE(EXERCISE_37_NAME)
        problem37.run(exercise_37_solution, menu)
    elif option == 38:
        problem38 = EXERCISE(EXERCISE_38_NAME)
        problem38.run(exercise_38_solution, menu)
    elif option == 39:
        problem39 = EXERCISE(EXERCISE_39_NAME)
        problem39.run(exercise_39_solution, menu)
    elif option == 40:
        problem40 = EXERCISE(EXERCISE_40_NAME)
        problem40.run(exercise_40_solution, menu)
    elif option == 41:
        problem41 = EXERCISE(EXERCISE_41_NAME)
        problem41.run(exercise_41_solution, menu)
    elif option == 42:
        problem42 = EXERCISE(EXERCISE_42_NAME)
        problem42.run(exercise_42_solution, menu)
    elif option == 43:
        problem43 = EXERCISE(EXERCISE_43_NAME)
        problem43.run(exercise_43_solution, menu)
    elif option == 44:
        problem44 = EXERCISE(EXERCISE_44_NAME)
        problem44.run(exercise_44_solution, menu)
    elif option == 45:
        problem45 = EXERCISE(EXERCISE_45_NAME)
        problem45.run(exercise_45_solution, menu)
    elif option == 46:
        problem46 = EXERCISE(EXERCISE_46_NAME)
        problem46.run(exercise_46_solution, menu)
    elif option == 47:
        problem47 = EXERCISE(EXERCISE_47_NAME)
        problem47.run(exercise_47_solution, menu)
    elif option == 48:
        problem48 = EXERCISE(EXERCISE_48_NAME)
        problem48.run(exercise_48_solution, menu)
    elif option == 49:
        problem49 = EXERCISE(EXERCISE_49_NAME)
        problem49.run(exercise_49_solution, menu)
    elif option == 50:
        problem50 = EXERCISE(EXERCISE_50_NAME)
        problem50.run(exercise_50_solution, menu)
    elif option == 51:
        problem51 = EXERCISE(EXERCISE_51_NAME)
        problem51.run(exercise_51_solution, menu)
    elif option == 52:
        problem52 = EXERCISE(EXERCISE_52_NAME)
        problem52.run(exercise_52_solution, menu)
    elif option == 53:
        problem53 = EXERCISE(EXERCISE_53_NAME)
        problem53.run(exercise_53_solution, menu)
    elif option == 54:
        problem54 = EXERCISE(EXERCISE_54_NAME)
        problem54.run(exercise_54_solution, menu)
    elif option == 55:
        problem55 = EXERCISE(EXERCISE_55_NAME)
        problem55.run(exercise_55_solution, menu)
    elif option == 56:
        problem56 = EXERCISE(EXERCISE_56_NAME)
        problem56.run(exercise_56_solution, menu)
    elif option == 57:
        problem57 = EXERCISE(EXERCISE_57_NAME)
        problem57.run(exercise_57_solution, menu)
    elif option == 58:
        problem58 = EXERCISE(EXERCISE_58_NAME)
        problem58.run(exercise_58_solution, menu)
    elif option == 59:
        problem59 = EXERCISE(EXERCISE_59_NAME)
        problem59.run(exercise_59_solution, menu)
    elif option == 60:
        problem60 = EXERCISE(EXERCISE_60_NAME)
        problem60.run(exercise_60_solution, menu)
    elif option == 61:
        problem61 = EXERCISE(EXERCISE_61_NAME)
        problem61.run(exercise_61_solution, menu)
    elif option == 62:
        problem62 = EXERCISE(EXERCISE_62_NAME)
        problem62.run(exercise_62_solution, menu)
    else:
        exit()


def exercise_35_solution():
    n = int(input("Enter an integer: "))
    if n % 2 == 0:
        return print("This is an even number")
    else:
        return print("This is an odd number")


def exercise_36_solution():
    age_human = round(float(input("Enter the age of the person: ")))
    dog_year = 0
    while int(age_human) <= 0:
        print("Have you entered a negative number or zero.")
        age_human = input("Please enter the age of the person as a positive integer: ")
    if age_human / 10.5 > 2:
        dog_year += 2
        age_human -= 21
        dog_year = dog_year + age_human / 4
    else:
        dog_year = age_human / 10.5
    return print("The age of a person, recalculated in dog years: %.2f" % dog_year)


def exercise_37_solution():
    letter = str(input("Enter a letter of the Latin alphabet: "))
    alpha = ['a', 'e', 'i', 'o', 'u']
    k = 0
    for i in range(5):
        if letter.lower() == alpha[i]:
            k = 1
    if k == 1:
        return print("It's a vowel letter.")
    else:
        return print("This is a consonant letter.")


def exercise_38_solution():
    edges = int(input("Enter the number of sides of the shape in the range from 3 to 10: "))
    while edges < 3 or edges > 10:
        edges = int(input("You entered the wrong number. Acceptable values range from 3 to 10: "))
    names = ['Triangle', 'Parallelepiped', 'Pentagon', 'Hexagon', 'Heptagon', 'Octagon', 'Nonagon', 'Decagon']
    k = 0
    for i in range(len(names)):
        if (edges - 3) == i:
            k = i
    return print("The name of the figure: %s" % names[k])


def exercise_39_solution():
    month = str(input("Enter the name of the month: "))
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
              'september', 'october', 'november', 'december']
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = str.lower(month)
    for i in range(len(months)):
        if month == months[i]:
            if i == 1:
                return print("Month " + months[i] + " contains " + str(days[i]) + " days (29 in a leap year).")
            else:
                return print("Month " + months[i] + " contains " + str(days[i]) + " days.")


def exercise_40_solution():
    jackhammer = 130
    lawn_mover = 106
    alarm = 70
    quiet_room = 40
    names = ['quiet room', 'alarm clock', 'gas lawnmower', 'jackhammer']
    db = int(input("Enter the volume level in decibels: "))
    if db == quiet_room:
        return print("The volume level corresponds to a quiet room")
    elif db == alarm:
        return print("The volume level corresponds to the alarm clock")
    elif db == lawn_mover:
        return print("The volume level corresponds to a lawn mower")
    elif db == jackhammer:
        return print("The volume level corresponds to a jackhammer")
    elif db < quiet_room:
        return print("The volume level is less than the level <%s>" % names[0])
    elif quiet_room < db < alarm:
        return print("The volume level is higher than the level <%s> and lower than the level <%s>"
                     % (names[0], names[1]))
    elif alarm < db < lawn_mover:
        return print("The volume level is higher than the level <%s> and lower than the level <%s>"
                     % (names[1], names[2]))
    elif lawn_mover < db < jackhammer:
        return print("The volume level is higher than the level <%s> and lower than the level <%s>"
                     % (names[2], names[3]))
    elif db > jackhammer:
        return print("The volume level is higher than the level <%s>" % names[3])


def exercise_41_solution():
    edge1 = float(input("Enter the length of the first side of the triangle: "))
    edge2 = float(input("Enter the length of the second side of the triangle: "))
    edge3 = float(input("Enter the length of the third side of the triangle: "))
    if (edge1 == edge2 and edge1 != edge3) or (edge1 == edge3
                                               and edge1 != edge2) or (edge2 == edge3 and edge2 != edge1):
        return print("This is an isosceles triangle")
    elif edge1 == edge2 and edge1 == edge3 and edge2 == edge3:
        return print("This is an equilateral triangle triangle")
    else:
        return print("This is a versatile triangle")


def exercise_42_solution():
    note = input("Enter the note and its octave number: ")
    note = str.lower(note)
    letters = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
    freq_list = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
    frequency = 0
    for i in range(7):
        if note[0] == letters[i]:
            frequency = freq_list[i] / 2 ** (4 - int(note[1]))
    note = str.upper(note)
    return print("The frequency of the note %s is equal to %.2f Hz" % (note, frequency))


def exercise_43_solution():
    frequency = float(input("Enter the frequency of the note in the range from 261.63 to 493.88 Hz: "))
    letters = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
    freq_list = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
    note = ""
    for i in range(7):
        if freq_list[i] <= frequency < freq_list[i + 1]:
            note = letters[i] + '4'
            note = str.upper(note)
    return print("The entered frequency corresponds to the note %s" % note)


def exercise_44_solution():
    denomination = [1, 2, 5, 10, 20, 50, 100]
    leaders = ['George Washington', 'Thomas Jefferson', 'Abraham Lincoln',
               'Alexander Hamilton', 'Andrew Jackson', 'Ulysses Grant', 'Benjamin Franklin']
    result = ""
    face_value = int(input("Enter the denomination of the banknote in $: "))
    while check_denomination(face_value, denomination) == 0:
        face_value = int(input("There is no such banknote. Enter the valid denomination of the banknote in $: "))
    for i in range(len(denomination)):
        if face_value == int(denomination[i]):
            result = "On a banknote with a face value of $" + str(face_value) + " pictured " + leaders[i] + "."
    return print(result)


def check_denomination(face_value, denomination):
    for i in range(len(denomination)):
        if face_value == int(denomination[i]):
            return 1
        else:
            return 0


def exercise_45_solution():
    day = int(input("Enter the date of the month: "))
    month = str(input("Enter the month: "))
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
              'september', 'october', 'november', 'december']
    dates = ['1 january', '1 july', '25 december']
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while check(day, month, months, dates) >= 20 or check(day, month, months, dates) == 0:
        if check(day, month, months, dates) >= 20:
            n = check(day, month, months, dates) % 20
            day = int(input("You entered the wrong number, %s has exactly %d days in the month. "
                            "Enter the correct date of the month: " % (months[n], days[n])))
            check(day, month, months, dates)
        else:
            month = str(input("You entered the wrong month. Enter the correct month name: "))
    flag = False
    if check(day, month, months, days) == 1:
        result = str(day) + " " + month
        for i in range(3):
            if result == dates[i]:
                flag = True
            if flag is True:
                return print("The date %s is a holiday in Canada." % dates[i][0:(len(dates[i]) - 1)])
            else:
                return print("There are no holidays on the selected date %s." % result[0:len(result)])


def check(date, month, months, days):
    for i in range(len(months)):
        if month == months[i]:
            if 0 < date <= days[i]:
                return 1
            else:
                result = 20 + i
                return result
        elif i == 11 and month != months[i]:
            return 0


def exercise_46_solution():
    cell = str(input("Enter the cell coordinate: "))
    cell = str.lower(cell)
    alpha = 'abcdefgh'
    black = [0, 2, 4, 6]
    even = False
    for i in range(4):
        if cell[0] == alpha[black[i]]:
            even = True
    if even is True:
        if int(cell[1]) % 2 == 1:
            return print("Cell %s is black" % cell)
        else:
            return print("Cell %s is white" % cell)
    else:
        if int(cell[1]) % 2 == 0:
            return print("Cell %s is black" % cell)
        else:
            return print("Cell %s is white" % cell)


def exercise_47_solution():
    month = input("Enter the month: ")
    day = int(input("Enter the day: "))
    result = str(day) + " " + month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
              'september', 'october', 'november', 'december']
    if ((day > 20 and month == months[11]) or month == months[0]
            or month == months[1] or (day < 20 and month == months[2])):
        return print("Date: %s\nSeason: Winter" % result)
    elif ((day > 19 and month == months[2]) or month == months[3]
          or month == months[4] or (day < 21 and month == months[5])):
        return print("Date: %s\nSeason: Spring" % result)
    elif ((day > 20 and month == months[5]) or month == months[6]
          or month == months[7] or (day < 22 and month == months[8])):
        return print("Date: %s\nSeason: Summer" % result)
    elif ((day > 21 and month == months[8]) or month == months[9]
          or month == months[10] or (day < 21 and month == months[11])):
        return print("Date: %s\nSeason: Autumn" % result)


def exercise_48_solution():
    month = input("Enter the month of your birth: ")
    day = int(input("Enter your birthday: "))
    result = str(day) + " " + month.lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
              'september', 'october', 'november', 'december']
    if (day > 21 and month == months[11]) or (day < 20 and month == months[0]):
        print("Date of birth: %s\nZodiac sign: Capricorn" % result)
    elif (day > 19 and month == months[0]) or (day < 19 and month == months[1]):
        print("Date of birth: %s\nZodiac sign: Aquarius" % result)
    elif (day > 18 and month == months[1]) or (day < 21 and month == months[2]):
        print("Date of birth: %s\nZodiac sign: Pisces" % result)
    elif (day > 20 and month == months[2]) or (day < 20 and month == months[3]):
        print("Date of birth: %s\nZodiac sign: Aries" % result)
    elif (day > 19 and month == months[3]) or (day < 21 and month == months[4]):
        print("Date of birth: %s\nZodiac sign: Taurus" % result)
    elif (day > 20 and month == months[4]) or (day < 21 and month == months[5]):
        print("Date of birth: %s\nZodiac sign: Gemini" % result)
    elif (day > 20 and month == months[5]) or (day < 23 and month == months[6]):
        print("Date of birth: %s\nZodiac sign: Cancer" % result)
    elif (day > 22 and month == months[6]) or (day < 23 and month == months[7]):
        print("Date of birth: %s\nZodiac sign: Leo" % result)
    elif (day > 22 and month == months[7]) or (day < 23 and month == months[8]):
        print("Date of birth: %s\nZodiac sign: Virgo" % result)
    elif (day > 22 and month == months[8]) or (day < 23 and month == months[9]):
        print("Date of birth: %s\nZodiac sign: Libra" % result)
    elif (day > 22 and month == months[9]) or (day < 22 and month == months[10]):
        print("Date of birth: %s\nZodiac sign: Scorpio" % result)
    elif (day > 21 and month == months[10]) or (day < 22 and month == months[11]):
        print("Date of birth: %s\nZodiac sign: Sagittarius" % result)


def exercise_49_solution():
    a = int(input("Enter the year of your birth: "))
    animals = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger',
               'Hare', 'Dragon', 'Snake', 'Horse', 'Sheep']
    b = a % 12
    for j in range(len(animals)):
        if b == j:
            return print("The animal of your year is", animals[j])


def exercise_50_solution():
    a = float(input("Enter the magnitude of the earthquake: "))
    richter_scale = ['Minimal', 'Very Weak', 'Weak', 'Intermediate', 'Moderate', 'Strong',
                     'Very Strong', 'Huge', 'Destructive']
    richter_magnitude = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0]
    if a < 2.0:
        return print("Richter scale magnitude: %.1f\nDescription of the earthquake: %s" % (a, richter_scale[0]))
    elif 2.0 <= a < 8.0:
        for i in range(1, 6, 1):
            b = a - richter_magnitude[i]
            if b < 0:
                return print("Richter scale magnitude: %.1f\nDescription of the earthquake: %s" % (a, richter_scale[i]))
            else:
                return print("Richter scale magnitude: %.1f\nDescription of the earthquake: %s" % (a, richter_scale[8]))


def exercise_51_solution():
    a = int(input("Enter the coefficient a: "))
    b = int(input("Enter the coefficient b: "))
    c = int(input("Enter the coefficient c: "))
    d = (b**2) - 4 * a * c
    if d > 0:
        x1 = ((-b) + sqrt(d)) / (2 * a)
        x2 = ((-b) - sqrt(d)) / (2 * a)
        return print(d, "The equation %dx**2 + %dx + %d = 0 has two valid roots: \n%f\n%f" % (a, b, c, x1, x2))
    elif d == 0:
        x1 = (-b) / (2 * a)
        return print("The equation %dx**2 + %dx + %d = 0 has exactly one root: %f" % (a, b, c, x1))
    else:
        return print("The equation %dx**2 + %dx + %d = 0 has no roots" % (a, b, c))


def exercise_52_solution():
    grade = input("Enter a letter grade:")
    grade_letters = ['A', 'B', 'C', 'D', 'F']
    grade_coefficients = [4, 3, 2, 1, 0]
    ng = 0
    for i in range(len(grade_letters)):
        if grade[0] == grade_letters[i]:
            ng = float(grade_coefficients[i])
            if grade.endswith('+'):
                ng += 0.3
            elif grade.endswith('-') and grade[0] != 'F':
                ng -= 0.3
    return print("Your letter grade is: %s\nYour numerical grade is: %.1f" % (grade, ng))


def exercise_53_solution():
    grade = float(input("Enter a numerical grade:"))
    grade_letters = ['A', 'B', 'C', 'D', 'F']
    grade_coefficients = [4, 3, 2, 1, 0]
    ag = 0
    flag = False
    while grade < 0 or grade > 5.0:
        grade = float(input("Enter a numerical grade from 0 to 5.0: "))
        if 0 <= grade <= 4.0:
            break
    for i in range(len(grade_coefficients)):
        if flag is False:
            b = float(grade) - float(grade_coefficients[i])
            print(b, i)
            if 0 <= b < 1:
                if grade < 1.0:
                    ag = grade_letters[4]
                else:
                    ag = grade_letters[i]
                    if 0 < b <= 0.3:
                        ag += '+'
                    elif b >= 0.7:
                        ag += '-'
                flag = True
    if flag is True:
        return print("Your numerical grade is: %.1f\nYour letter grade is: %s" % (grade, ag))


def exercise_54_solution():
    grades = ['Unacceptable Performance', 'Acceptable Performance', 'Meritorious Performance']
    rating = float(input("Enter your rating as an employee of the company: "))
    while rating < 0 or 0 < rating < 0.4 or (0.4 < rating < 0.6):
        rating = float(input("Please, enter the correct rating value (0, o.4, or 0.6 or more): "))
    premium = 2400 * rating
    if rating == 0.0:
        return print("Your rating of <%.2f> means <%s> and rewarded by the <$%.2f> premium."
                     % (rating, grades[0], premium))
    elif rating == 0.4:
        return print("Your rating of <%.2f> means <%s> and rewarded by the <$%.2f> premium."
                     % (rating, grades[1], premium))
    else:
        return print("Your rating of <%.2f> means <%s> and rewarded by the <$%.2f> premium."
                     % (rating, grades[2], premium))


def exercise_55_solution():
    color = ['Violet', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']
    wavelength = float(input("Enter the value of the wavelength: "))
    while wavelength < 380 or wavelength > 750:
        wavelength = float(input("Your wavelength is outside of visible spectrum.\n"
                                 "Please, enter the correct value of the wavelength in range from 380 to 750 nm: "))
    if 380 <= wavelength < 450:
        return print("The color of <%.2f> nm is <%s>." % (wavelength, color[0]))
    elif 450 <= wavelength < 495:
        return print("The color of <%.2f> nm is <%s>." % (wavelength, color[1]))
    elif 495 <= wavelength < 570:
        return print("The color of <%.2f> nm is <%s>." % (wavelength, color[2]))
    elif 570 <= wavelength < 590:
        return print("The color of <%.2f> nm is <%s>." % (wavelength, color[3]))
    elif 590 <= wavelength < 620:
        return print("The color of <%.2f> nm is <%s>." % (wavelength, color[4]))
    else:
        return print("The color of <%.2f> nm is <%s>." % (wavelength, color[5]))


def exercise_56_solution():
    range_1 = 3 * 10 ** 9
    range_2 = 3 * 10 ** 12
    range_3 = 4.3 * 10 ** 14
    range_4 = 7.5 * 10 ** 14
    range_5 = 3 * 10 ** 17
    range_6 = 3 * 10 ** 19
    radiation = ['Radio Waves', 'Microwaves', 'Infrared Light', 'Visible Light',
                 'Ultraviolet Light', 'X-Rays', 'Gamma Rays']
    frequency = float(input("Enter the radiation frequency: "))
    while frequency == "":
        frequency = float(input("Please, enter the correct value of the radiation frequency: "))
    if frequency < range_1:
        return print("The name of <%.2f> frequency is <%s>." % (frequency, radiation[0]))
    elif range_1 <= frequency < range_2:
        return print("The name of <%.2f> frequency is <%s>." % (frequency, radiation[1]))
    elif range_2 <= frequency < range_3:
        return print("The name of <%.2f> frequency is <%s>." % (frequency, radiation[2]))
    elif range_3 <= frequency < range_4:
        return print("The name of <%.2f> frequency is <%s>." % (frequency, radiation[3]))
    elif range_4 <= frequency < range_5:
        return print("The name of <%.2f> frequency is <%s>." % (frequency, radiation[4]))
    elif range_5 <= frequency < range_6:
        return print("The name of <%.2f> frequency is <%s>." % (frequency, radiation[5]))
    elif frequency > range_6:
        return print("The name of <%.2f> frequency is <%s>." % (frequency, radiation[6]))


def exercise_57_solution():
    minute_cost = 0.25
    minutes_bill = 0
    message_cost = 0.15
    messages_bill = 0
    fee_911 = 0.44
    sales_tax = 0.05
    plan_cost = 15
    bill = f"Base charge: ${plan_cost}\n"
    minutes = float(input("Enter the number of minutes talked in this month: "))
    messages = float(input("Enter the number of messages sent in this month: "))
    if minutes > 50:
        minutes_bill = (minutes - 50) * minute_cost
        additional_minutes = f"Additional minutes: $%.2f\n" % minutes_bill
        bill += additional_minutes
    if messages > 50:
        messages_bill = (messages - 50) * message_cost
        additional_messages = "Additional messages: $%.2f\n" % messages_bill
        bill += additional_messages
    tax = (plan_cost + minutes_bill + messages_bill + fee_911) * sales_tax
    round(tax, 2)
    total_bill = plan_cost + minutes_bill + messages_bill + fee_911 + tax
    bill += f"The 911 fee: ${fee_911}\nTax: $%.2f\nTotal bill: $%.2f" % (tax, total_bill)
    return print(bill)


def exercise_58_solution():
    year = int(input('Enter a year: '))
    if year % 400 == 0:
        return print("A year <%d> is a leap year." % year)
    else:
        if year % 100 == 0:
            return print("A year <%d> is NOT a leap year." % year)
        else:
            if year % 4 == 0:
                return print("A year <%d> is a leap year." % year)
            else:
                return print("A year <%d> is NOT a leap year." % year)


def exercise_59_solution():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = int(input("Enter the year in your date: "))
    while year < 0:
        year = int(input("Please, enter the correct year in your date: "))
    month = int(input("Enter the month in your date: "))
    while month < 0 or month > 12:
        month = int(input("Please, enter the correct month in your date: "))
    day = int(input("Enter the day in your date: "))
    while day < 0 or day > days_in_month[month-1]:
        day = int(input("Please, enter the correct day in your date: "))
    if year % 400 == 0:
        days_in_month[1] += 1
    else:
        if year % 100 == 0:
            print("A year <%d> is NOT a leap year." % year)
        else:
            if year % 4 == 0:
                days_in_month[1] += 1
            else:
                print("A year <%d> is NOT a leap year." % year)
    n = month - 1
    if day == days_in_month[n]:
        month += 1
        day = 1
        if month > 12:
            year += 1
            month = 1
    else:
        day += 1
    if day % 10 >= 0:
        day_str = '0' + str(day)
    else:
        day_str = str(day)
    if month % 10 >= 0:
        month_str = '0' + str(month)
    else:
        month_str = str(month)
    return print("The next date is %d:%s:%s" % (year, month_str, day_str))


def exercise_60_solution():
    year = int(input("Enter the number of year: "))
    while year < 0:
        year = int(input("Please, enter the correct year in your date: "))
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_of_the_week = (year + floor((year - 1)/4) - floor((year-1)/100) + floor((year - 1) / 400)) % 7
    if day_of_the_week == 1:
        return print("The 1st of January is <%s> in <%d>" % (week_days[0], year))
    elif day_of_the_week == 2:
        return print("The 1st of January is <%s> in <%d>" % (week_days[1], year))
    elif day_of_the_week == 3:
        return print("The 1st of January is <%s> in <%d>" % (week_days[2], year))
    elif day_of_the_week == 4:
        return print("The 1st of January is <%s> in <%d>" % (week_days[3], year))
    elif day_of_the_week == 5:
        return print("The 1st of January is <%s> in <%d>" % (week_days[4], year))
    elif day_of_the_week == 6:
        return print("The 1st of January is <%s> in <%d>" % (week_days[5], year))
    else:
        return print("The 1st of January is <%s> in <%d>" % (week_days[6], year))


def exercise_61_solution():
    valid = False
    plate_style_old = False
    plate_style_new = False
    license_plate = str(input("Enter the license plate characters: "))
    while valid is False:
        if len(license_plate) == 6:
            if not (license_plate[0].isupper()) \
                    or not license_plate[1].isupper() \
                    or not license_plate[2].isupper() \
                    or not license_plate[3].isdigit() \
                    or not license_plate[4].isdigit() \
                    or not license_plate[5].isdigit():
                license_plate = str(input("Please, enter the correct license plate characters(ZZZ000 or 0000ZZZ): "))
            else:
                valid = True
                plate_style_old = True
        elif len(license_plate) == 7:
            if not (license_plate[0].isdigit()) \
                    or not license_plate[1].isdigit() \
                    or not license_plate[2].isdigit() \
                    or not license_plate[3].isdigit() \
                    or not license_plate[4].isupper() \
                    or not license_plate[5].isupper() \
                    or not license_plate[6].isupper():
                license_plate = str(input("Please, enter the correct license plate characters(ZZZ000 or 0000ZZZ): "))
            else:
                valid = True
                plate_style_new = True
        else:
            license_plate = str(input("Please, enter the license plate characters(ZZZ000 or 0000ZZZ): "))
    if plate_style_old is True:
        return print("The characters are valid for an OLDER style license plate.")
    elif plate_style_new is True:
        return print("The characters are valid for a NEWER style license plate.")


def exercise_62_solution():
    number = -1
    color = -1
    parity = -1
    half = -1
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    print("[INFO] You can make four different bets in a row:\n"
          "[BET] Single number (1 to 36, or 0, or 00)\n"
          "[BET] Red versus black\n"
          "[BET] Odd versus Even (0 and 00 don't pay out)\n"
          "[BET] 1 to 18 versus 19 to 36\n")
    for bet in range(1, 5):
        if bet == 1:
            number = int(input("[BET] Enter the number you want to place a bet on (1 to 36, or 0, or 00): "))
            while number < 0 or number > 36:
                number = int(input("[BET] Please, enter the correct number you want "
                                   "to place a bet on (1 to 36, or 0, or 00): "))
        elif bet == 2:
            color = int(input("[0] No bet\n"
                              "[1] RED\n"
                              "[2] BLACK\n"
                              "[BET] Enter the number of color you want to place a bet on: "))
            while color != 1 and color != 2 and color != 0:
                color = int(input("[BET] Please, enter the correct number of color you want to place a bet on: "))
        elif bet == 3:
            parity = int(input("[0] No bet\n"
                               "[1] Odd\n"
                               "[2] Even\n"
                               "[BET] Enter the number where you want to place a bet: "))
            while parity != 1 and parity != 2 and parity != 0:
                parity = int(input("[BET] Please, enter the correct number where you want to place a bet (1 or 2): "))
        elif bet == 4:
            half = int(input("[0] No bet\n"
                             "[1] 1 to 18\n"
                             "[2] 19 to 36\n"
                             "[BET] Enter the number where you want to place a bet: "))
            while half != 1 and half != 2 and half != 0:
                half = int(input("[BET] Please, enter the correct number where you want to place a bet (1 or 2): "))
    result = randrange(0, 37)
    print(f"The spin resulted in {result}...")
    if result == 37:
        print(f"Pay 00")
    elif result == number:
        print(f"Pay {number}")
    elif result != 0 and result != 37 and color != 0:
        for i in range(18):
            if result == black[i] and color == 2:
                print(f"Pay Black")
            elif result == red[i] and color == 1:
                print(f"Pay Red")
        if result % 2 == 1 and parity == 1:
            print("Pay Odd")
        elif result % 2 == 0 and parity == 2:
            print("Pay Even")
        elif 0 < result < 19 and half == 1:
            print("Pay 1 to 18")
        elif 18 < result < 37 and half == 2:
            print("Pay 19 to 36")
    return 1
