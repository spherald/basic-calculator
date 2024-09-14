def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return f"Error: {e}"

def main():
    while True:
        sign = input("What kind of operation do you wish to do? [+, -, *, /] or 'q' to quit: ")
        if sign == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        if sign not in ['+', '-', '*', '/']:
            print("Please input valid operations. Available operations include [+, -, *, /]")
            continue

        while True:
            try:
                num1 = int(input("Please choose your first number: "))
                num2 = int(input("Please choose your second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter integers only.")
                continue

        if sign == "+":
            result = add(num1, num2)
        elif sign == "-":
            result = subtract(num1, num2)
        elif sign == "*":
            result = multiply(num1, num2)
        elif sign == "/":
            result = divide(num1, num2)

        print(f"The result of {num1} {sign} {num2} is: {result}")

if __name__ == "__main__":
    main()