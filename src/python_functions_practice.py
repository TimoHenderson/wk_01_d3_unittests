def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 // num_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(num):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[num-1]

def number_to_short_month_name(num):
    return number_to_full_month_name(num)[0:3]

def volume_of_cube(length):
    return length ** 3

def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit -32) * (5 / 9)
    return celcius