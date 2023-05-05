from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time

try:
 fout1 = open("time_log_aes_gcm_enc.txt", "a+") 
except IOError:
    print("IO Error")
    exit()

try:
 fout2 = open("time_log_aes_gcm_dec.txt", "a+") 
except IOError:
    print("IO Error")
    exit()


i = 1000

while (i != 0):

    #   getting data from user/input
    #data = input()
    with open("input_data.txt", "rb") as fin:
        data = fin.read()

    # generating encryption keys
    key = get_random_bytes(32)
    nonce = get_random_bytes(16)

    # encryption and generating hash

    tn = int(time.time_ns())

    cipher_enc = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ctext, hash = cipher_enc.encrypt_and_digest(data)

    tf = int(time.time_ns()) - tn
    fout1.writelines(str(tf) + '\n')

    tn = int(time.time_ns())
    # decryption and verifying hash
    cipher_dec = AES.new(key, AES.MODE_GCM, nonce=nonce)

    try:
        data = cipher_dec.decrypt_and_verify(ctext, hash)
        tf = int(time.time_ns()) - tn
        fout2.writelines(str(tf) + '\n')
        #print(data)
    except ValueError:
        print("MAC check failed")

    i -= 1

fout1.close()
fout2.close()
