'''
Implement the General Substitiution Cipher (enryption & decryption), the key is any
permutation of the English alphabet without a space. The permissible alphabet is English
alphabet without spaces (uppercase only). Inputs must be entered from standard input
(keyboard), outputs will be written to standard output (console). You must handle any
impermissible characters that would appear in the input. No GUI is needed yet, it can be a
simple console application
'''

import random
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generateKey():
    shuffle = sorted(chars, key=lambda k: random.random())
    return(dict(zip(chars, shuffle)))

def Encryption(key, plain):
    return(''.join(key[l] for l in plain))

def Decryption(key, cipher):
    flip = {v: k for k, v in key.items()}
    return(''.join(flip[l] for l in cipher))

if __name__ == "__main__":
    plain = 'My name is June!'
    plain = plain.replace(" ","")
    plain = plain.upper()
    p_list = list(plain)
    for i in range(len(p_list)):
        if(p_list[i] not in chars):
            plain = plain.replace(p_list[i],"")
    key = generate_key()
    encrypted = encrypt(key, plain)
    decrypted = decrypt(key, encrypted)
    print('Key: ',key)
    print('Plain Text: ',plain)
    print('Encrypted Text: ',encrypted)
    print('Decrypted Text: ',decrypted)
