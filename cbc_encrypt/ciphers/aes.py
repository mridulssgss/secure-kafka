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


def encrypt_aes(key, msg):
    return encrypt_aes_bytes(key, msg.encode())


def encrypt_aes_bytes(key, msg):

    # print(f"AES block size = {AES.block_size}")
    # print(f"msg size {msg}")
    msg_sz = len(msg)
    if msg_sz % AES.block_size != 0:
        msg = pad_pkcs5(msg)
    # make an AES object with key,mode ecb
    aes_obj = AES.new(key, AES.MODE_ECB)
    cipher_text = aes_obj.encrypt(msg)

    return cipher_text


def decrypt_aes_bytes(key, msg):
    aes_obj = AES.new(key, AES.MODE_ECB)
    p_text = aes_obj.decrypt(msg)

    return unpad_pkcs5(p_text)


def decrypt_aes(key, msg):
    return decrypt_aes_bytes(key, msg).decode()


'''
if __name__ == '__main__':
    str = input()
    key = gen_key()
    estr = encrypt_aes(key, str)
    print(f"Encrypted message = {estr}")
    dstr = decrypt_aes(key, estr)
    if (str == dstr):
        print(f"Decrypted message = {dstr}")
    else:
        print(f"Decryption failed")
'''
