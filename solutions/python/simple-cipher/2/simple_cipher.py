class Cipher:


    def __init__(self, key = None):
        if key is None:
            import string
            import random
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))  

        else:
            self.key = key
        
        self.alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



    def encode(self, text):
        self.text = text
        self.ciphertext = ''

        idx = 0
        for i in self.text:
            pos1 = self.alfabeto.index(i)
            if idx+1 > len(self.key):
                idx = 0
                pos2 = self.alfabeto.index(self.key[idx])
                idx += 1
            else:
                pos2 = self.alfabeto.index(self.key[idx])
                idx += 1
            pos_final = pos1 + pos2
            if pos_final >= len(self.alfabeto):
                pos_final = pos_final - 26
            self.ciphertext += self.alfabeto[pos_final]
 

        return self.ciphertext

    def decode(self, text):
        self.ciphertext = text
        self.plaintext = ''
   
        idx = 0
        for i in self.ciphertext:
            pos1 = self.alfabeto.index(i)
            if idx >= len(self.key):
                idx = 0
                pos2 = self.alfabeto.index(self.key[idx])
                idx += 1
            else:
                pos2 = self.alfabeto.index(self.key[idx])
                idx += 1

            pos_final = pos1 - pos2

            if pos_final < 0: 
                pos_final = pos_final + 26

            self.plaintext += self.alfabeto[pos_final]

        return self.plaintext