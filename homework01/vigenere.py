def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext: list = []
    plains: list = []
    codes: list = []
    bill: list = []
    a: list = []
    for w in range(len(keyword)):
        if keyword[w].islower() == True:
            codes.append(ord(str(keyword[w])) - 97)
        else:
            codes.append(ord(str(keyword[w])) - 65)
    plaintext.split()
    for i in range(len(plaintext)):
        plains.append(ord(plaintext[i]))
    if len(codes) < len(plains):
        for k in range(len(codes), len(plains)):
            a.append(codes[k % len(codes)])
    new_codes = codes + a
    for i in range(len(plains)):
        n = int(new_codes[i])
        p = int(plains[i])
        if not p <= 90:
            if p + n > 122:
                bill.append(chr(p + n - 26))
            else:
                bill.append(chr(p + n))
        else:
            if p + n > 90:
                bill.append(chr(p + n - 26))
            else:
                bill.append(chr(p + n))
    return "".join(bill)


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    a: list = []
    codez: list = []
    plainz: list = []
    bil: list = []
    for w in range(len(keyword)):
        if keyword[w].islower() == True:
            codez.append(ord(str(keyword[w])) - 97)
        else:
            codez.append(ord(str(keyword[w])) - 65)
    ciphertext.split()
    for i in range(len(ciphertext)):
        plainz.append(ord(ciphertext[i]))
    if len(codez) < len(plainz):
        for k in range(len(codez), len(plainz)):
            a.append(codez[k % len(codez)])
    new_codez = codez + a
    for i in range(len(plainz)):
        n = int(new_codez[i])
        p = int(plainz[i])
        if not p <= 90:
            if p - n < 97:
                bil.append(chr(p - n + 26))
            else:
                bil.append(chr(p - n))
        else:
            if p - n < 65:
                bil.append(chr(p - n + 26))
            else:
                bil.append(chr(p - n))
    return "".join(bil)
