#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Import library math dan random
import math
import random

# Fungsi untuk memeriksa apakah sebuah bilangan adalah bilangan prima
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Fungsi untuk menghasilkan pasangan kunci RSA (public key, private key)
def generate_keypair():
    # Pilih bilangan prima acak p
    p = random.randint(100, 500)
    while not is_prime(p):
        p = random.randint(100, 500)

    # Pilih bilangan prima acak q, pastikan q != p
    q = random.randint(100, 500)
    while not is_prime(q) or q == p:
        q = random.randint(100, 500)

    # Hitung modulus n dan nilai Euler phi
    n = p * q
    phi = (p - 1) * (q - 1)

    # Pilih eksponen enkripsi e, pastikan e relatif prima dengan phi
    e = random.randint(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randint(1, phi)

    # Hitung eksponen dekripsi d menggunakan modinv
    d = modinv(e, phi)

    # Kembalikan pasangan kunci
    return ((n, e), (n, d))

# Fungsi untuk menghitung invers modulo menggunakan algoritma Euclidean yang diperpanjang
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Fungsi untuk mengenkripsi plaintext menggunakan algoritma RSA
def encrypt(public_key, plaintext):
    n, e = public_key
    # Enkripsi setiap karakter plaintext menjadi ciphertext
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# Fungsi untuk mendekripsi ciphertext menggunakan algoritma RSA
def decrypt(private_key, ciphertext):
    n, d = private_key
    # Dekripsi setiap karakter ciphertext menjadi plaintext
    decrypted = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted)

# Program utama
if __name__ == '__main__':
    # Generate pasangan kunci
    public_key, private_key = generate_keypair()
    print(f'Public Key: {public_key}')
    print(f'Private Key: {private_key}')

    # Input plaintext dari pengguna
    plaintext = input('Enter plaintext: ')

    # Enkripsi plaintext
    ciphertext = encrypt(public_key, plaintext)
    print(f'Enkripsi: {ciphertext}')

    # Dekripsi ciphertext
    decrypted_text = decrypt(private_key, ciphertext)
    print(f'Dekripsi: {decrypted_text}')


# In[ ]:




