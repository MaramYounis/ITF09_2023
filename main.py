# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import math

def sum_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

def subtract_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is: {result}")

def multiply_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")

def divide_numbers():
    num1 = float(input("Enter the dividend: "))
    num2 = float(input("Enter the divisor: "))
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")

def calculate_triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")

def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * 2
    print(f"The area of the circle is: {area}")

def calculate_rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")

while True:
    print("\nMain Menu:")
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Calculate triangle area")
    print("6. Calculate circle area")
    print("7. Calculate rectangle area")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        sum_numbers()
    elif choice == '2':
        subtract_numbers()
    elif choice == '3':
        multiply_numbers()
    elif choice == '4':
        divide_numbers()
    elif choice == '5':
        calculate_triangle_area()
    elif choice == '6':
        calculate_circle_area()
    elif choice == '7':
        calculate_rectangle_area()
    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
