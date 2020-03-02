import random

if __name__ == "__main__":
    print("It's a file with logic and computation, please run \'main.py\'")


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
            calculator = Calculator(n, optimize(a, n))
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
        print(a)
        print(n)
        calculator = Calculator(n, optimize(a, n))
        calculator.calculate()
    except FileNotFoundError:
        print("File " + path + " don't exist.")
        return
    except UnboundLocalError:
        return



def random_system():
    try:
        n = int(input("Number of equations (less than 20 and more than 1):").strip())
        if 20 >= n > 1:
            a = []
            for i in range(n):
                line = []
                for j in range(n):
                    line.append(random.random() * 100 - 50)
                line.append("|")
                line.append(random.random() * 100 - 50)
                a.append(line)
            calculator = Calculator(n, a)
            calculator.calculate()
        else:
            print("Incorrect input.")
            return
    except ValueError:
        print("Incorrect input.")


def optimize(arr, n):
    i = 0
    while i < n:
        j = 0
        while j < n:
            arr[i][j] = float(arr[i][j])
            j += 1
        arr[i][j + 1] = float(arr[i][j + 1])
        i += 1
    return arr


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


def make_matrix(sys):
    i = 0
    while i < len(sys):
        sys[i] = sys[i][:-2:] + sys[i][-1]
        i += 1
    return sys


class Calculator:
    n = 0
    x = []
    system = []
    det = 0

    def __init__(self, n, system):
        self.n = n
        self.system = system
        self.x = []

    def calculate(self):
        print("\nMain system:\n")
        self.__print_system()
        self.__make_triangle()
        print("\nTriangle system:\n")
        self.__print_system()
        self.__get_determinate()
        self.__x_calculation()
        self.__print_x()
        self.__get_residuals()

    def __check_diagonal(self, i):
        j = i
        while j < self.n:
            if self.system[j][i] != 0 and self.system[i][j] != 0:
                swap = self.system[j]
                self.system[j] = self.system[i]
                self.system[i] = swap
                return
            j += 1
        print("No solutions")
        return ArithmeticError

    def __x_calculation(self):
        i = self.n - 2
        self.x.append(self.system[self.n - 1][-1]/self.system[self.n - 1][self.n - 1])
        while i > -1:
            k = self.n - 1
            value = self.system[i][-1]
            while k > i:
                value -= self.x[self.n - 1 - k] * self.system[i][k]
                k -= 1
            self.x.append(value/self.system[i][i])
            i -= 1

    def __make_triangle(self):
        try:
            i = 0
            while i < self.n:
                if self.system[i][i] == 0:
                    self.__check_diagonal(i)
                m = i
                while m < self.n - 1:
                    a = -(self.system[m + 1][i] / self.system[i][i])
                    j = i
                    while j < self.n:
                        self.system[m + 1][j] += a * self.system[i][j]
                        j += 1
                    self.system[m + 1][-1] += a * self.system[i][-1]
                    m += 1
                k = 0
                line_sum = 0
                while k < self.n:
                    line_sum += self.system[i][k]
                    k += 1
                if line_sum == 0:
                    print("This system is incompatible, no solutions")
                    return ArithmeticError
                i += 1
        except ValueError:
            print("Incorrect working data.")
        except ArithmeticError:
            print("")

    def __print_system(self):
        i = 0
        while i < self.n:
            j = 0
            while j < self.n:
                print(str(self.system[i][j]) + " x_" + str(j) + " ", end='')
                j += 1
            print(str(self.system[i][-2]) + " " + str(self.system[i][-1]), end='')
            print("")
            i += 1

    def __print_x(self):
        i = 0
        print("\nSolutions:")
        self.x.reverse()
        while i < self.n:
            print("\tX_" + str(i) + ": " + str(self.x[i]))
            i += 1

    def __get_determinate(self):
        i = 0
        self.det = 1
        while i < self.n:
            self.det *= self.system[i][i]
            i += 1
        print("\nDeterminant: " + str(self.det))

    def __get_residuals(self):
        i = 0
        print("\nResiduals:")
        while i < self.n:
            res = 0
            j = 0
            while j < self.n:
                res += self.system[i][j] * self.x[j]
                j += 1
            res -= self.system[i][-1]
            i += 1
            print("\tResidual for row №" + str(i) + " = " + str(abs(res)))
        print("")
