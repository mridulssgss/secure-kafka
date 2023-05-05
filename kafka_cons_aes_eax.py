import kafka
import kafka.errors
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# checking keys if they exists
try:
    key_file = open("aes_eax_key.bin", "rb")
    key_file.close()
except FileNotFoundError:
    print("encryption keys not found")
    exit(-1)

# getting keys
with open("aes_eax_key.bin", "rb") as fin:
    key = fin.read(32)

consumer = kafka.KafkaConsumer("python_tests", bootstrap_servers=['localhost:9092'], auto_offset_reset='latest')


for event in consumer:
    print("> ", end="")
    cipher_dec = AES.new(key, AES.MODE_EAX, event.value[:16])
    print(event.timestamp,": ", str(cipher_dec.decrypt(event.value[16:])))

