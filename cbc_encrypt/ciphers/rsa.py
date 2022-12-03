from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP


def gen_key(bits=2048):
    return RSA.generate(bits)


def put_rsa_key(key, key_file):
    with open(key_file, 'wb') as outfile:
        outfile.write(key)


def load_rsa_key(keyfile):
    with open(keyfile, 'rb') as f:
        return RSA.import_key(f.read())


def encrypt_rsa(public_key, msg):
    public_crypter = PKCS1_OAEP.new(public_key)
    enc_data = public_crypter.encrypt(msg.encode())
    return enc_data


def decrypt_rsa(private_key, en_msg):
    priv_decrypter = PKCS1_OAEP.new(private_key)
    return priv_decrypter.decrypt(en_msg).decode()


def dump_public_key(key, key_file):
    public_key = key.publickey().exportKey('PEM')
    put_rsa_key(public_key, key_file)


def dump_private_key(key_pair, key_file):
    put_rsa_key(key_pair.exportKey('PEM'), key_file)


if __name__ == '__main__':
    key = RSA.generate(2048)
    pub_key_path = "pub_key.pem"
    priv_key_path = "priv_key.pem"

    dump_public_key(key, pub_key_path)
    dump_private_key(key, priv_key_path)

    msg = input("Enter Input")

    public_key = load_rsa_key(pub_key_path)
    en_msg = encrypt_rsa(public_key, msg)

    print(f"encrypted msg {en_msg}")

    private_key = load_rsa_key(priv_key_path)
    msg = decrypt_rsa(private_key, en_msg)

    print(f"decrypt msg = {msg}")
