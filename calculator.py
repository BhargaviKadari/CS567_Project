import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of a negative number"
    return math.sqrt(x)

def exponentiation(x, y):
    return x ** y

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm(x):
    if x <= 0:
        return "Error: Cannot calculate logarithm for a non-positive number"
    return math.log(x)

def factorial(x):
    if x < 0:
        return "Error: Cannot calculate factorial of a negative number"
    if x == 0:
        return 1
    return math.factorial(x)

def absolute_value(x):
    return abs(x)

def gcd(x, y):
    return math.gcd(int(x), int(y))

def lcm(x, y):
    return (x * y) // gcd(x, y)

def arc_sine(x):
    return math.degrees(math.asin(x))

def arc_cosine(x):
    return math.degrees(math.acos(x))

def arc_tangent(x):
    return math.degrees(math.atan(x))

def hyperbolic_sine(x):
    return math.sinh(x)

def hyperbolic_cosine(x):
    return math.cosh(x)

def hyperbolic_tangent(x):
    return math.tanh(x)

def ceil(x):
    return math.ceil(x)

def floor(x):
    return math.floor(x)

def round_to_nearest(x):
    return round(x)

def calculator():
    print("Welcome to the Scientific Calculator!")
    while True:
        print("\nOptions:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Exponentiation")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Logarithm")
        print("11. Factorial")
        print("12. Absolute Value")
        print("13. Greatest Common Divisor (GCD)")
        print("14. Least Common Multiple (LCM)")
        print("15. Arc Sine")
        print("16. Arc Cosine")
        print("17. Arc Tangent")
        print("18. Hyperbolic Sine")
        print("19. Hyperbolic Cosine")
        print("20. Hyperbolic Tangent")
        print("21. Ceiling (Round up)")
        print("22. Floor (Round down)")
        print("23. Round to Nearest Integer")
        print("24. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24): ")

        if choice == "24":
            print("Thank you for using the Scientific Calculator!")
            break

        if choice in ["1", "2", "3", "4", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]:
            num1 = float(input("Enter the first number: "))
            if choice not in ["5", "11", "12", "15", "16", "17", "18", "19", "20", "21", "22", "23"]:
                num2 = float(input("Enter the second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        elif choice == "5":
            num = float(input("Enter a number: "))
            print("Result:", square_root(num))
        elif choice == "6":
            print("Result:", exponentiation(num1, num2))
        elif choice == "7":
            angle = float(input("Enter an angle in degrees: "))
            print("Result:", sine(angle))
        elif choice == "8":
            angle = float(input("Enter an angle in degrees: "))
            print("Result:", cosine(angle))
        elif choice == "9":
            angle = float(input("Enter an angle in degrees: "))
            print("Result:", tangent(angle))
        elif choice == "10":
            num = float(input("Enter a number: "))
            print("Result:", logarithm(num))
        elif choice == "11":
            num = float(input("Enter a number: "))
            print("Result:", factorial(num))
        elif choice == "12":
            num = float(input("Enter a number: "))
            print("Result:", absolute_value(num))
        elif choice == "13":
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print("Result:", gcd(x, y))
        elif choice == "14":
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            print("Result:", lcm(x, y))
        elif choice == "15":
            num = float(input("Enter a number: "))
            print("Result:", arc_sine(num))
        elif choice == "16":
            num = float(input("Enter a number: "))
            print("Result:", arc_cosine(num))
        elif choice == "17":
            num = float(input("Enter a number: "))
            print("Result:", arc_tangent(num))
        elif choice == "18":
            num = float(input("Enter a number: "))
            print("Result:", hyperbolic_sine(num))
        elif choice == "19":
            num = float(input("Enter a number: "))
            print("Result:", hyperbolic_cosine(num))
        elif choice == "20":
            num = float(input("Enter a number: "))
            print("Result:", hyperbolic_tangent(num))
        elif choice == "21":
            num = float(input("Enter a number: "))
            print("Result:", ceil(num))
        elif choice == "22":
            num = float(input("Enter a number: "))
            print("Result:", floor(num))
        elif choice == "23":
            num = float(input("Enter a number: "))
            print("Result:", round_to_nearest(num))
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    calculator()
