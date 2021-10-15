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
    for i in range(len(plaintext)):
        if i > len(keyword) - 1:
            if 65 <= ord(keyword[i % len(keyword)]) <= 90:
                shift = ord(keyword[i % len(keyword)]) - ord("A")
            else:
                shift = ord(keyword[i % len(keyword)]) - ord("a")
        else:
            if 65 <= ord(keyword[i]) <= 90:
                shift = ord(keyword[i]) - ord("A")
            else:
                shift = ord(keyword[i]) - ord("a")

        if 65 <= ord(plaintext[i]) <= 90:
            sum = ord(plaintext[i]) + shift
            if sum > 90:
                ciphertext.append(chr(sum - 26))
            else:
                ciphertext.append(chr(sum))
        elif 97 <= ord(plaintext[i]) <= 122:
            sum = ord(plaintext[i]) + shift
            if sum > 122:
                ciphertext.append(chr(sum - 26))
            else:
                ciphertext.append(chr(sum))
        else:
            ciphertext.append(plaintext[i])
    return "".join(ciphertext)


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
    plaintext: list = []
    for i in range(len(ciphertext)):
        if i > len(keyword) - 1:
            if 65 <= ord(keyword[i % len(keyword)]) <= 90:
                shift = ord(keyword[i % len(keyword)]) - ord("A")
            else:
                shift = ord(keyword[i % len(keyword)]) - ord("a")
        else:
            if 65 <= ord(keyword[i]) <= 90:
                shift = ord(keyword[i]) - ord("A")
            else:
                shift = ord(keyword[i]) - ord("a")

        if 65 <= ord(ciphertext[i]) <= 90:
            sum = ord(ciphertext[i]) - shift
            if sum < 65:
                plaintext.append(chr(sum + 26))
            else:
                plaintext.append(chr(sum))
        elif 97 <= ord(ciphertext[i]) <= 122:
            sum = ord(ciphertext[i]) - shift
            if sum < 97:
                plaintext.append(chr(sum + 26))
            else:
                plaintext.append(chr(sum))
        else:
            plaintext.append(ciphertext[i])
    return "".join(plaintext)
