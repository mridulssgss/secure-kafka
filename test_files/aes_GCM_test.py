from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# getting data from user/input
#data = input()
data = "dummy data"
data = data.encode("UTF-8") 

 
# generating encryption keys
key = get_random_bytes(16)
nonce = get_random_bytes(12)

# storing key
with open("aes_gcm_key.bin", "wb") as fout:
    [fout.write(x) for x in (key, nonce)]

# encryption and generating hash
cipher_enc = AES.new(key, AES.MODE_GCM, nonce=nonce)
ctext, hash = cipher_enc.encrypt_and_digest(data)

# getting keys
with open("aes_gcm_key.bin", "rb") as fin:
    key, nonce = [fin.read(x) for x in (16, 12)]


# decryption and verifying hash
cipher_dec = AES.new(key, AES.MODE_GCM, nonce=nonce)

try:
    data = cipher_dec.decrypt_and_verify(ctext, hash)
    print(str(data.decode("UTF-8")))
except ValueError:
    print("MAC check failed")












