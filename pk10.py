
# requires PyWin32 extensions

import win32com.client
import random
import math
from datetime import date
import string_utils
import numpy as np



qng = win32com.client.Dispatch("QWQNG.QNG") 
random32_from_device: int = abs(qng.RandInt32)




def get_numbers():
    array_numbers = [1,2,3,4,5,6,7,8,9,10]
    selected_number =[ 4]
    draw_number: int = []
   

    random.shuffle(array_numbers)
    draw_number.append(array_numbers)
    draw_number.append(selected_number)
    draw_number
   

    print(draw_number)
    



get_numbers()