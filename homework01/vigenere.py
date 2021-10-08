def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    for w in range(len(keyword)):
        if keyword[w].islower() == True:
            codes.append(ord(str(keyword[w])) - 97)
        else:
            codes.append(ord(str(keyword[w])) - 65)
    for w in plaintext: plains.append(ord(w))
    if len(codes) < len(plains):
        for k in range(len(codes), len(plains)): a.append(codes[k % len(codes)])
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
    ciphertext = "".join(bill)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    for w in range(len(keyword)):
        if keyword[w].islower() == True:
            codez.append(ord(str(keyword[w])) - 97)
        else:
            codez.append(ord(str(keyword[w])) - 65)
    for w in ciphertext: plainz.append(ord(w))
    if len(codez) < len(plainz):
        for k in range(len(codez), len(plainz)): a.append(codez[k % len(codez)])
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
    plaintext = "".join(bill)
    return plaintext

plains = []; codes = []; bill = []; a = []; codez = []; plainz = []; bil = []

plaintext = input("Введите Ваше великолепное слово: ")
ciphertext = input("Введите Ваше великолепное зашифрованное слово: ")
keyword = input("Введите Ваш великолепный ключ: ")

print("Зашифрованное слово выглядит так: ", encrypt_vigenere(plaintext, keyword))
print("Расшифрованное слово выглядит так: ", decrypt_vigenere(ciphertext, keyword))