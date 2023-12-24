def launch():
    """Output of a text block with borders at the BEGINNING of the program execution"""
    return print("---------------------------------------------------------------------------\n"
                 "[ SOLUTION ]")


def finish(menu):
    """Output of a text block with borders at the END of the program execution"""
    try:
        print("[ THE PROGRAM IS COMPLETED ]\n"
              "---------------------------------------------------------------------------")
        menu_return = str(input("Do you want to return to the menu? (y/n): "))
        if menu_return.lower() == "y":
            return menu()
        else:
            exit()
    except KeyboardInterrupt:
        exit()


class EXERCISE:
    """Creating a class to combine problem conditions and demonstrate their solutions"""
    def __init__(self, title):
        self.title = title

    def run(self, solution, menu):
        print(self.title)
        launch()
        solution()
        finish(menu)
        return 1
