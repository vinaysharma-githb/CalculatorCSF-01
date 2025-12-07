


def calculator():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            Num = int(input("Enter your choice: "))

            

            if Num not in [1, 2, 3, 4]:
                raise Exception("Invalid")

            A = float(input("Enter first number: "))
            B = float(input("Enter second number: "))

            if Num == 1:
                print("Addition:", A + B)

            elif Num == 2:
                print("Subtraction:", A - B)

            elif Num == 3:
                print("Multiplication:", A * B)

            elif Num == 4:
                try:
                    print("Division:", A/B)
                except ZeroDivisionError:
                    print("Error is coming")
            if Num == 5:
                print("Exit")
                break

        except ValueError:
            print("Error")

        except Exception as e:
            print("Error1:", e)


calculator()

        
