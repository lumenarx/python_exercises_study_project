def launch():
    """Output of a text block with borders at the BEGINNING of the program execution"""
    return print("---------------------------------------------------------------------------\n"
                 "[ SOLUTION ]")


def finish():
    """Output of a text block with borders at the END of the program execution"""
    return print("[ THE PROGRAM IS COMPLETED ]\n"
                 "---------------------------------------------------------------------------")


class EXERCISE:
    """Creating a class to combine problem conditions and demonstrate their solutions"""
    def __init__(self, title):
        self.title = title

    def run(self, solution):
        print(self.title)
        launch()
        solution()
        finish()
        return 1
