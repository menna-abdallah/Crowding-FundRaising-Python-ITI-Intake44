user_input = input("Please enter a number: ")

if user_input.isdigit():
    number = int(user_input)
    if 20 <= number <= 50:
        print(f'{number} is within the range 20-50.')
    else:
        print(f'{number} is not within the range 20-50.')
else:
    print("please Enter a valid number")

"""///////////////// 2 //////////////////////////////"""

def rectangle_area():
    return 2 * 3

def rectangle_perimeter():
    return 2 * (5 + 3)   

area = rectangle_area()
perimeter = rectangle_perimeter()

print('------------- - 2 - -------------')
print(f"The area is: {area}")
print(f"The perimeter is: {perimeter}")

"""////////////////// 3 /////////////////////////////"""

def concatenate(str1, str2):
    str3 = str1 + str2
    return str3

def join_String(str1,str2):
    str3 = ''.join([str1, str2])
    return str3

str1 = "Hello"
str2 = "World"
str3 = concatenate(str1,str2)

print('------------- - 3 - -------------')

print(f"method1 +: {str3}")
str3 = join_String(str1,str3)
print(f"method2 join(): {str3}")

"""////////////////// 4 /////////////////////////////"""

def square_list(*args):
    squared_list = []
    for num in args:
        squared_list.append(num ** 2)
    return squared_list

squared_values = square_list(1, 2, 3, 4, 5)

print('------------- - 4 - -------------')

print("Squared list:", squared_values)


"""////////////////// 5 /////////////////////////////"""

def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}  
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict= merge_dicts(dict1, dict2)

print('------------- - 5 - -------------')
print("Merged dictionary", merged_dict)

"""////////////////// 6 /////////////////////////////"""
def merge_lists(list1, list2):
    list3 = list1 + list2
    return list3

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = merge_lists(list1, list2)

print('------------- - 6 - -------------')
print("Merged list:", list3)


"""////////////////// 7 /////////////////////////////"""

def check_keys_exist(dictionary):
    dic_keys = dictionary.keys()
    keys_to_check = {"job", "card_number"}

    return keys_to_check.issubset(dic_keys)

dict = {
    "name": "jone",
    "email": "jane@outlook.com",
    "age": 25,
    "job": "engineer",
    "address": "cairo, Egypt"
}

keys_exist = check_keys_exist(dict)
print('------------- - 7 - -------------')
print("Do 'job' and 'card_number' keys exist?", keys_exist)

"""////////////////// 8 /////////////////////////////"""
sum = 0
for num in range(1, 101):
    sum += num  
print('------------- - 8 - -------------')
print("The sum of numbers from 1 to 100 is:", sum)

"""////////////////// 9 /////////////////////////////"""
def check_even_or_odd(number):
    return number % 2 == 0

print('------------- - 9 - -------------')
num = input('Enter a Number: ')
try:
    num = int (num)
    if ((check_even_or_odd(num))):
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")
except:
    print(f"The number {num} is not a valid number.")

"""////////////////// 10 /////////////////////////////"""
def reverse_string(input_string):
    return input_string[::-1]

print('------------- - 10 - -------------')
string = input("Enter a string: ")

while not string:
    print("Can not reverse Empty!!")
    string = input("Enter a string: ")

reversed_string = reverse_string(string)
print("Original string:", string)
print("Reversed string:", reversed_string)

"""////////////////// 11 /////////////////////////////"""
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()

    return s == s[::-1]

print('------------- - 11 - -------------')
string = input('Enter a string: ')
while not string:
    print("Can not be Empty!!")
    string = input("Enter a string: ")

print("Is the string a palindrome?", is_palindrome(string))

"""////////////////// 12 /////////////////////////////"""

def new_list(lst):
    list = [num ** 2 for num in lst if num % 2 != 0]
    return list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processed_list = new_list(original_list)

print('------------- - 12 - -------------')
print("Original list:", original_list)
print("Processed list:", processed_list)

"""////////////////// 13 /////////////////////////////"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  
    return True  
print('------------- - 13 - -------------')
number = input('Enter a Number: ')
try:
    number = int (number)
    if (is_prime(number)):
        print(f"The number {number} is prime.")
    else:
        print(f"The number {number} is not prime.")
except:
    print(f"The number {number} is not a valid number.")

"""////////////////// 14 /////////////////////////////"""

def factorial(n): 
    if n == 0:
        return 1 
    return n * factorial(n - 1)
print('------------- - 14 - -------------')
number = input('Enter a Number: ')
try:
    number = int (number)
    print(f"The factorial of {number} is {factorial(number)}.")
except:
    print("Please enter a number.")

"""////////////////// 15 /////////////////////////////"""

def operation_list(list):
    result = []
    sum = 0
    for i in list:
        sum += i
    result.append(sum)
    # result.append(sum(list))
    result.append(min(list))
    result.append(max(list))
    
    squared_list = []
    for i in numbers:
        squared_list.append(i ** 2)
    result.append(squared_list)
    
    return result

numbers = [1, 2, 3, 4, 5]
results = operation_list(numbers)
print('------------- - 15 - -------------')
print (results)