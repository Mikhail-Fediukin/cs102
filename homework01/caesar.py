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
            b = (
                ord(i) + shift
            )  # юникод-значение буквы суммированное с шифтом. Далле проверка, выходит ли эта сумма за рамки юникодов букв.
            if ord("A") <= ord(i) <= ord("Z"):
                if b > ord("Z"):
                    ciphertext += chr((b - ord("Z")) % 26 + ord("A") - 1)
                else:
                    ciphertext += chr(ord(i) + shift)
            if ord("a") <= ord(i) <= ord("z"):
                if b > ord("z"):
                    ciphertext += chr((b - ord("z")) % 26 + ord("a") - 1)
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
            b = ord(i) - shift
            if ord("A") <= ord(i) <= ord("Z"):
                if b < ord("A"):
                    plaintext += chr(ord("Z") + 1 - (ord("A") - b) % 26)
                else:
                    plaintext += chr(ord(i) - shift)
            if ord("a") <= ord(i) <= ord("z"):
                if b < ord("a"):
                    plaintext += chr(ord("z") + 1 - (ord("a") - b) % 26)
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
