
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
    eleven_five = ['01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11']
    temp_numbers = []
    draw_numbers = []

    for i in range(3):
        temp_numbers.append(eleven_five)

    for i in temp_numbers:
        draw_numbers.append(random.choice(i))


    print(temp_numbers)
    print(draw_numbers)
    



get_numbers()