import json
from math import sqrt

numbers = [4, 9, 16, 25, 36]

sqrt_of_numbers = list(map(lambda x: sqrt(x), numbers))
# [(lambda x: sqrt(x))(x) for x in numbers]

result_dict = dict(map(lambda i,j : (i,j) , numbers,sqrt_of_numbers))
# result_dict = dict(zip(numbers, sqrt_of_numbers))

with open('file.json', 'w') as json_file:
    json.dump(result_dict, json_file, indent=4)

json_file.close()
print("written successfully!")
