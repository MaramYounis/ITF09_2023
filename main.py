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
#Q1
def concatenate_dicts(*dicts):
    concatenated_dict = {}
    for d in dicts:
        concatenated_dict.update(d)
    return concatenated_dict

dict1 = {"Name" : "Amal" , "Age" : 20}
dict2 =  {"City" : 'Gaza', "Gender" : "Female"}
dict3 = {'Name' : "Amal", 'Age' : 20, 'City' : 'Gaza', 'Gender': 'Female'}

result_dict = concatenate_dicts(dict1, dict2,dict3)
print(result_dict)





# Q 2
def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive values")
    return length * width

def calculate_rectangle_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive values")
    return 2 * (length + width)

try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = calculate_rectangle_area(length, width)
    perimeter = calculate_rectangle_perimeter(length, width)

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")

except ValueError as e:
    print(f"Error: {e}")


