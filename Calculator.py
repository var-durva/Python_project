def Calculator():
    print("===Simple Python Calculator")
    print("Perform any operations: '+', '-', '*', '/'")

    try:
        num1 = float(input("Enter first number: "))
        oper = input("Select any opeartions: ")
        num2 = float(input("Enter second number: "))

        if oper == "+":
            result = num1 + num2
        elif oper == "-":
            result = num1 - num2
        elif oper == "*":
            result = num1 * num2
        elif oper == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1/num2
        else:
            print("Invalid operator!")
            return

        print(f"Result: {result}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")


Calculator()

