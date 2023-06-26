import numpy as np

decode_lib = {
    'f': 1,
    'd': 4,
    'p': 27,
    'x': 100,
    'w': 1331,
    'z': 144,
    'g': 2197,
    'l': 400,
    't': 9261,
    'm': 484,
    'e': 12167,
    'c': 900,
    'b': 29791,
    'q': 1024,
    'y': 35937,
    'u': 10000,
    'n': 1030301,
    'i': 10404,
    's': 1092727,
    'a': 12100,
    'o': 1367631,
    'z': 12544,
    'r': 1442897,
    'h': 14400,
    'j': 1771561,
    'k': 14884, 
    ' ': 1860867
}

num_dic = {
    26: 'a',
    1: 'b',
    25:'c',
    2: 'd',
    24: 'e',
    3:'f',
    23: 'g',
    4: 'h',
    22: 'i',
    5: 'j',
    21: 'k',
    6: 'l',
    20: 'm',
    7: 'n',
    19: 'o',
    8: 'p',
    18: 'q',
    9: 'r',
    17: 's',
    10: 't',
    16: 'u',
    11: 'v',
    15: 'w',
    12: 'x',
    14: 'y',
    13: 'z',
    27: ' '
}

#Square roots or cube roots numbers based on if they're even or odd
#Then it converts the number from base 4 to base 10
def switch_num(number):
    if number % 2 == 1:
        decrypt_num = int(str(int(np.cbrt(number))), 4)
    else:
        decrypt_num = int(str(int(np.sqrt(number))), 4)
    return decrypt_num

#Uses above dictionaries and switch_num function to decode strings
def decrypt(str):
    decryption = []
    for i in str:
        decryption.append(num_dic[switch_num(decode_lib[i])])
    final_message = ''.join(k for k in decryption)
    return final_message

decoded_message = input("Enter what you want decoded: ")

print(decrypt(decoded_message))
