# requires PyWin32 extensions

import win32com.client
import random
import math
from datetime import date
import string_utils



qng = win32com.client.Dispatch("QWQNG.QNG") 
random32_from_device: int = abs(qng.RandInt32)

# arr1 = [0,1,2,3,4,5,6,7,8,9]
# arr1 = [0,1,2,3,4,5,6,7,8,9]
# arr1 = [0,1,2,3,4,5,6,7,8,9]
# arr1 = [0,1,2,3,4,5,6,7,8,9]
# arr1 = [0,1,2,3,4,5,6,7,8,9]

# total = 7, 5, 8, 9, 6

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_number = str(random.choice(my_list))

numbers: int
numbers = abs(random32_from_device)
fixed_number = int(new_number)

def get_draw_number(original_number: int, fixed_number: int):

    S1 = str(original_number)
    S2 = str(fixed_number)

    # print(S1 + "   Lenght  " + str(len(S1)))
    # print(S2 + "   Lenght  " + str(len(S2)))
    

    if(len(S1) < 10 ):

        S3 = S1 + S2

        retsults = int(S3)

        return retsults
    else:
        return random32_from_device


total_nums = []
draw_numbers = []
winning_number: str
results: int

results1 = get_draw_number(random32_from_device, fixed_number)
results2 = get_draw_number(random32_from_device, fixed_number)
results3 = get_draw_number(random32_from_device, fixed_number)
results4 = get_draw_number(random32_from_device, fixed_number)
results5 = get_draw_number(random32_from_device, fixed_number)

list_one =   string_utils.shuffle(str(results1))
list_two =   string_utils.shuffle(str(results2))
list_three = string_utils.shuffle(str(results3))
list_four =  string_utils.shuffle(str(results4))
list_five =  string_utils.shuffle(str(results5))

total_nums.append(list_one)
total_nums.append(list_two)
total_nums.append(list_three)
total_nums.append(list_four)
total_nums.append(list_five)  

draw_numbers.append(random.choice(list_one))
draw_numbers.append(random.choice(list_two))
draw_numbers.append(random.choice(list_three))
draw_numbers.append(random.choice(list_four))
draw_numbers.append(random.choice(list_five))



print(total_nums)
print("Draw Numbers      " + str(draw_numbers))

