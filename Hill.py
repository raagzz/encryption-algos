import numpy as np

print("Hill Cipher\n1.Encryption\n2.Decryption")

choice = int(input("Enter your Choice (1/2):"))
text = input('Enter your text: ').lower().replace(" ", "")
key = input("Enter the key matrix separated by space: ").split()
key = [eval(i) for i in key]

dim = int(np.sqrt(len(key)))
key_matrix = np.array(key).reshape(dim, dim)

def encryption(text, key):
    if len(text) % dim:
        pad = dim - (len(text) % dim)
        text += 'a' * pad
    text_val = [ord(char) - ord('a') for char in text]

    cipher = ""
    for i in range(0, len(text), dim):
        row = np.array(text_val[i: i + dim])
        cipher_row = np.dot(key, row) % 26
        cipher += "".join(chr(val + ord('a')) for val in cipher_row)

    return cipher[:-pad]


def decryption(text, key):
    a = np.linalg.inv(key)
    det = np.linalg.det(key)

    adj = [int(i * det) for i in a.flatten()]
    inverse = np.array([i * pow(int(det), -1, 26) for i in adj]).reshape(dim, dim) % 26

    return encryption(text, inverse)

print(encryption(text, key_matrix) if choice == 1 else decryption(text, key_matrix))