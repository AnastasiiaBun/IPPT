while True:
 def CaesarChar(i):
    if i.isalnum():
        i = chr(ord(i) + 1)
        return i
    if not i.isalpha():
        return i
 def CesarCipher(S):
    new_S = ""
    for l in range(len(S)):
        new_S +=(CaesarChar(S[l]))
    return new_S
 S = input('введіть слово : ')
 print(CesarCipher(S))