from exercises import EXERCISE
from math import floor, sin, cos, acos, tan, sqrt, log10, radians, pi
from time import asctime
import __main__
"""
Loading the EXERCISE class that is being used 
to combine an exercise name and a solution into one
"""

exercise_name = {
    1: "Exercise 1: Mailing Address",
    2: "Exercise 2: Hello",
    3: "Exercise 3: Area of a Room",
    4: "Exercise 4: Area of a Field",
    5: "Exercise 5: Bottle Deposits",
    6: "Exercise 6: Tax and Tip",
    7: "Exercise 7: Sum of the First n Positive Integers",
    8: "Exercise 8: Widgets and Gizmos",
    9: "Exercise 9: Compound Interest",
    10: "Exercise 10: Arithmetic",
    11: "Exercise 11: Fuel Efficiency",
    12: "Exercise 12: Distance Between Two Points on Earth",
    13: "Exercise 13: Making Change",
    14: "Exercise 14: Height Units",
    15: "Exercise 15: Distance Units",
    16: "Exercise 16: Area and Volume",
    17: "Exercise 17: Heat Capacity",
    18: "Exercise 18: Volume of a Cylinder",
    19: "Exercise 19: Free Fal",
    20: "Exercise 20: Ideal Gas Law",
    21: "Exercise 21: Area of a Triangle",
    22: "Exercise 22: Area of a Triangle (Again)",
    23: "Exercise 23: Area of a Regular Polygon",
    24: "Exercise 24: Units of Time",
    25: "Exercise 25: Units of Time (Again)",
    26: "Exercise 26: Current Time",
    27: "Exercise 27: When is Easter?",
    28: "Exercise 28: Body Mass Index ",
    29: "Exercise 29: Wind Chill",
    30: "Exercise 30: Celsius to Fahrenheit and Kelvin",
    31: "Exercise 31: Units of Pressure",
    32: "Exercise 32: Sum of the Digits in an Integer",
    33: "Exercise 33: Sort 3 Integers",
    34: "Exercise 34: Day Old Bread"
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

EXERCISE_1_NAME = (STMP_1 + "%s" % exercise_name[1])
EXERCISE_2_NAME = (STMP_1 + "%s" % exercise_name[2])
EXERCISE_3_NAME = (STMP_1 + "%s" % exercise_name[3])
EXERCISE_4_NAME = (STMP_1 + "%s" % exercise_name[4])
EXERCISE_5_NAME = (STMP_1 + "%s" % exercise_name[5])
EXERCISE_6_NAME = (STMP_1 + "%s" % exercise_name[6])
EXERCISE_7_NAME = (STMP_1 + "%s" % exercise_name[7])
EXERCISE_8_NAME = (STMP_1 + "%s" % exercise_name[8])
EXERCISE_9_NAME = (STMP_1 + "%s" % exercise_name[9])
EXERCISE_10_NAME = (STMP_1 + "%s" % exercise_name[10])
EXERCISE_11_NAME = (STMP_1 + "%s" % exercise_name[11])
EXERCISE_12_NAME = (STMP_1 + "%s" % exercise_name[12])
EXERCISE_13_NAME = (STMP_1 + "%s" % exercise_name[13])
EXERCISE_14_NAME = (STMP_1 + "%s" % exercise_name[14])
EXERCISE_15_NAME = (STMP_1 + "%s" % exercise_name[15])
EXERCISE_16_NAME = (STMP_1 + "%s" % exercise_name[16])
EXERCISE_17_NAME = (STMP_1 + "%s" % exercise_name[17])
EXERCISE_18_NAME = (STMP_1 + "%s" % exercise_name[18])
EXERCISE_19_NAME = (STMP_1 + "%s" % exercise_name[19])
EXERCISE_20_NAME = (STMP_1 + "%s" % exercise_name[20])
EXERCISE_21_NAME = (STMP_1 + "%s" % exercise_name[21])
EXERCISE_22_NAME = (STMP_1 + "%s" % exercise_name[22])
EXERCISE_23_NAME = (STMP_1 + "%s" % exercise_name[23])
EXERCISE_24_NAME = (STMP_1 + "%s" % exercise_name[24])
EXERCISE_25_NAME = (STMP_1 + "%s" % exercise_name[25])
EXERCISE_26_NAME = (STMP_1 + "%s" % exercise_name[26])
EXERCISE_27_NAME = (STMP_1 + "%s" % exercise_name[27])
EXERCISE_28_NAME = (STMP_1 + "%s" % exercise_name[28])
EXERCISE_29_NAME = (STMP_1 + "%s" % exercise_name[29])
EXERCISE_30_NAME = (STMP_1 + "%s" % exercise_name[30])
EXERCISE_31_NAME = (STMP_1 + "%s" % exercise_name[31])
EXERCISE_32_NAME = (STMP_1 + "%s" % exercise_name[32])
EXERCISE_33_NAME = (STMP_1 + "%s" % exercise_name[33])
EXERCISE_34_NAME = (STMP_1 + "%s" % exercise_name[34])


def menu():
    """Creating chapter's 1 menu"""
    print("[-----------] Menu [-----------] ")
    print("[1111] COPYRIGHT ")
    print("[1] %s" % exercise_name[1])
    print("[2] %s" % exercise_name[2])
    print("[3] %s" % exercise_name[3])
    print("[4] %s" % exercise_name[4])
    print("[5] %s" % exercise_name[5])
    print("[6] %s" % exercise_name[6])
    print("[7] %s" % exercise_name[7])
    print("[8] %s" % exercise_name[8])
    print("[9] %s" % exercise_name[9])
    print("[10] %s" % exercise_name[10])
    print("[11] %s" % exercise_name[11])
    print("[12] %s" % exercise_name[12])
    print("[13] %s" % exercise_name[13])
    print("[14] %s" % exercise_name[14])
    print("[15] %s" % exercise_name[15])
    print("[16] %s" % exercise_name[16])
    print("[17] %s" % exercise_name[17])
    print("[18] %s" % exercise_name[18])
    print("[19] %s" % exercise_name[19])
    print("[20] %s" % exercise_name[20])
    print("[21] %s" % exercise_name[21])
    print("[22] %s" % exercise_name[22])
    print("[23] %s" % exercise_name[23])
    print("[24] %s" % exercise_name[24])
    print("[25] %s" % exercise_name[25])
    print("[26] %s" % exercise_name[26])
    print("[27] %s" % exercise_name[27])
    print("[28] %s" % exercise_name[28])
    print("[29] %s" % exercise_name[29])
    print("[30] %s" % exercise_name[30])
    print("[31] %s" % exercise_name[31])
    print("[32] %s" % exercise_name[32])
    print("[33] %s" % exercise_name[33])
    print("[34] %s" % exercise_name[34])
    print("[0] Exit to the main menu")
    option = int(input("Enter the number of an exercise: "))
    if option == 1111:
        print(COPYRIGHT)
    elif option == 0:
        __main__.menu()
    elif option == 1:
        problem1 = EXERCISE(EXERCISE_1_NAME)
        problem1.run(exercise_1_solution, menu)
    elif option == 2:
        problem2 = EXERCISE(EXERCISE_2_NAME)
        problem2.run(exercise_2_solution, menu)
    elif option == 3:
        problem3 = EXERCISE(EXERCISE_3_NAME)
        problem3.run(exercise_3_solution, menu)
    elif option == 4:
        problem4 = EXERCISE(EXERCISE_4_NAME)
        problem4.run(exercise_4_solution, menu)
    elif option == 5:
        problem5 = EXERCISE(EXERCISE_5_NAME)
        problem5.run(exercise_5_solution, menu)
    elif option == 6:
        problem6 = EXERCISE(EXERCISE_6_NAME)
        problem6.run(exercise_6_solution, menu)
    elif option == 7:
        problem7 = EXERCISE(EXERCISE_7_NAME)
        problem7.run(exercise_7_solution, menu)
    elif option == 8:
        problem8 = EXERCISE(EXERCISE_8_NAME)
        problem8.run(exercise_8_solution, menu)
    elif option == 9:
        problem9 = EXERCISE(EXERCISE_9_NAME)
        problem9.run(exercise_9_solution, menu)
    elif option == 10:
        problem10 = EXERCISE(EXERCISE_10_NAME)
        problem10.run(exercise_10_solution, menu)
    elif option == 11:
        problem11 = EXERCISE(EXERCISE_11_NAME)
        problem11.run(exercise_11_solution, menu)
    elif option == 12:
        problem12 = EXERCISE(EXERCISE_12_NAME)
        problem12.run(exercise_12_solution, menu)
    elif option == 13:
        problem13 = EXERCISE(EXERCISE_13_NAME)
        problem13.run(exercise_13_solution, menu)
    elif option == 14:
        problem14 = EXERCISE(EXERCISE_14_NAME)
        problem14.run(exercise_14_solution, menu)
    elif option == 15:
        problem15 = EXERCISE(EXERCISE_15_NAME)
        problem15.run(exercise_15_solution, menu)
    elif option == 16:
        problem16 = EXERCISE(EXERCISE_16_NAME)
        problem16.run(exercise_16_solution, menu)
    elif option == 17:
        problem17 = EXERCISE(EXERCISE_17_NAME)
        problem17.run(exercise_17_solution, menu)
    elif option == 18:
        problem18 = EXERCISE(EXERCISE_18_NAME)
        problem18.run(exercise_18_solution, menu)
    elif option == 19:
        problem19 = EXERCISE(EXERCISE_19_NAME)
        problem19.run(exercise_19_solution, menu)
    elif option == 20:
        problem20 = EXERCISE(EXERCISE_20_NAME)
        problem20.run(exercise_20_solution, menu)
    elif option == 21:
        problem21 = EXERCISE(EXERCISE_21_NAME)
        problem21.run(exercise_21_solution, menu)
    elif option == 22:
        problem22 = EXERCISE(EXERCISE_22_NAME)
        problem22.run(exercise_22_solution, menu)
    elif option == 23:
        problem23 = EXERCISE(EXERCISE_23_NAME)
        problem23.run(exercise_23_solution, menu)
    elif option == 24:
        problem24 = EXERCISE(EXERCISE_24_NAME)
        problem24.run(exercise_24_solution, menu)
    elif option == 25:
        problem25 = EXERCISE(EXERCISE_25_NAME)
        problem25.run(exercise_25_solution, menu)
    elif option == 26:
        problem26 = EXERCISE(EXERCISE_26_NAME)
        problem26.run(exercise_26_solution, menu)
    elif option == 27:
        problem27 = EXERCISE(EXERCISE_27_NAME)
        problem27.run(exercise_27_solution, menu)
    elif option == 28:
        problem28 = EXERCISE(EXERCISE_28_NAME)
        problem28.run(exercise_28_solution, menu)
    elif option == 29:
        problem29 = EXERCISE(EXERCISE_29_NAME)
        problem29.run(exercise_29_solution, menu)
    elif option == 30:
        problem30 = EXERCISE(EXERCISE_30_NAME)
        problem30.run(exercise_30_solution, menu)
    elif option == 31:
        problem31 = EXERCISE(EXERCISE_31_NAME)
        problem31.run(exercise_31_solution, menu)
    elif option == 32:
        problem32 = EXERCISE(EXERCISE_32_NAME)
        problem32.run(exercise_32_solution, menu)
    elif option == 33:
        problem33 = EXERCISE(EXERCISE_33_NAME)
        problem33.run(exercise_33_solution, menu)
    elif option == 34:
        problem34 = EXERCISE(EXERCISE_34_NAME)
        problem34.run(exercise_34_solution, menu)


def exercise_1_solution():
    name = "Aurelia"
    return (
        print("My name is %s" % name),
        print("My email might look like this one:\n"
              "%s_the_best@gmail.com" % name.lower())
    )


def exercise_2_solution():
    name = str(input("Hi! Please, enter your Name: "))
    return print("Hello, %s!" % name)


def exercise_3_solution():
    width = float(input("Please, enter the width of a room in meters: "))
    length = float(input("Please, enter the length of a room in meters: "))
    area_metric = width * length
    area_us = area_metric * 10.764
    return print("The area of a room is %.2f sq. meters or %.2f sq. ft." % (area_metric, area_us))


def exercise_4_solution():
    length = float(input("Enter the length of a field in feet: "))
    width = float(input("Enter the width of a field in feet: "))
    area = (length * width) / 43560
    return print("The area of the field is %.2f acres" % area)


def exercise_5_solution():
    small_bottles = input("Enter the available quantity of bottles with a volume of 1 litre of less: ")
    large_bottles = input("Enter the available quantity of bottles with a volume of more than 1 litre: ")
    price_1 = 0.10
    price_2 = 0.25
    summ = float(small_bottles) * price_1 + float(large_bottles) * price_2
    return print("The total revenue will be equal to: $%.2f" % summ)


def exercise_6_solution():
    check = float(input("Enter the amount of your order in $: "))
    tips = check * 0.18
    tax = check * 0.2
    summ = check + tax + tips
    return print("Total: $%.2f\nTax: $%.2f\nTips: $%.2f" % (summ, tax, tips))


def exercise_7_solution():
    n = int(input("Enter a positive integer number: "))
    summ = int(n * (n + 1) / 2)
    return print("The sum of the first n positive integers is: %d" % summ)


def exercise_8_solution():
    widget = 75
    gizmo = 125
    widget_count = int(input("Enter the quantity of the bought widgets: "))
    gizmo_count = int(input("Enter the quantity of the bought gizmos: "))
    weight = widget_count * widget + gizmo_count * gizmo
    if weight < 1000:
        return print("Total shipping weight: %.2f grams" % weight)
    else:
        return print("Total shipping weight: %.2f kilos" % (weight / 1000))


def exercise_9_solution():
    present_value = float(input("Enter the deposit value: "))
    percent = 0.04
    first_year = float(present_value * (1 + percent) ** 1)
    second_year = float(present_value * (1 + percent) ** 2)
    third_year = float(present_value * (1 + percent) ** 3)
    return print("The amount on the account:\n "
                 "1st year- %.2f\n "
                 "2nd year = %.2f\n "
                 "3rd year - %.2f"
                 % (first_year, second_year, third_year)
                 )


def exercise_10_solution():
    a = int(input("Enter the integer number a: "))
    b = int(input("Enter the integer number b: "))
    summ = a + b
    substr = a - b
    multiplication = a * b
    division = a / b
    reminder = a % b
    logarithm = log10(a)
    exponent = a ** b
    return print("Sum: %d\nDifference: %d\nProduct: %d \nQuotient: %.2f\nReminder a/b: %d\n"
                 "Tenth logarithm a: %.2f\nThe number a to the power b: %d"
                 % (summ, substr, multiplication, division, reminder, logarithm, exponent)
                 )


def exercise_11_solution():
    us_mpg = float(input("Enter the fuel consumption in miles per gallon: "))
    ca_lpk = float(us_mpg / 235.215)
    return print("Conversion into canadian system of litres per kilometers: %.2f" % ca_lpk)


def exercise_12_solution():
    latitude_1 = radians(float(input("Enter the latitude of the first point: ")))
    longitude_1 = radians(float(input("Enter the longitude of the first point: ")))
    latitude_2 = radians(float(input("Enter the latitude of the second point: ")))
    longitude_2 = radians(float(input("Enter the longitude of the second point: ")))
    distance = 6371.01 * acos(
        sin(latitude_1) * sin(latitude_2) + cos(latitude_1) * cos(latitude_2) * cos(
            longitude_1 - longitude_2))
    return print("The distance between the two point equals: %.2f" % distance)
    # Example: Warsaw (52.2297, 21.0122) to Berlin(52.5200, 13.4050)


def exercise_13_solution():
    change = float(input("Enter the change sum: "))
    nickels = [2, 1, 0.25, 0.1, 0.05, 0.01]
    counter = [0, 0, 0, 0, 0, 0]
    k = 0
    for i in range(0, 5):
        while change > 0 and i < 6:
            if change - float(nickels[i]) >= 0:
                change = change - float(nickels[i])
                change = round(change, 2)
                counter[i] += 1
            elif change == 0 or change - float(nickels[i]) < 0:
                k += 1
            else:
                break
    print("You change will look like:")
    coins = ["2 dollars", "1 dollar", "25 cents", "10 cents", "5 cents", "1 cent"]
    for i in range(6):
        if counter[i] > 0:
            text = str(counter[i]) + " coins denominated " + str(coins[i])
            print(text)


def exercise_14_solution():
    length = float(input("Enter the length of a field in feet: "))
    width = float(input("Enter the width of a field in feet: "))
    area = (length * width) / 43560
    return print("The area of the field is %.2f acres" % area)


def exercise_15_solution():
    distance = float(input("Enter the distance in feet: "))
    inches = distance * 12
    yard = distance / 3
    mile = distance / 5280
    return print("Distance in inches: %.2f\nDistance in yards: %.2f\nDistance in miles: %.2f" % (inches, yard, mile))


def exercise_16_solution():
    r = float(input("Enter the radius: "))
    area = pi * r ** 2
    volume = 4 / 3 * pi * r ** 3
    return print("The area of the circle is equal to: %.2f\nThe volume of the ball is equal to: %.2f" % (area, volume))


def exercise_17_solution():
    weight = float(input("Enter the mass of water in kg: "))
    delta_t = float(input("Enter the temperature difference in degrees Celsius: "))
    const = 4.186
    q = weight * const * delta_t
    print("The amount of energy needed to change the temperature: %.2f joules" % q)
    print("There is an extension to this program! Do you like coffee?")
    """Program extension"""
    coffee = 0.35
    temp = 85
    q2 = coffee * const * temp
    cost = q2 * 2.77778 * 10 ** -7
    return print("The cost of heating a 350 ml cup of coffee from 15 to 100 degrees is equal to: %.10f kWh" % cost)


def exercise_18_solution():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))

    """Calculating the volume of the cylinder
    :return print: str - string format of calculated volume of the cylinder
    """
    volume = pi * radius ** 2 * height
    return print("The volume of the cylinder is equal to: %.1f" % volume)


def exercise_19_solution():
    a = 9.8
    v = 0
    height = float(input("Enter the height in meters from which the object should be lowered: "))
    vf = sqrt(v ** 2 + 2 * a * height)
    return print("The velocity of the object's contact with the ground is %.2f meters per second" % vf)


def exercise_20_solution():
    p = float(input("Enter the pressure in pascal: "))
    v = float(input("Enter the volume in liters: "))
    t = float(input("Enter the temperature in Celsius: "))
    r = 8.3145
    t += 273.15
    n = (p * v) / (r * t)
    return print("The amount of gas is equal to %f" % n)


def exercise_21_solution():
    b = float(input("Enter the length of the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    area = b * h / 2
    return print("The area of the triangle is: %.2f" % area)


def exercise_22_solution():
    s1 = float(input("Enter the length of the first side of the triangle: "))
    s2 = float(input("Enter the length of the second side of the triangle: "))
    s3 = float(input("Enter the length of the third side of the triangle: "))
    s = (s1 + s2 + s3) / 2
    area = (s * (s - s1) * (s - s2) * (s - s3)) ** 1 / 2
    return print("The area of the triangle is equal to: %f" % area)


def exercise_23_solution():
    s = float(input("Enter the length of the side of the regular polygon: "))
    n = float(input("Enter the number of sides of a regular polygon: "))
    area = (n * s) / 4 * tan(pi / n)
    return print("The area of a regular polygon is: %f" % area)


def exercise_24_solution():
    days = int(input("Enter the number of days: "))
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    secs = int(input("Enter the number of seconds: "))
    seconds = secs + (minutes * 60) + (hours * 60 ** 2) + (days * 60 ** 3)
    return print("The number of seconds in the specified time interval %d" % seconds)


def exercise_25_solution():
    secs = round(int(input("Enter the total number of seconds: ")))
    days = 0
    hours = 0
    minutes = 0
    while secs > 0:
        if secs >= 216000:
            days += 1
            secs -= 216000
        elif 3600 <= secs < 216000:
            hours += 1
            secs -= 3600
        elif 60 <= secs < 3600:
            minutes += 1
            secs -= 60
        else:
            break
    return print("The time interval is %d:%02d:%02d:%02d" % (days, hours, minutes, secs))


def exercise_26_solution():
    return print(asctime())


def exercise_27_solution():
    year = int(input("Enter the year in which you want to find out the date of Easter: "))
    a = year % 19
    b = floor(year / 100)
    c = year % 100
    d = floor(b / 4)
    e = b % 4
    f = floor((b + 8) / 25)
    g = floor((b - f + 1) / 3)
    h = (19 * a + b - d - g + 15) % 30
    i = floor(c / 4)
    k = c % 4
    el = (32 + 2 * e + 2 * i - h - k) % 7
    m = floor((a + 11 * h + 22 * el) / 451)
    month = (h + el + 7 * m + 114) / 31
    n = int(month) - 1
    day = ((h + 1 - 7 * m + 114) % 31) + 1
    titles = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    result = 'Month: ' + titles[n] + '\nNumber: ' + str(day)
    return print(result)


def exercise_28_solution():
    height = float(input("Enter your height: "))
    weight = float(input("Enter your weight: "))
    n = 0
    bmi = 0
    while n != 1 or n != 2:
        if n == 1 or n == 2:
            break
        else:
            n = int(input("Select the measurement system and enter the number: 1 - colonial, 2 - metric: "))
    if n == 1:
        bmi = (weight / height ** 2) * 703
    elif n == 2:
        bmi = (weight / height ** 2)
    return print("Your body mass index is: %.6f" % bmi)


def exercise_29_solution():
    t = float(input("Enter the air temperature: "))
    v = float(input("Enter the wind speed: "))
    wci = round(13.12 + 0.6215 * t - 11.37 * v ** 0.16 + 0.3965 * t * v ** 0.16)
    return print("Wind cooling coefficient: %d" % wci)


def exercise_30_solution():
    t = float(input("Enter the temperature in Celsius: "))
    t_f = (t * 9 / 5) + 32
    t_k = t + 273.15
    return print("Celsius: %.2f\nFahrenheits: %.2f\nKelvins: %.2f" % (t, t_f, t_k))


def exercise_31_solution():
    p = float(input("Enter the pressure value in kPa: "))
    psi = p / 6.895
    pmm = p * 760 / 101.325
    return print("kPa: %.2f\nPound per sq. meter inch: %.2f\nMillimeters of mercury: %.2f" % (p, psi, pmm))


def exercise_32_solution():
    n = str(input("Enter a four-digit integer: "))
    num = []
    addition = 0
    for i in range(len(n)):
        num.append(int(n[i]))
        addition += num[i]
    return print("The sum of the numbers in the number is equal to: %d" % addition)


def exercise_33_solution():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))
    numbers = [num1, num2, num3]
    max_n = max(numbers)
    min_n = min(numbers)
    addition = numbers[0] + numbers[1] + numbers[2]
    avr_n = addition - max_n - min_n
    return print("Maximum: %d\nRemaining: %d\nMinimum: %d" % (max_n, avr_n, min_n))


def exercise_34_solution():
    quantity = int(input("Enter the number of loaves purchased: "))
    p = 3.49
    discounted = 0.4 * p
    check = quantity * discounted
    return print("The usual price: $%.2f\nDiscounted price: $%.2f\nTotal purchase price: $%.2f"
                 % (p, discounted, check))
