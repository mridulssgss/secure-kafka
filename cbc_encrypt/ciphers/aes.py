from Crypto import Random
from Crypto.Cipher import AES


def gen_key(bits=256):
    byte_size = 8
    size = (bits + 1) // byte_size
    key = Random.get_random_bytes(size)
    return key


def put_aes_key(key, key_file):
    with open(key_file, 'wb') as outfile:
        outfile.write(key)


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
