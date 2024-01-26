import tkinter as tk

def encode(plaintext,cipher):
    result = mono_encode(plaintext,cipher)
    result = ceaser(result,4)
    result = mono_encode(result,cipher)
    return result

def decode(plaintext,cipher):
    result = mono_decode(plaintext,cipher)
    result = ceaser(result,-4)
    result = mono_decode(result,cipher)
    return result

def mono_encode(plaintext, cipher):
    return "".join(cipher.get(character.upper()) or character
                   for character in plaintext)

def mono_decode(ciphertext, encoding_cipher):
    decode_cipher = {value: key for key, value in encoding_cipher.items()} #inverse the cipher dictionary
    return mono_encode(ciphertext, decode_cipher)

def ceaser(plaintext,key):
    result = ""
 
    # traverse text
    for i in range(len(plaintext)):
        character = plaintext[i]

        if(key>0):
            key = key+1
        
        if(key<0):
            key = key-1

        if(character == " "):
            result += " "
            continue
 
        # Encrypt uppercase characters
        if (character.isupper()):
            result += chr((ord(character) + key-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(character) + key - 97) % 26 + 97)
 
    return result

def main():
    cipher = {"A": "O", "B": "D", "C": "L", "D": "T", "E": "I",
              "F": "N", "G": "G", "H": "J", "I": "E", "J": "V",
              "K": "F", "L": "C", "M": "R", "N": "S", "O": "U",
              "P": "Q", "Q": "H", "R": "Y", "S": "B", "T": "K",
              "U": "A", "V": "W", "W": "P", "X": "Z", "Y": "M",
              "Z": "X"}

    def encryption_button_clicked():
        ciphertextField.delete(0, tk.END)
        ciphertextField.insert(0,encode(plaintextField.get(),cipher).lower())

    def decryption_button_clicked():
        plaintextField.delete(0, tk.END)
        plaintextField.insert(0,decode(ciphertextField.get(),cipher).lower())

    window = tk.Tk()
    window.title("MK")

    # Create the plaintext field
    plaintextField = tk.Entry(window)
    plaintextField.pack()

    # Create the ciphertext field
    ciphertextField = tk.Entry(window)
    ciphertextField.pack()

    # Create the encryption button
    encryptionButton = tk.Button(window, text="Encrypt", command=encryption_button_clicked)
    encryptionButton.pack()

    # Create the decryption button
    decryptionButton = tk.Button(window, text="Decrypt", command=decryption_button_clicked)
    decryptionButton.pack()

    # Start the main event loop
    window.mainloop()

if __name__ == '__main__':
    main()