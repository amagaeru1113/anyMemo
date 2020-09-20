from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)


# 暗号化
f = Fernet(key)
plaintext = bytes("My name is Mike!", "utf-8")
token = f.encrypt(plaintext)
print(token)

# 複号化
r = f.decrypt(token)
print(r)
