# Reminder, keep letters lowercase so turn uppercase ones into lower case in function
import numpy as np

# Reminder, keep letters lowercase so turn uppercase ones into lower case in function
encrypt = {
    'a': 26,
    'b': 1,
    'c': 25,
    'd': 2,
    'e': 24,
    'f': 3,
    'g': 23,
    'h': 4,
    'i': 22,
    'j': 5,
    'k': 21,
    'l': 6,
    'm': 20,
    'n': 7,
    'o': 19,
    'p': 8,
    'q': 18,
    'r': 9,
    's': 17,
    't': 10,
    'u': 16,
    'v': 11,
    'w': 15,
    'x': 12,
    'y': 14,
    'z': 13,
    ' ': 27
}

#here's the first test to change string to int using the dictionary
test_string =  'its a secret code'

string_to_num = []

for i in test_string:
    string_to_num.append(encrypt[i])

#Change values in string_to_num from base 10 to base 4
base_four = []

for j in string_to_num:
   switch_b_four = int(np.base_repr(j, base=4))
   base_four.append(switch_b_four)

#Here we raise to power of 2 if even and power of 3 if odd
encryption = []

for m in base_four:
    if m % 2 == 1:
        new_pow = m ** 3
    else:
        new_pow = m ** 2
    
    encryption.append(new_pow)

#print results
print(encryption)


