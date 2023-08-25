alphabet_to_numeric={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h': 7, 'i': 8, 'j': 9,
                       'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
                       't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

numeric_to_alphabet={v: k for k, v in alphabet_to_numeric.items()}

s = "abhishek"
key = 20010516

list3 = []  # List to store encrypted characters
list4 = []  # List to store decrypted characters

for i in s:
    numeric_value = alphabet_to_numeric[i]
    encrypted_numeric_value = (numeric_value + key) % 26
    encrypted_char = numeric_to_alphabet[encrypted_numeric_value]
    list3.append(encrypted_char)

encrypted_msg = "".join(list3)

for i in encrypted_msg:
    numeric_value = alphabet_to_numeric[i]
    decrypted_numeric_value = (numeric_value - key) % 26
    decrypted_char = numeric_to_alphabet[decrypted_numeric_value]
    list4.append(decrypted_char)

decrypted_msg = "".join(list4)

print("Original Message:", s)
print("Encrypted Message:", encrypted_msg)
print("Decrypted Message:", decrypted_msg)