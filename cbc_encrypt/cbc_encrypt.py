


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