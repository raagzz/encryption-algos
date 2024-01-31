print("Columnar Transposition Cipher\n1.Encryption\n2.Decryption")

choice = int(input("Enter your Choice (1/2):"))
text = input('Enter your text: ')
key = input("Enter the key: ")

def encryption(text, key):
    keylist = list(key)
    dic = {item: [] for item in keylist}

    pad = len(text) % len(key)
    if pad:
        padded_text = text + ((len(key) - pad % 10)) * " "

    for i in range(len(text)):
        for j in range(len(key)):
            if i % len(key) == j:
                dic[keylist[j]].append(padded_text[i])

    sorted_dic = dict(sorted(dic.items()))
    return "".join(sum(sorted_dic.values(), []))

def decryption(text, key):
    keylist = sorted(list(key))
    dic = {item: [] for item in keylist}

    iter_text = iter(text)
    for i in dic:
        dic[i].extend([next(iter_text) for i in range(len(key))])

    sorted_dic = {k: dic[k] for k in key}
    table = sorted_dic.values()

    decrypted = []
    for i in range(len(key)):
        for row in table:
            decrypted.extend(row[i])

    return "".join(decrypted).strip()


print(encryption(text, key) if choice == 1 else decryption(text, key))