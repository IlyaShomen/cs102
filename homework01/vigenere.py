def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    for index, b in enumerate(plaintext):
        if 'a' <= b <= 'z' or 'A' <= b <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= b <= 'z' else ord('A')
            c = ord(b) + shift
            if 'a' <= b <= 'z' and c > ord('z'):
                c -= 26
            elif 'A' <= b <= 'Z' and c > ord('Z'):
                c -= 26
            ciphertext += chr(c)
        else:
            ciphertext += b
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    for index, b in enumerate(ciphertext):
        if 'a' <= b <= 'z' or 'A' <= b <= 'Z':
            shift = ord(keyword[index % len(keyword)])
            shift -= ord('a') if 'a' <= b <= 'z' else ord('A')
            c = ord(b) - shift
            if 'a' <= b <= 'z' and c < ord('a'):
                c += 26
            elif 'A' <= b <= 'Z' and c < ord('A'):
                c += 26
            plaintext += chr(c)
        else:
            plaintext += b
    return plaintext


if __name__ == "__main__":
    import doctest
    doctest.testmod()