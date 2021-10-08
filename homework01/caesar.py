import typing as tp

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
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
    ciphertext = "".join(map(str, new_word))
    return ciphertext

plaintext = input("Введите Ваше великолепное слово: ")
print(encrypt_caesar(plaintext))


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
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
    plaintext = "".join(map(str, new_word))
    return plaintext

ciphertext = input("Введите Ваше великолепное зашифрованное слово: ")
print(decrypt_caesar(ciphertext))
