#!/usr/bin/env python
# coding: utf-8

# In[18]:


from Crypto.Cipher import AES  # Mengimpor modul AES dari pustaka Crypto
from Crypto.Random import get_random_bytes  # Mengimpor fungsi get_random_bytes untuk menghasilkan kunci acak
import base64  # Mengimpor modul base64 untuk konversi data menjadi bentuk yang bisa disimpan/ditransfer

# Fungsi enkripsi menggunakan AES dalam mode CFB
def enkripsi(data, kunci):
    iv = get_random_bytes(AES.block_size)  # Menghasilkan vektor inisialisasi (IV) sepanjang ukuran blok AES
    cipher_enkripsi = AES.new(kunci, AES.MODE_CFB, iv=iv)  # Membuat objek AES untuk enkripsi dengan kunci dan IV yang telah dibuat
    data_terenkripsi = cipher_enkripsi.encrypt(data)  # Melakukan enkripsi pada data menggunakan objek AES yang telah dibuat
    data_hasil_enkripsi = iv + data_terenkripsi  # Menggabungkan IV dengan data terenkripsi
    return data_hasil_enkripsi  # Mengembalikan data yang telah terenkripsi beserta IV

# Fungsi dekripsi menggunakan AES dalam mode CFB
def dekripsi(data_terenkripsi, kunci):
    iv = data_terenkripsi[:AES.block_size]  # Mengambil IV dari data yang telah terenkripsi
    data_terenkripsi = data_terenkripsi[AES.block_size:]  # Mengambil data terenkripsi setelah bagian IV
    cipher_dekripsi = AES.new(kunci, AES.MODE_CFB, iv=iv)  # Membuat objek AES untuk dekripsi dengan kunci dan IV yang diperoleh
    data_terdekripsi = cipher_dekripsi.decrypt(data_terenkripsi)  # Melakukan dekripsi pada data terenkripsi menggunakan objek AES yang telah dibuat
    return data_terdekripsi  # Mengembalikan data yang telah terdekripsi

kunci = get_random_bytes(16)  # Menghasilkan kunci acak sepanjang 16 byte untuk enkripsi dan dekripsi

data_input = input("Masukkan teks: ")  # Memasukkan teks yang akan dienkripsi
data = data_input.encode('utf-8')  # Mengonversi teks menjadi bentuk byte menggunakan encoding utf-8

# Enkripsi data menggunakan fungsi enkripsi
data_terenkripsi = enkripsi(data, kunci)
print("Enkripsi: ", data_terenkripsi)  # Menampilkan hasil enkripsi

# Dekripsi data menggunakan fungsi dekripsi
data_terdekripsi = dekripsi(data_terenkripsi, kunci)
print("Dekripsi: ", data_terdekripsi.decode('utf-8'))  # Menampilkan hasil dekripsi


# In[ ]:




