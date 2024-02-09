class StringInputAndOutput:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Введите строку: ")

    def printString(self):
        print("Строка в верхнем регистре:", self.input_string.upper())


string = StringInputAndOutput()
string.getString()
string.printString()

