print("Playfair Cipher\n1.Encryption\n2.Decryption")

choice = int(input("Enter your Choice (1/2):"))
text = input('Enter your text: ').lower().replace(" ", "")
key = input("Enter the key: ").lower()

def encryption(text, key):
    
    if len(text) % 2:
        text += "x"

    iter_text = iter(text)
    digraph = [next(iter_text) + next(iter_text, 'z') for i in range(len(text)//2)]
    digraph = list(map(lambda x: x[0] + "x" if x[0] == x[1] else x, digraph))

    key_sq = []
    key_sq = [i for i in key if i not in key_sq]

    for i in range(ord('a'), ord('z') + 1):
        char = chr(i) if chr(i) != 'j' else 'i'
        if char not in key_sq:
            key_sq.extend(char)

    key_matrix = [key_sq[i:i+5] for i in range(0, len(key_sq), 5)]

    cipher = []
    for di in range(len(digraph)):
        for i in range(5):
            for j in range(5):
                if key_matrix[i][j] == digraph[di][0]:
                    x1, y1 = i, j
                if key_matrix[i][j] == digraph[di][1]:
                    x2, y2 = i, j

        if x1 == x2:
            c1, c2 = key_matrix[x1][(y1 + 1) % 5], key_matrix[x2][(y2 + 1) % 5]
        elif y1 == y2:
            c1, c2 = key_matrix[(x1 + 1) % 5][y1], key_matrix[(x2 + 1) % 5][y2]
        else:
            c1, c2 = key_matrix[x1][y2], key_matrix[x2][y1]

        ci = c1 + c2
        cipher.append(ci)
    return ''.join(cipher)

def decryption(text, key):

    iter_text = iter(text)
    digraph = [next(iter_text) + next(iter_text) for i in range(len(text)//2)]

    key_sq = []
    key_sq = [i for i in key if i not in key_sq]

    for i in range(ord('a'), ord('z') + 1):
        char = chr(i) if chr(i) != 'j' else 'i'
        if char not in key_sq:
            key_sq.extend(char)

    key_matrix = [key_sq[i:i+5] for i in range(0, len(key_sq), 5)]

    plain = []
    for di in range(len(digraph)):
        for i in range(5):
            for j in range(5):
                if key_matrix[i][j] == digraph[di][0]:
                    x1, y1 = i, j
                if key_matrix[i][j] == digraph[di][1]:
                    x2, y2 = i, j

        if x1 == x2:
            c1, c2 = key_matrix[x1][(y1 - 1) % 5], key_matrix[x2][(y2 - 1) % 5]
        elif y1 == y2:
            c1, c2 = key_matrix[(x1 - 1) % 5][y1], key_matrix[(x2 - 1) % 5][y2]
        else:
            c1, c2 = key_matrix[x1][y2], key_matrix[x2][y1]

        ci = c1 + c2
        plain.append(ci)
    return ''.join(plain).strip('x')

print(encryption(text, key) if choice == 1 else decryption(text, key))