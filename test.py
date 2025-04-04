class TabularCipher:
    def __init__(self, key):
        self.key = key
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.table = self.generate_table()

    def generate_table(self):

        key_unique = "".join(sorted(set(self.key), key=self.key.index))  
        key_alphabet = key_unique + "".join(c for c in self.alphabet if c not in key_unique)  
        table = [key_alphabet[i*5:(i+1)*5] for i in range(5)] 
        return table

    def encrypt(self, plaintext):

        plaintext = plaintext.upper().replace(" ", "")  
        ciphertext = []
        for char in plaintext:
            for row in range(5):
                if char in self.table[row]:
                    col = self.table[row].index(char)
                    ciphertext.append(self.table[(row + 1) % 5][col])  
                    break
        return ''.join(ciphertext)

    def decrypt(self, ciphertext):

        ciphertext = ciphertext.upper().replace(" ", "") 
        plaintext = []
        for char in ciphertext:
            for row in range(5):
                if char in self.table[row]:
                    col = self.table[row].index(char)
                    plaintext.append(self.table[(row - 1) % 5][col])  
                    break
        return ''.join(plaintext)

    def print_table(self):
        for row in self.table:
            print(" ".join(row))



cipher = TabularCipher("VIOLETA")
cipher.print_table()
plaintext = "HELLO"
ciphertext = cipher.encrypt(plaintext)
print(f"Encrypted: {ciphertext}")
decrypted = cipher.decrypt(ciphertext)
print(f"Decrypted: {decrypted}")
