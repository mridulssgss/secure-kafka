# AES Encryption with built-in authentication
import Crypto.Cipher.AES as AES
from Crypto.Random import get_random_bytes
import base64
import time


try:
 fout1 = open("time_log_aes_eax_enc.txt", "a+") 
except IOError:
    print("IO Error")
    exit()

try:
 fout2 = open("time_log_aes_eax_dec.txt", "a+") 
except IOError:
    print("IO Error")
    exit()


i = 1000

while (i != 0):
    # message data
    with open("input_data.txt", "rb") as fin:
        data = base64.urlsafe_b64encode(fin.read())

    # Encryption key and cipher
    key = get_random_bytes(32)
    
    tn = int(time.time_ns())
    

    cipher_enc = AES.new(key, AES.MODE_EAX)
    ciphertext, hash = cipher_enc.encrypt_and_digest(data)

    tf = int(time.time_ns()) - tn
 
    fout1.writelines(str(tf) + '\n')


    tn = int(time.time_ns())
    # Decryption cipher
    cipher_dec = AES.new(key, AES.MODE_EAX, cipher_enc.nonce)

    try:
        data = cipher_dec.decrypt_and_verify(ciphertext, hash)
        tf = int(time.time_ns()) - tn
        fout2.writelines(str(tf) + '\n')
    except ValueError:
        print("MAC Check failed")
    data = base64.urlsafe_b64decode(data)
    #print(data)

    i -= 1

fout1.close()
fout2.close()

