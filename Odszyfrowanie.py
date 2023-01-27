from Crypto.Cipher import AES

# Wczytujemy klucz potrzebny do odszyfrowania
with open('key.txt', 'r') as f:
    key = f.readline()

# Odczytanie danych zaszyfrowanych z pliku
with open('zaszyfrowane.txt', 'rb') as f:
    nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]

# utworzenie obiektu odszyfrowywania
cipher = AES.new(key.encode('utf8'), AES.MODE_EAX, nonce)

# Odszyfrowanie danych
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)
data = str(data)
with open('odszyfrowane.txt' , 'w') as f:
    f.write(data)

