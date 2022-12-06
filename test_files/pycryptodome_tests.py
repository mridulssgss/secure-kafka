from Crypto.Cipher import AES
from os import urandom

# for generating cipher text
sc = urandom(16)
iv = urandom(16)
obj = AES.new(sc, AES.MODE_CBC, iv)

# Encryption

msg = b"Dummy Text Dummy Dummy Bye"
pad_len = 16 - (len(msg) % 16)
msg += bytes([pad_len]) * pad_len
print("msg is ", msg)
enct = obj.encrypt(msg)
print("cipher text is ", enct)

# Decryption

rev_obj = AES.new(sc, AES.MODE_CBC, iv)
dec_msg = rev_obj.decrypt(enct)
print("decrypted message is ", dec_msg.decode("UTF-8"))

