#Created by Zoltan Szeman

from caesar_cipher import CaesarCipher

class Decipher(CaesarCipher):
    '''A class to decipher monoalphabetic ciphers'''

    def __init__(self, plaintext = "", ciphertext = "", char_set = ""):
        '''CaesarCipher is the parent'''
        CaesarCipher.__init__(self, plaintext, ciphertext, char_set)
  
    def brute_force(self):
        '''Brute force codebreaking requiring user input'''
        txt_og = ""
        start = 100
        end = 200
        i = start
        key = 1
        while i != end:
            txt_og += self.ciphertext[i]
            i += 1
        while True:
            txt = ""
            for letter in txt_og:
              try:
                index = self.char_set.index(letter.lower())
              except:
                pass
              if letter == letter.lower() and letter in self.char_set:
                try:
                  letter = self.char_set[index+key]
                except:
                  letter = self.char_set[index+key-26]
              elif letter in self.char_set.upper():
                try:
                  letter = self.char_set.upper()[index+key]
                except:
                  letter = self.char_set.upper()[index+key-26]
              txt += letter
            user_input = input(f"\n{txt}\nIs the above a correct english "
                                "text?[y or n]\n ")
            if user_input == "y":
                break
            key += 1
        return key
    
    def freq_analysis(self):
        '''Frequency analysis codebreaking'''
        ciphertext_list = [char for char in self.ciphertext]
        letter_count = {}
        letter_freq = {}
        for letter in self.char_set:
            i = 0
            count = 0
            while True:
                try:
                    if letter == ciphertext_list[i].lower():
                        ciphertext_list.remove(ciphertext_list[i])
                        count += 1
                    else:
                        i += 1
                except IndexError:
                    break
            letter_count[letter] = count
        inverse = [(value, key) for key, value in letter_count.items()]
        e_coded = max(inverse)[1]
        '''"e" is the most common letter in an english language text'''
        key = self.char_set.index('e') - self.char_set.index(e_coded)
        if key < 0:
            key += 26
        return key
