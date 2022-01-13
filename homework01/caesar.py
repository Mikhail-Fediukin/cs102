import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """

    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            new_i = ord(i) + shift
            if ord("A") <= ord(i) <= ord("Z"):
                if new_i > ord("Z"):
                    ciphertext += chr((new_i - ord("Z")) % 26 + ord("A") - 1)
                else:
                    ciphertext += chr(ord(i) + shift)
            if ord("a") <= ord(i) <= ord("z"):
                if new_i > ord("z"):
                    ciphertext += chr((new_i - ord("z")) % 26 + ord("a") - 1)
                else:
                    ciphertext += chr(ord(i) + shift)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """

    plaintext = ""
    for i in ciphertext:
        if i.isalpha():
            new_i = ord(i) - shift
            if ord("A") <= ord(i) <= ord("Z"):
                if new_i < ord("A"):
                    plaintext += chr(ord("Z") + 1 - (ord("A") - new_i) % 26)
                else:
                    plaintext += chr(ord(i) - shift)
            if ord("a") <= ord(i) <= ord("z"):
                if new_i < ord("a"):
                    plaintext += chr(ord("z") + 1 - (ord("a") - new_i) % 26)
                else:
                    plaintext += chr(ord(i) - shift)
        else:
            plaintext += i
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
