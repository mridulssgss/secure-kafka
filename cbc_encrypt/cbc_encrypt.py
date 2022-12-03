from Crypto import Random
from Crypto.Util import strxor
from ciphers.rsa import encrypt_rsa, decrypt_rsa, load_rsa_key, dump_private_key, dump_public_key, gen_key

MSG_BLOCK_SIZE = 128


def pad_pkcs5(s):

    null_ch = b'\0'
    #print(f"null_ch == {len(null_ch)}")
    sz = (MSG_BLOCK_SIZE - len(s) % MSG_BLOCK_SIZE)
    #print(f"sz = {sz}")
    rwords = chr(MSG_BLOCK_SIZE - len(s) % MSG_BLOCK_SIZE)
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


def cbc_encrypt(data, encrypt_func):
    data_padded = pad_pkcs5(data)

    msg_chunks = []

    for i in range(len(data_padded), MSG_BLOCK_SIZE):
        msg_chunks.append(data_padded[i: i + MSG_BLOCK_SIZE])

    IV = ''.join(str(Random.get_random_bytes(MSG_BLOCK_SIZE)))
    IV = IV.encode()
    IV2 = IV

    cipher_texts = []

    for d in msg_chunks:
        dx = strxor.strxor(d, IV)
        cipher_text = encrypt_func(dx)

        IV = cipher_text[0: MSG_BLOCK_SIZE]
        cipher_texts.append(cipher_text)

    cipher_texts.append(IV2)

    return (b"").join(cipher_texts)


def cbc_decrypt(data, decrypt_func):

    IV = data[-MSG_BLOCK_SIZE:]
    cipher_text = data[:-MSG_BLOCK_SIZE]

    encrypted_blocks = []

    for i in range(len(data), MSG_BLOCK_SIZE):
        encrypted_blocks.append(cipher_text[i:i+MSG_BLOCK_SIZE])

    plain_text = []

    for d in encrypted_blocks:
        dx = decrypt_func(d)
        clear_text = strxor.strxor(dx, IV)
        IV = d[0:MSG_BLOCK_SIZE]
        clear_text.append(clear_text)

    pad_text = "".join(plain_text)
    return unpad_pkcs5(pad_text)


if __name__ == "__main__":

    key = gen_key(2048)
    pub_key_path = "pub_key.pem"
    priv_key_path = "priv_key.pem"

    dump_public_key(key, pub_key_path)
    dump_private_key(key, priv_key_path)

    pub_key = load_rsa_key(pub_key_path)
    private_key = load_rsa_key(priv_key_path)

    msg = input("Enter message")
    en_msg = cbc_encrypt(msg.encode(), lambda x: encrypt_rsa(x, pub_key))
    print(f"{type(en_msg)}")

    plain_msg = cbc_decrypt(msg, lambda x: decrypt_rsa(x, private_key))
    print(f"decrypt message = {plain_msg}")
