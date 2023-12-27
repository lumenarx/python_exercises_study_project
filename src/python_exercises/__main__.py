import chapter_1
import chapter_2
import chapter_3
import exercises


def menu():
    print("[1] Chapter 1")
    print("[2] Chapter 2")
    print("[3] Chapter 3")
    print("[4] Chapter 4")
    print("[5] Chapter 5")
    print("[6] Chapter 6")
    print("[7] Chapter 7")
    print("[8] Chapter 8")
    print("[0] Exit the program")
    option = int(input("Enter the number of a charter: "))
    if option == 1:
        chapter_1.menu()
    elif option == 2:
        chapter_2.menu()
    elif option == 3:
        chapter_3.menu()
    elif option == 4:
        chapter_4.menu()
    elif option == 5:
        chapter_5.menu()
    elif option == 6:
        chapter_6.menu()
    elif option == 7:
        chapter_7.menu()
    elif option == 8:
        chapter_8.menu()
    else:
        print("You have finished the execution of the program")
        exit()


if __name__ == "__main__":
    menu()
