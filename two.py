
# requires PyWin32 extensions

import win32com.client
import random
import math
from datetime import date
import string_utils


qng = win32com.client.Dispatch("QWQNG.QNG") 
#rand32 = qng.RandInt32
# randUniform = qng.RandUniform
# randNormal = qng.RandNormal
# randBytes = qng.RandBytes(7)
def get_random32():
    randone32 = qng.RandInt32
    return randone32



my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fixed_number = str(random.choice(my_list))

numbers: int
numbers = abs(get_random32())
new_number = random.choice(my_list)

def concate(original_nums, fixed_nums):
    S1 = str(original_nums)
    S2 = str(fixed_nums)
    

    if(len(S1) < 10 ):

        S3 = S1 + S2

        retsults = int(S3)

        return retsults
    else:
        return numbers


first_number: int
second_number: int
shuffle_string: int
first_number_shuffle: str
# todays_date: date
# todays_date = date.today()

# month: str = (todays_date.month)
# day: str = (todays_date.day)
# new_string: str = month + date

first_number = concate(numbers,new_number)
second_number = concate(numbers,new_number)
first_number_shuffle = str(first_number)

def get_two_numbers(first_number_shuffle: str):
    

    shuffle_string = string_utils.shuffle(first_number_shuffle)
    print(shuffle_string + "  " + "Length   "+ str(len(shuffle_string)))
    print(first_number_shuffle + "  " + "Length   " + str(len(first_number_shuffle)))


get_two_numbers(first_number_shuffle)
