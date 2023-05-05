from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time

try:
 fout1 = open("time_log_aes_cbc_enc_growth.txt", "a+") 
except IOError:
    print("IO Error")
    exit()

try:
 fout2 = open("time_log_aes_cbc_dec_growth.txt", "a+") 
except IOError:
    print("IO Error")
    exit()


i = 10000
data = b""

while (i != 0):

    #   getting data from user/input
    #data = input()
    data += get_random_bytes(32)
    
    # preparing data
    pad_len = 32 - (len(data) % 32)
    data += bytes([pad_len]) * pad_len

    # generating encryption keys
    key = get_random_bytes(32)
    iv = get_random_bytes(16)

    # encryption and generating hash

    tn = int(time.time_ns())

    cipher_enc = AES.new(key, AES.MODE_CBC, iv=iv)
    ctext = cipher_enc.encrypt(data)

    tf = int(time.time_ns()) - tn
    fout1.writelines(str(len(data)) + "," + str(tf) + '\n')

    tn = int(time.time_ns())
    # decryption and verifying hash
    cipher_dec = AES.new(key, AES.MODE_CBC, iv=iv)

    try:
        data = cipher_dec.decrypt(ctext)
        tf = int(time.time_ns()) - tn
        fout2.writelines(str(len(data)) + "," + str(tf) + '\n')
        #print(data)
    except ValueError:
        print("MAC check failed")

    i -= 1

fout1.close()
fout2.close()
