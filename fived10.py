# requires PyWin32 extensions

import win32com.client
import random
import math
from datetime import date
import string_utils
import numpy as np



qng = win32com.client.Dispatch("QWQNG.QNG") 
random32_from_device: int = abs(qng.RandInt32)



my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_number = str(random.choice(my_list))

numbers: int
numbers = abs(random32_from_device)
fixed_number = int(new_number)

def get_draw_number(original_number: int, fixed_number: int):

    S1 = str(original_number)
    S2 = str(fixed_number)

    if(len(S1) < 10 ):

        S3 = S1 + S2

        retsults = int(S3)

        return retsults
    else:
        return random32_from_device


total_nums = []
draw_numbers = []
one_array_draw_number = []
all_takes = []
output_numbers = []
temp_numbers = []
winning_number: str
item: int
new_item: int
counter: int = 3 # items in Array
takes: int =  3 # Array
isOne_to_Six = True




# getting numbers from device
item = get_draw_number(random32_from_device, fixed_number)



def get_numbers_from_device(isOne_to_Six):
    
    if(isOne_to_Six == True):
        one_to_six(item)


    else:

        for i in range(counter):
            total_nums.append(string_utils.shuffle(str(item)))

        for take in range(takes):
            all_takes.append(total_nums)

        for sublist  in all_takes:
            for sub in sublist:
                temp_numbers.append(string_utils.shuffle(sub))
                # print(sub)
            

        chunks = np.array_split(temp_numbers, takes)
        for chunk in chunks:
            my_list = list(chunk)
            draw_num = []
            for i in my_list:
                draw_num.append(random.choice(i))

            my_list.append(draw_num)
            output_numbers.append(my_list)
        
        
        print(output_numbers)
        # print(total_nums)
        # print(one_array_draw_number)


#End of function


def one_to_six(item):

    num_list: int =  123456
    all_takes = []
    takes = 1
    counter = 3
    numbers = int(num_list)
    total_nums = []
    output_numbers = []
    temp_numbers = []
   
    
    for i in range(counter):
        total_nums.append(string_utils.shuffle(str(numbers)))
    
    for take in range(takes):
        all_takes.append(total_nums)
        

    for sublist  in all_takes:
            for sub in sublist:
                temp_numbers.append(string_utils.shuffle(sub))
                
    
    chunks = np.array_split(temp_numbers, takes)
    for chunk in chunks:
            my_list = list(chunk)
            draw_num = []
            for i in my_list:
                draw_num.append(random.choice(i))

            my_list.append(draw_num)
            output_numbers.append(my_list)



    # print(total_nums)
    # print(all_takes)
    # print(temp_numbers)
    print(output_numbers)
    



# Call function to draw
get_numbers_from_device(isOne_to_Six)



