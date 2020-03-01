from logic import input_from_console, input_from_file, random_system
print("Welcome to linear system solver!\n")
flag = bool(1)
while flag:
    print("Available functionality:\n" +
          "1. Input linear system manually.\n" +
          "2. Read linear system from file.\n" +
          "3. Generate linear system with random coefficient.\n" +
          "4. Exit.")
    answer = input()
    if answer == "1":
        print("Please input coefficient")
        input_from_console()
    elif answer == "2":
        print("File must contain linear system in format:\n" +
              " a11 a12 ... a1n | b1\n" +
              " a21 a22 ... a2n | b2\n" +
              " ... ... ... ... . ..\n" +
              " an1 an2 ... ann | bn")
        input_from_file(input("Please write path to file:"))
    elif answer == "3":
        print("Generating system...")
        random_system()
    elif answer == "4":
        print("Exit.")
        flag = bool(0)
    else:
        print("Incorrect input. Please choose again.")
