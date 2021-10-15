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
    ciphertext: list = []
    new_word = []
    for i in plaintext:
        if i.isalpha() == True:
            b = ord(i) + shift
            if 65 <= ord(i) <= 90:
                if b > 90:
                    new_word.append(chr((b - 90) % 26 + ord("A") - 1))
                else:
                    new_word.append(chr(ord(i) + shift))
            if 97 <= ord(i) <= 122:
                if b > 122:
                    new_word.append(chr((b - 122) % 26 + ord("a") - 1))
                else:
                    new_word.append(chr(ord(i) + shift))
        else:
            new_word.append(i)
    return "".join(map(str, new_word))


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
    plaintext: list = []
    new_word = []
    for i in ciphertext:
        if i.isalpha() == True:
            b = ord(i) - shift
            if 65 <= ord(i) <= 90:
                if b < 65:
                    new_word.append(chr(ord("Z") + 1 - (65 - b) % 26))
                else:
                    new_word.append(chr(ord(i) - shift))
            if 97 <= ord(i) <= 122:
                if b < 97:
                    new_word.append(chr(ord("z") + 1 - (97 - b) % 26))
                else:
                    new_word.append(chr(ord(i) - shift))
        else:
            new_word.append(i)
    return "".join(map(str, new_word))


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
