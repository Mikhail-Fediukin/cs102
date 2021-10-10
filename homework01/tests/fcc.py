def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = []
    plaintext.split()
    keyword.split()
    k = 0
    for i in range(len(plaintext)):
        if plaintext[i].isalpha() == True:
            if 65 <= ord(plaintext[i]) <= 90:
                if ord(plaintext[i]) + ord(keyword[(i + k) % len(keyword)]) > 90:
                    ciphertext.append(chr(ord(plaintext[i]) + ord(keyword[(i + k) % len(keyword)]) - 65))
                else:
                    ciphertext.append(chr(ord(plaintext[i]) + ord(keyword[(i + k) % len(keyword)])))
            elif 97 <= ord(plaintext[i]) <= 122:
                if ord(plaintext[i]) + ord(keyword[i % len(keyword)]) > 122:
                    ciphertext.append(chr(ord(plaintext[i]) + ord(keyword[(i + k) % len(keyword)]) - 97))
                else:
                    ciphertext.append(chr(ord(plaintext[i]) + ord(keyword[(i + k) % len(keyword)])))
        else:
            ciphertext.append(plaintext[i])
            k += 1
    return "".join(ciphertext)

print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
