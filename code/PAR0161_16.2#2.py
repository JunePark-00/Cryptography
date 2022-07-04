#2
'''
Implement the brute force attack against the Generalized Caesar Cipher (Shift Cipher). 
Break the given ciphertext. What is the obtained plaintext and the key?
'''

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def Decryption(encrypted,key):
    result = ""
    for c in encrypted:
        if c in chars:
            index1 = chars.find(c)
            index2 = (index1 - key) % 26
            sub_char = chars[index2]
            result += sub_char
        else:
            result += c
            
    return result

if __name__ == "__main__":
    encrypted = input("Encrypted Text: ")
    while True:
        key = int(input("Key: "))
        print("Decrypted Text: ",Decryption(encrypted,key))
        
        flag = input("If it is right, enter the 1: ")
        if(flag=='1'):
            break
            
            
'''
Key
>> 4
Result
>> CITIESHAVEOFTENBOUNCEDBACKFROMCRISESFROMPANDEMICSANDEARTHQUAKESTOFLOODSANDF IRESTHEWORLDSURBANPOWERHOUSESHAVEEMERGEDSTRONGERWHENFACEDWITHADVERSITYAFTERTHEGRE ATFIREOFLONDONDESTROYEDMOSTOFTHECITYARAFTOFFIRESAFETYREGULATIONSWEREUSHEREDINBU ILDERSSWAPPEDTIMBERFORBRICKORSTONEWALLSWEREMADETHICKERSTREETSBECAMEWIDERWHEN CHOLERATORETHROUGHAMERICANEWYORKANDOTHERCITIESINTRODUCEDSEWAGESYSTEMSANDPUBL ICPARKSTODAYSURBANAREASFACEACHALLENGEOFADIFFERENTSORTWITHTHEMASSRETURNTOOFFICE WORKSTILLUNCERTAINTHEPANDEMICHASSHARPENEDDEBATEABOUTWHATTHEFUTUREHOLDSFORTHEIRC OMMERCIALHUBSKEYBUSINESSDISTRICTSLIKEMANHATTANTHECITYOFLONDONTOKYOSMARU NOUCHIANDLADÉFENSEINPARISHAVEBORNETHEBRUNTOFTHEOFFICEEXODUS
'''
    
