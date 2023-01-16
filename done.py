
# requires PyWin32 extensions

import win32com.client
import random
import math


qng = win32com.client.Dispatch("QWQNG.QNG") 

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



print("Random32        " + str(concate(numbers,new_number)))

# print("RandUniform "+ str(randUniform))
# print("randNormaL "+ str(randNormal))
# print("randBytes"+ str(randBytes))

#  my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     output_string = ''
#     fixed_number = str(random.choice(my_list))
