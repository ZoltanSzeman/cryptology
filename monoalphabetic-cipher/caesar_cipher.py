#Created by Zoltan Szeman

class CaesarCipher:
    '''A class containing the Caesar's cipher encode and decode logic'''

    def __init__(self, plaintext = "", ciphertext = "", char_set = ""):
        '''Instantiate the attributes with default values where necessary'''
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.char_set = char_set

    def encrypt(self, key):
        '''Encrypt the plaintext'''
        encrypt_txt = ""
        for letter in self.plaintext:
          try:
            index = self.char_set.index(letter.lower())
          except ValueError:
            pass
          if letter == letter.lower() and letter in self.char_set:
            letter = self.char_set[index-key]
          elif letter in self.char_set.upper():
            letter = self.char_set.upper()[index-key]
          encrypt_txt += letter
        return encrypt_txt
    
    def decrypt(self,key):
        '''Decrypt the ciphertext'''
        decrypt_txt = ""
        for letter in self.ciphertext:
          try:
            index = self.char_set.index(letter.lower())
          except ValueError:
            pass
          if letter == letter.lower() and letter in self.char_set:
            try:
              letter = self.char_set[index+key]
            except IndexError:
              letter = self.char_set[index+key-26]
          elif letter in self.char_set.upper():
            try:
              letter = self.char_set.upper()[index+key]
            except IndexError:
              letter = self.char_set.upper()[index+key-26]
          decrypt_txt += letter
        return decrypt_txt
