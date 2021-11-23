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
    ciphertext = ""
    for i, j in enumerate(plaintext):
        if i > len(keyword) - 1:
            if ord("A") <= ord(keyword[i % len(keyword)]) <= ord("Z"):
                shift = ord(keyword[i % len(keyword)]) - ord("A")
            else:
                shift = ord(keyword[i % len(keyword)]) - ord("a")
        else:
            if ord("A") <= ord(keyword[i]) <= ord("Z"):
                shift = ord(keyword[i]) - ord("A")
            else:
                shift = ord(keyword[i]) - ord("a")

        if ord("A") <= ord(j) <= ord("Z"):
            sum = ord(j) + shift
            if sum > ord("Z"):
                ciphertext += chr(sum - 26)
            else:
                ciphertext += chr(sum)
        elif ord("a") <= ord(j) <= ord("z"):
            sum = ord(j) + shift
            if sum > ord("z"):
                ciphertext += chr(sum - 26)
            else:
                ciphertext += chr(sum)
        else:
            ciphertext += j
    return ciphertext


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
    for i, j in enumerate(ciphertext):
        if i > len(keyword) - 1:
            if ord("A") <= ord(keyword[i % len(keyword)]) <= ord("Z"):
                shift = ord(keyword[i % len(keyword)]) - ord("A")
            else:
                shift = ord(keyword[i % len(keyword)]) - ord("a")
        else:
            if ord("A") <= ord(keyword[i]) <= ord("Z"):
                shift = ord(keyword[i]) - ord("A")
            else:
                shift = ord(keyword[i]) - ord("a")

        if ord("A") <= ord(j) <= ord("Z"):
            sum = ord(j) - shift
            if sum < ord("A"):
                plaintext += chr(sum + 26)
            else:
                plaintext += chr(sum)
        elif ord("a") <= ord(j) <= ord("z"):
            sum = ord(j) - shift
            if sum < ord("a"):
                plaintext += chr(sum + 26)
            else:
                plaintext += chr(sum)
        else:
            plaintext += j
    return plaintext
