import random


def input_from_console():
    try:
        n = int(input("Number of equations (less than 20 and more than 1):").strip())
        if 20 >= n > 1:
            print("Please write equations in format:\n" +
                  " ai1 ai2 ... aij | bi ")
            a = []
            for i in range(n):
                while 1:
                    line = list((input(str(i + 1) + ". ").split()))
                    if (int(len(line) - 2) != n) or (line[-2] != "|"):
                        print("Number of rows is not equals to the number of columns\n" +
                              "or incorrect input, please enter again:")
                    else:
                        a.append(line)
                        break
            calculator = Calculator(n, a)
            calculator.calculate()
        else:
            print("Incorrect input.")
            return
    except ValueError:
        print("Incorrect input.")


def input_from_file(path):
    try:
        n = 0
        a = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if line != "\n" and line != " " and line != " \n":
                    n += 1
        file.close()
        with open(path, 'r', encoding='utf-8') as file:
            for row in file:
                line = list(row.split())
                if line[-2] != "|" or len(line) - 2 != n:
                    print("Incorrect file contents.")
                    return
                a.append(list(line))
        file.close()
        calculator = Calculator(n, a)
        calculator.calculate()
    except FileNotFoundError:
        print("File " + path + " don't exist.")


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def random_system():
    try:
        n = int(input("Number of equations (less than 20 and more than 1):").strip())
        if 20 >= n > 1:
            a = []
            for i in range(n):
                line = []
                for j in range(n):
                    line.append(toFixed((random.random() * 100 - 50), 2))
                line.append("|")
                line.append(toFixed((random.random() * 100 - 50), 2))
                a.append(line)
            calculator = Calculator(n, a)
            calculator.calculate()
        else:
            print("Incorrect input.")
            return
    except ValueError:
        print("Incorrect input.")


class Calculator:

    n = 0
    system = []

    def __init__(self, n, system):
        self.n = n
        self.system = system

    def calculate(self):
        self.system
