caesar = "".join(map(chr, range(ord(" "), ord("я") + 1)))
 
def encrypt_caesar(text, step):
    return text.translate(
        str.maketrans(caesar, caesar[step:] + caesar[:step]))
 
def decrypt_caesar(text, step):
    return text.translate(
        str.maketrans(caesar[step:] + caesar[:step], caesar))
