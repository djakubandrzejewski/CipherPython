from Crypto.Cipher import AES

# Wczytujemy plik txt z kluczem do zaszyfrowania
with open('key.txt', 'r') as f:
    key = f.readline()
# Wprowadzamy dane do zaszyfrowania
data = input("Tekst do zaszyfrowania:")
# Tworzymy obiekt szyfrujący
cipher = AES.new(key.encode('utf8'), AES.MODE_EAX)

# Szyfrujemy dany
ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf8'))

# Zapisanie zaszyfrowanych danych do pliku txt
with open('zaszyfrowane.txt', 'wb') as f:
    [f.write(x) for x in (cipher.nonce, tag, ciphertext)]