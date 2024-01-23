print("Vigenere Cipher\n1.Encryption\n2.Decryption")

choice = int(input("Enter your Choice (1/2):"))
text = input('Enter your text: ').replace(" ", "").upper()
key = input("Enter the key: ").upper()

def convert_key(text, key):
    key = key * ((len(text) // len(key)) + 1)
    return key[:len(text)]


def operation(choice, text, key):
    cipher = []
    key = convert_key(text, key)

    for i in range(len(text)):
        text_val = ord(text[i])

        if choice == 2:
            key_val = 26 - ord(key[i])
        else:
            key_val = ord(key[i])

        char = (text_val + key_val) % 26 + 65
        cipher.append(chr(char))
    
    return "".join(cipher)

print(operation(choice, text, key))

