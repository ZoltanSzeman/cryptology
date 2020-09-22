#Created by Zoltan Szeman
#This is how Caeser used to cipher his private letters

from random import randint
from caesar_cipher import CaesarCipher
from decipher import Decipher

'''Ciphering'''
file = open("text-file\cryptonomicon_plaintext.txt")
msg = file.read()
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = randint(1,25) #the key remains unknown
cipher = CaesarCipher(plaintext = msg, char_set = alphabet)
coded_msg = cipher.encrypt(key)

'''Deciphering'''
file_coded = open("text-file\cryptonomicon_ciphertext.txt","w+")
file_coded.write(coded_msg)
file_coded.seek(0)
msg_to_break = file_coded.read()
codebreak = Decipher(plaintext = "", ciphertext = msg_to_break, char_set = alphabet)

method = "f" #"f" - frequancy analysis or "b" - brute force codebreaking
if method == "f":    
    codebreak_key = codebreak.freq_analysis()
elif method == "b":
    codebreak_key = codebreak.brute_force()
    
decoded_msg = codebreak.decrypt(codebreak_key)
file_decoded = open("text-file\cryptonomicon_deciphered.txt","w+")
file_decoded.write(decoded_msg)
    
    

'''Close all files'''
file.close()
file_coded.close()
file_decoded.close()

print("Your key for the code is:",codebreak_key)
