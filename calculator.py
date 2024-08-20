from math import sqrt


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def square(n1):
    return n1 ** 2

keys = {"+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "^": sqrt}

def calculator():
    print("Welcome to the calculator\n")

    keepGoing = True
    num1 = float(input("Enter a number\n"))
    while keepGoing:
        for key in keys:
            print(key)
        operator = str(input("What operator would you like to do?\n"))
        if operator == "^":
            output = square(num1)
        else:
            num2 = float(input("Enter another number\n"))
            if operator in keys.keys():
                output = keys[operator](num1, num2)
            else:
                print("Invalid input\n")

        if operator == "^":
            print(f"{num1} squared is {output}")
        else:
            print(f"The result of {num1} {operator} {num2} is {output}")

        cont = str(input(("Would you like to continue with this number? Type yes or no\n"))).lower()
        if cont == "yes":
            num1 = output
            keepGoing = True
        elif cont == "no":
            restart = str(input("Would you like to restart the program? Type yes or no\n").lower())
            if restart == "yes":
                calculator()
            elif restart == "no":
                print("Thank you for using this program\n")
                keepGoing = False
            else:
                print("Invalid input\n")
        else:
            print("Invalid input\n")


calculator()

