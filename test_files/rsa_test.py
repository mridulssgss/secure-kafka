import Crypto.PublicKey.RSA as RSA
from Crypto.Cipher import PKCS1_OAEP

"""
sc = "some data"
key = RSA.generate(2048)
print(key.export_key())
print(key.public_key().export_key())
"""

data = "dummy data".encode("UTF-8")
print(data)

# generating RSA private key
key = RSA.generate(2048)

public_key = key.public_key()

rsa_cipher_enc = PKCS1_OAEP.new(public_key)

encd = rsa_cipher_enc.encrypt(data)
print(encd)

rsa_cipher_dec = PKCS1_OAEP.new(key)
data = rsa_cipher_dec.decrypt(encd)
print(data)

