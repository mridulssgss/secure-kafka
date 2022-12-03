from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
from Crypto import Random

# setting iv to 16 random bytes
iv = Random.get_random_bytes(16)

def gen_key(bits=256):
    byte_size = 8
    size = (bits + 1) // byte_size
    key = Random.get_random_bytes(size)
    return key


def put_aes_key(key, key_file):
    with open(key_file, 'wb') as outfile:
        outfile.write(key)


def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return b64encode(cipher.encrypt(pad(plaintext.encode(), 16))).decode()


def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(b64decode(ciphertext.encode())), 16).decode()


def unpad_pkcs5(s):

    null_ch = b'\0'
    pos = len(s) - 1
    while (s[pos] == null_ch):
        pos -= 1

    return s[0:-pos]


'''
if __name__ == '__main__':
    str = input("Enter Input: ")
    key = gen_key()
    estr = encrypt_aes(key, str)
    print(f"Encrypted message = {estr}")
    print(f"Encrypted message = ")
    dstr = decrypt_aes(key, estr)
    print(dstr)
    if (str == dstr):
        print(f"Decrypted message = {dstr}")
    else:
        print(f"Decryption failed")
'''
