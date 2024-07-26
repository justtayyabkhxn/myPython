import random
import string

chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)

plain_text=input("Enter your text: ")
cipher_text=""
for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]

print(f"Plain text i s: {plain_text}")
print(f"Encrypted text is: {cipher_text}")

cipher_text=input("Enter cipher text: ")
plain_text=""
for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]

print(f"Encrypted text is: {cipher_text}")
print(f"Plain text is: {plain_text}")