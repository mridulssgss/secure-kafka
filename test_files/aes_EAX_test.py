# AES Encryption with built-in authentication
import Crypto.Cipher.AES as AES
from Crypto.Random import get_random_bytes
import base64

# message data
with open("input_data.txt", "rb") as fin:
    data = base64.urlsafe_b64encode(fin.read())
    
# Encryption key and cipher
key = get_random_bytes(32)
cipher_enc = AES.new(key, AES.MODE_EAX)
ciphertext, hash = cipher_enc.encrypt_and_digest(data)

# Decryption cipher
cipher_dec = AES.new(key, AES.MODE_EAX, cipher_enc.nonce)

try:
    data = cipher_dec.decrypt_and_verify(ciphertext, hash)
except ValueError:
    print("MAC Check failed")
data = base64.urlsafe_b64decode(data)
print(data)
