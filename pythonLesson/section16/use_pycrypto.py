import string
import random
from Crypto.Cipher import AES

key = "".join(random.choice(string.ascii_letters) for _ in range(AES.block_size))

iv = "".join(random.choice(string.ascii_letters) for _ in range(AES.block_size))

# plaintext = "I am a cat. My name is no yet."
# cipher = AES.new(key, AES.MODE_CBC, iv)

# padding_length = AES.block_size - len(plaintext) % AES.block_size
# plaintext += chr(padding_length) * padding_length
# cipher_text = cipher.encrypt(plaintext)
# print(cipher_text)


# cipher2 = AES.new(key, AES.MODE_CBC, iv)
# decrypted_text = cipher2.decrypt(cipher_text)
# print(decrypted_text[: -decrypted_text[-1]])


with open("plaintext.txt", "r") as f, open("enc.txt)", "wb") as e:
    plaintext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += chr(padding_length) * padding_length
    cipher_text = cipher.encrypt(plaintext)
    e.write(cipher_text)

with open("enc.txt", "rb") as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher2.decrypt(f.read())
    print(decrypted_text[: -decrypted_text[-1]].decode("utf-8"))

