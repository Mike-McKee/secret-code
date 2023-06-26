# Reminder, keep letters lowercase so turn uppercase ones into lower case in function
import numpy as np

# Dictionary for changing letters in secret message into numbers
num_lib = {
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

# Dictionary for encoding numbers back to letters
encode_lib = {
    1: 'f',
    4: 'd',
    27: 'p',
    100: 'x',
    1331: 'w',
    144: 'z',
    2197: 'g',
    400: 'l',
    9261: 't',
    484: 'm',
    12167: 'e',
    900: 'c',
    29791: 'b',
    1024: 'q',
    35937: 'y',
    10000: 'u',
    1030301: 'n',
    10404: 'i',
    1092727: 's',
    12100: 'a',
    1367631: 'o',
    12544: 'z',
    1442897: 'r',
    14400: 'h',
    1771561: 'j',
    14884: 'k',
    1860867: ' '
}

def change_num(num):    
    sb_four = int(np.base_repr(num, base=4))    #changes numbers from base 10 to base 4
    if sb_four % 2 == 1:
        new_num = sb_four ** 3  #Cubes odd numbers
    else:
        new_num = sb_four ** 2  #Squares even numbers
    return new_num

# the encryption function to create secret messages
def encrypt(str):
    encryption = []
    for i in str:
        encryption.append(encode_lib[change_num(num_lib[i])])
    result = ''.join(k for k in encryption)
    return result        

secret_message = input("Enter secret message here: ")

print(encrypt(secret_message))