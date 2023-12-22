#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np  # Mengimpor modul numpy

# Fungsi untuk mengubah teks menjadi matriks huruf-huruf alfabet
def text_to_matrix(text, dimension):
    text = text.replace(" ", "").upper()  # Menghapus spasi dan ubah ke huruf besar
    n = len(text)
    if n % dimension != 0:
        text += "X" * (dimension - (n % dimension))  # Menambahkan 'X' jika panjang teks tidak sesuai dengan dimensi matriks
        n = len(text)
    matrix = np.zeros((dimension, n // dimension), dtype=int)  # Membuat matriks kosong sesuai dengan dimensi yang diberikan
    idx = 0
    for i in range(n // dimension):  # Loop untuk mengisi matriks dengan karakter dari teks
        for j in range(dimension):
            matrix[j][i] = ord(text[idx]) - ord('A')  # Mengubah karakter alfabet menjadi nilai numerik dan memasukkannya ke dalam matriks
            idx += 1
    return matrix  # Mengembalikan matriks yang telah diisi dengan teks

# Fungsi untuk enkripsi menggunakan Hill Cipher
def hill_cipher_encrypt(plaintext, key_matrix):
    dimension = key_matrix.shape[0]  # Mendapatkan dimensi matriks kunci
    plaintext_matrix = text_to_matrix(plaintext, dimension)  # Konversi teks ke matriks

    if dimension != plaintext_matrix.shape[0]:  # Memeriksa apakah dimensi matriks kunci sesuai dengan matriks teks
        raise ValueError("Dimensi kunci dan teks tidak sesuai")

    encrypted_matrix = np.dot(key_matrix, plaintext_matrix) % 26  # Proses enkripsi menggunakan matriks kunci
    ciphertext = matrix_to_text(encrypted_matrix)  # Konversi matriks terenkripsi kembali ke teks
    return ciphertext  # Mengembalikan teks terenkripsi

# Fungsi untuk dekripsi menggunakan Hill Cipher
def hill_cipher_decrypt(ciphertext, key_matrix):
    key_inverse = np.linalg.inv(key_matrix)  # Mencari matriks invers dari kunci
    key_inverse = np.round(key_inverse * np.linalg.det(key_matrix) % 26).astype(int)  # Modulo 26 untuk integer

    ciphertext_matrix = text_to_matrix(ciphertext, key_matrix.shape[0])  # Konversi teks terenkripsi ke matriks
    decrypted_matrix = np.dot(key_inverse, ciphertext_matrix) % 26  # Proses dekripsi menggunakan matriks invers kunci
    plaintext = matrix_to_text(decrypted_matrix)  # Konversi matriks terdekripsi kembali ke teks
    return plaintext  # Mengembalikan teks terdekripsi

# Fungsi untuk mengubah matriks huruf-huruf alfabet kembali menjadi teks
def matrix_to_text(matrix):
    text = ""
    for i in range(matrix.shape[1]):
        for j in range(matrix.shape[0]):
            text += chr(matrix[j][i] % 26 + ord('A'))  # Mengembalikan karakter dari nilai numerik ke alfabet dan menyusun kembali teks
    return text  # Mengembalikan teks dari matriks huruf-huruf alfabet

# Input dimensi matriks dan nilai-nilai matriks kunci
try:
    dimension = int(input("Masukkan dimensi matriks (contoh: 2 untuk matriks 2x2, 3 untuk matriks 3x3): "))
    key_values = list(map(int, input(f"Masukkan {dimension**2} nilai matriks kunci (pisahkan dengan spasi): ").split()))
    key_matrix = np.array(key_values).reshape(dimension, dimension)  # Membentuk matriks kunci dari nilai-nilai yang dimasukkan oleh pengguna
except ValueError:
    print("Masukan tidak valid. Harap masukkan angka.")
else:
    plaintext = input("Masukkan teks yang ingin dienkripsi: ")

    try:
        # Enkripsi teks
        encrypted_text = hill_cipher_encrypt(plaintext, key_matrix)
        print("\nHasil Enkripsi:")
        print("Plaintext:", plaintext)
        print("Encrypted:", encrypted_text)

        # Dekripsi teks
        decrypted_text = hill_cipher_decrypt(encrypted_text, key_matrix)
        print("\nHasil Dekripsi:")
        print("Decrypted:", decrypted_text)
    except ValueError as e:
        print("Error:", e)


# In[ ]:




