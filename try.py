import random


# x = [ [1,2,3], [4,5,6], [7,8,9] ]

# random.shuffle(x)
# for i in x:
#     random.shuffle(i)
# print(x)
# Y =  [[4, 6, 2, 5, 3, 1], [4, 6, 2, 5, 3, 1], [4, 6, 2, 5, 3, 1]]

# # random.shuffle(Y)
# for i in Y:
#     random.shuffle(i)
# print(Y)

import random

number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
# Original list
print(number_list)
# Output [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# List after first shuffle
random.shuffle(number_list)
print(number_list)
# Output [42, 28, 