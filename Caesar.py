print("Caesar Cipher\n1.Encryption\n2.Decryption")

choice = int(input("Enter your Choice (1/2):"))
text = input('Enter your text: ')
shift = int(input("Enter the no. of shift (1 - 25): "))

class CaesarCipher:

    def __init__(self, choice, text, shift):
        self.choice = choice
        self.text = text
        self.shift = shift

    def operation(self):
        cipher = ""

        if self.choice == 2:
            self.shift = 26 - self.shift

        for i in range(len(text)):
            char = text[i]

            if(char.isupper()):
                cipher += chr((ord(char) + self.shift - 65) % 26 + 65)

            else:
                cipher += chr((ord(char) + self.shift - 97) % 26 + 97)
    
        return cipher

caesar = CaesarCipher(choice, text, shift)
print(caesar.operation())