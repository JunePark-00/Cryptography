'''
#2
Implement the Vigenere cipher (enryption & decryption). Work with a permissible alphabet
containing only the English alphabet characters without a space. The plaintext P = TO BE OR
NOT TO BE THAT IS THE QUESTION (omit spaces befor encryption), the key is K= DOG. What
is the ciphertext?
'''

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generateKey(plain, key):
    key = list(key)
    if(len(plain) == len(key)):
        return(key)
    else:
        for i in range(len(plain) - len(key)):
            key.append(key[i % len(key)])
    return("".join(key))


def Encryption(plain, key):
    cipher = []
    for i in range(len(plain)):
        x = (ord(plain[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher.append(chr(x))
    return("".join(cipher))


def Decryption(cipher, key):
    plain = []
    for i in range(len(cipher)):
        x = (ord(cipher[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        plain.append(chr(x))
    return("".join(plain))

if __name__ == "__main__":
    plain = "TO BE OR NOT TO BE THAT IS THE QUESTION!"
    plain = plain.replace(" ","")
    keyword = "DOG"
    p_list = list(plain)
    for i in range(len(p_list)):
        if(p_list[i] not in chars):
            plain = plain.replace(p_list[i],"")
    key = generateKey(plain, keyword)
    cipher = Encryption(plain,key)
    print("Plain Text : ",plain)
    print("Encrypted Text :", cipher)
    print("Decrypted Text :",Decryption(cipher, key))
