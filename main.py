from logic import input_from_console, input_from_file, random_system

print("Welcome to linear equations system solver!\n")

while 1:
    try:
        print("Available functionality:\n" +
              "\t1. Input linear system manually.\n" +
              "\t2. Read linear system from file.\n" +
              "\t3. Generate linear system with random coefficient.\n" +
              "\t4. Exit.")
        answer = input().strip()
        if answer == "1":
            input_from_console()
        elif answer == "2":
            print("File must contain linear system in format:\n" +
                  "\t a11 a12 ... a1n | b1\n" +
                  "\t a21 a22 ... a2n | b2\n" +
                  "\t ... ... ... ...  ...\n" +
                  "\t an1 an2 ... ann | bn")
            input_from_file(input("Please write path to file:").strip())
        elif answer == "3":
            print("Generating system...")
            random_system()
        elif answer == "4":
            print("Exit.")
            break
        else:
            print("Incorrect input. Please choose again.")
    except KeyboardInterrupt:
        print("Finished work...")
