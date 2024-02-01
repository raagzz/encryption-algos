print("ROT13 Cipher\n1.Encryption\n2.Decryption")

choice = int(input("Enter your Choice (1/2):"))
text = input('Enter your text: ')

def operation(choice, text):
    cipher = ""
    shift = 13

    for i in range(len(text)):
        char = text[i]
        offset = 65 if char.isupper() else 97
        cipher += chr((ord(char) + shift - offset) % 26 + offset)

    return cipher

print(operation(choice, text))