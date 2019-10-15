def encrypt_caesar(plaintext):
    ciphertext = ''
    for b in plaintext:
        if 'a' <= b <= 'z' or 'A' <= b <= 'Z':
            c = ord(b) + 3
            if ord('Z') < c < ord('a') or c > ord('z'):
                c -= 26
                ciphertext += chr(c)
            else:
                ciphertext += b
                return ciphertext


def decrypt_caesar(ciphertext):
    plaintext = ''
    for b in ciphertext:
        if 'a' <= b <= 'z' or 'A' <= b <= 'Z':
            c = ord(b) - 3
            if ord('a') > c > ord('Z') or c < ord('A'):
                c += 26
                plaintext += chr(c)
        else:
            plaintext += b
    return plaintext


if __name__ == "__main__":
    import doctest
    doctest.testmod()
