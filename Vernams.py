print("Vernam's Cipher\n1.Encryption\n2.Decryption")

choice = int(input("Enter your Choice (1/2):"))
text = input('Enter your text: ').lower().replace(" ", "")
key = input("Enter key: ").lower()

while len(key) != len(text):
    key = input("Enter key with same length of text: ").lower()

def operation(operation, text, key):
    flag = 1 if operation == 1 else -1
    cipher = []
    for i in range(len(key)):
        cipher.append((ord(text[i]) - ord('a') + flag * (ord(key[i]) - ord('a'))) % 26)
    return "".join([chr(i + ord('a')) for i in cipher])

print(operation(choice, text, key))