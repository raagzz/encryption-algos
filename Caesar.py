print("Caesar Cipher\n1.Encryption\n2.Decryption")

choice = int(input("Enter your Choice (1/2):"))
text = input('Enter your text: ')
shift = int(input("Enter the no. of shift (1 - 25): "))

def operation(choice, text, shift):
    cipher = ""
    shift = (26 - shift) if choice == 2 else shift

    for i in range(len(text)):
        char = text[i]
        offset = 65 if char.isupper() else 97
        cipher += chr((ord(char) + shift - offset) % 26 + offset)

    return cipher

print(operation(choice, text, shift))
