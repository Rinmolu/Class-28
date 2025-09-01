class stringUppercase:
    def __init__(self):
        self.str = ""
    def getvalue(self):
        self.str = input("Enter String: ")
    def printvalue(self):
        print("Result Is ", self.str.upper())
str1 = stringUppercase()
str1.getvalue()
str1.printvalue()
    