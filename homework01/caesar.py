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
            if i == "X" or i == "Y" or i == "Z" or i == "x" or i == "y" or i == "z":
                l = chr(ord(str(i)) - 23)
                new_word.append(l)
            else:
                l = chr(ord(str(i)) + shift)
                new_word.append(l)
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
            if i == "A" or i == "B" or i == "C" or i == "a" or i == "b" or i == "c":
                l = chr(ord(str(i)) + 23)
                new_word.append(l)
            else:
                l = chr(ord(str(i)) - shift)
                new_word.append(l)
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
