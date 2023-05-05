import kafka
import kafka.errors
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time

# creating kafka producer instance
pcr = kafka.KafkaProducer(bootstrap_servers="localhost:9092")

# generating keys if not exists
try:
    key_file = open("aes_gcm_key.bin", "rb")
    key_file.close()
except FileNotFoundError:
    with open("aes_gcm_key.bin", "wb") as fout:
        fout.write(get_random_bytes(32))

# getting keys
with open("aes_gcm_key.bin", "rb") as fin:
    key = fin.read(32) # 32 random bytes for AES 256


#msg = b"a sample test message"
msg = input("enter message: ").encode("UTF-8")
while (msg != "exit".encode("UTF-8")):
    nonce = get_random_bytes(16)
    cipher_enc = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ctext, hash = cipher_enc.encrypt_and_digest(msg)
    fmsg = nonce
    fmsg += hash
    fmsg += ctext

    # kafka producer is sending messages asynchronously
    future = pcr.send("python_tests", fmsg, timestamp_ms=int(time.time()))

    try:
        rcd = future.get(timeout=10)
    except kafka.errors.KafkaError:
        print("error in sending messages")
    #print(rcd)

    msg = input("enter message: ").encode("UTF-8")
