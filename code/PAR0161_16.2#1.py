#1
'''
Implement (the choice of programming language is up to you) the Generalized Caesar Cipher
(Shift Cipher). The permissible alphabet is English alphabet without spaces (uppercase only).
Inputs must be entered from standard input (keyboard), outputs will be written to standard
output (console). You must handle any impermissible characters that would appear in the
input. The key will also be entered from the standard input. No GUI is needed yet, it can be a
simple console application.
'''

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Encryption(plain,shift):
    result = ""
    for i in range(len(plain)):
        char = plain[i]
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + shift - 97) % 26 + 97)
            result = result.upper()
    return result

def Decryption(encrypted,shift):
    result = ""
    for c in encrypted:
        if c in chars:
            position = chars.find(c)
            new_position = (position - shift) % 26
            new_character = chars[new_position]
            result += new_character
        else:
            result += c
            
    return result

if __name__ == "__main__": 
    plain = "My name is June"
    shift = 3
    encrypted = Encryption(plain,shift)
    decrypted = Decryption(encrypted,shift)
    print("Plain Text : ",plain)
    print("Shift : ",str(shift))
    print("Encrypted Text: ",encrypted)
    print("Decrypted Text: ",decrypted)
