import random
import string
import time

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list (chars)
key = chars.copy ()
random.shuffle (key)

#ENCRYPTION:
plain_text= input ("Orignal Message: ")
cipher_text = ""

for letters in plain_text:
    index = chars.index (letters)
    cipher_text += key[index]

time.sleep (1)
print (f"Encrypted Message: {cipher_text}")

print ("***********************************")
time.sleep (2)
# DECRYPTION:
cipher_text = input("Encrypted Message: ")
plain_text = ""

for letters in cipher_text:
    index = key.index(letters)
    plain_text += chars[index]

time.sleep (1)
print(f"Orignal Message   : {plain_text}")