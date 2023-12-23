#!/usr/bin/env python
# coding: utf-8

# In[15]:


from Crypto.PublicKey import RSA  # Mengimpor modul RSA dari pustaka Crypto
from Crypto.Cipher import PKCS1_OAEP  # Mengimpor modul PKCS1_OAEP dari pustaka Crypto
import base64  # Mengimpor modul base64

# Fungsi untuk membuat pasangan kunci RSA
def buat_kunci_RSA():
    kunci = RSA.generate(2048)  # Membuat pasangan kunci RSA dengan panjang 2048 bit
    return kunci

# Fungsi untuk menyimpan kunci RSA ke dalam file
def simpan_kunci_ke_file(kunci, nama_file):
    with open(nama_file, 'wb') as file:
        file.write(kunci.export_key())  # Menyimpan kunci ke dalam file

# Fungsi untuk melakukan enkripsi file menggunakan kunci publik RSA
def enkripsi_file(nama_file, public_key_path):
    with open(nama_file, 'rb') as file:
        teks_plaintext = file.read()  # Membaca isi file untuk dienkripsi

    with open(public_key_path, 'rb') as file:
        kunci_publik = RSA.import_key(file.read())  # Membaca kunci publik RSA dari file

    cipher_rsa = PKCS1_OAEP.new(kunci_publik)  # Membuat objek enkripsi dengan kunci publik RSA
    teks_terenkripsi = cipher_rsa.encrypt(teks_plaintext)  # Melakukan enkripsi teks menggunakan kunci publik RSA

    teks_terenkripsi_b64 = base64.b64encode(teks_terenkripsi).decode('utf-8')  # Encoding hasil enkripsi ke dalam base64

    nama_file_terenkripsi = "enkripsi_rsa.txt"  # Menambahkan ekstensi nama file terenkripsi
    with open(nama_file_terenkripsi, 'w') as file_terenkripsi:
        file_terenkripsi.write(teks_terenkripsi_b64)  # Menyimpan pesan terenkripsi ke dalam file teks

    return nama_file_terenkripsi

# Fungsi untuk melakukan dekripsi file
def dekripsi_file(nama_file_terenkripsi, private_key_path):
    with open(nama_file_terenkripsi, 'r') as file:
        teks_terenkripsi_b64 = file.read()  # Membaca isi file terenkripsi

    teks_terenkripsi = base64.b64decode(teks_terenkripsi_b64)  # Decoding hasil enkripsi dari base64

    with open(private_key_path, 'rb') as file:
        kunci_privat = RSA.import_key(file.read())  # Membaca kunci privat RSA dari file

    cipher_rsa = PKCS1_OAEP.new(kunci_privat)  # Membuat objek dekripsi dengan kunci privat RSA
    teks_terdekripsi = cipher_rsa.decrypt(teks_terenkripsi)  # Melakukan dekripsi teks menggunakan kunci privat RSA

    nama_file_terdekripsi = "dekripsi_rsa.txt"  # Menambahkan ekstensi nama file terdekripsi
    with open(nama_file_terdekripsi, 'wb') as file_terdekripsi:
        file_terdekripsi.write(teks_terdekripsi)  # Menyimpan pesan yang sudah didekripsi ke dalam file teks

    return nama_file_terdekripsi

# Buat pasangan kunci RSA
kunci_privat = buat_kunci_RSA()  # Membuat kunci privat RSA
kunci_publik = kunci_privat.publickey()  # Mendapatkan kunci publik dari kunci privat

# Simpan kunci privat ke dalam file
simpan_kunci_ke_file(kunci_privat, "private_key.pem")

# Simpan kunci publik ke dalam file
simpan_kunci_ke_file(kunci_publik, "public_key.pem")

# Path file yang akan dienkripsi
nama_file = "jaringan.txt"

# Enkripsi file
file_terenkripsi = enkripsi_file(nama_file, "public_key.pem")
print(f"File Terenkripsi: {file_terenkripsi}")  # Menampilkan nama file terenkripsi

# Dekripsi file yang telah terenkripsi sebelumnya
file_terdekripsi = dekripsi_file(file_terenkripsi, "private_key.pem")
print(f"File Terdekripsi: {file_terdekripsi}")  # Menampilkan nama file terdekripsi


# In[ ]:




