print("RailFence Cipher\n1.Encryption\n2.Decryption")

choice = int(input("Enter your Choice (1/2):"))
text = input('Enter your text: ')
num_rails = int(input("Enter the no. of rails: "))

def encryption(text, num_rails):
    fence = [[None] * len(text) for row in range(num_rails)]
    rails = list(range(num_rails - 1)) + list(range(num_rails - 1, 0, -1))

    for n, char in enumerate(text):
        fence[rails[n % len(rails)]][n] = char

    return  [char for rail in fence for char in rail if char is not None]

def decryption(text, num_rails):
    rng = list(range(len(text)))
    pos = encryption(rng, num_rails)
    return "".join(text[pos.index(i)] for i in rng)

print("".join(encryption(text, num_rails)) if choice == 1 else decryption(text, num_rails))