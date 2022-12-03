from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

key = get_random_bytes(32)
iv = get_random_bytes(16)


def pad_pkcs5(s):

    null_ch = b'\0'
    #print(f"null_ch == {len(null_ch)}")
    sz = (AES.block_size - len(s) % AES.block_size)
    #print(f"sz = {sz}")
    rwords = chr(AES.block_size - len(s) % AES.block_size)
    #print(f"rwords = {len(rwords.encode())}")
    if sz == 0:
        return s
    else:
        return s + sz * null_ch


def unpad_pkcs5(s):

    null_ch = b'\0'
    pos = len(s) - 1
    while (s[pos] == null_ch):
        pos -= 1

    return s[0:-pos]


def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return b64encode(cipher.encrypt(pad(plaintext.encode(), 16))).decode()


def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad_pkcs5(cipher.decrypt(b64decode(ciphertext.encode())), 16).decode()


if __name__ == "__main__":
    msg = input("Enter input: ")
    encrypt_msg = encrypt("hello", key)
    print(f"Encrypted msg = {encrypt_msg}")
    decrypt_msg = decrypt(encrypt_msg, key)
    print(f"Decrypted msg = {decrypt_msg}")
