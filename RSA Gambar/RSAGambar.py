#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np  # Mengimpor modul numpy 
import cv2  # Mengimpor modul cv2 

# Fungsi untuk melakukan enkripsi XOR pada gambar
def encrypt_image(image_path):
    # Baca gambar dari path yang diberikan
    img = cv2.imread(image_path)  # Membaca gambar dari path yang diberikan
    height, width, _ = img.shape  # Mendapatkan dimensi gambar (tinggi, lebar, dan saluran warna)

    # Ubah gambar menjadi data byte
    image_bytes = img.tobytes()  # Mengonversi gambar ke dalam data byte

    # Kunci yang digunakan untuk enkripsi (bilangan acak dengan ukuran yang sama dengan data gambar)
    key = np.random.randint(0, 256, len(image_bytes), dtype=np.uint8)  # Membuat kunci acak dengan panjang yang sama dengan data gambar
    key = key.reshape((height, width, 3))  # Mengubah bentuk kunci sesuai dengan dimensi gambar

    # Enkripsi dengan melakukan operasi XOR antara gambar dan kunci
    encrypted_data = np.bitwise_xor(np.frombuffer(image_bytes, dtype=np.uint8), key.flatten())  # Melakukan operasi XOR antara data gambar dan kunci

    # Ubah data yang sudah dienkripsi ke dalam bentuk gambar
    encrypted_img = encrypted_data.reshape((height, width, 3))  # Mengubah data yang dienkripsi ke dalam bentuk gambar

    # Simpan gambar terenkripsi 
    cv2.imwrite("straw_enkripsi.jpg", encrypted_img)  # Menyimpan gambar terenkripsi

    print("Gambar berhasil dienkripsi.")  # Menampilkan pesan bahwa gambar berhasil dienkripsi
    return encrypted_data, key  # Mengembalikan data gambar yang terenkripsi dan kunci yang digunakan

# Fungsi untuk melakukan dekripsi XOR pada gambar
def decrypt_image(encrypted_data, key, height, width):
    # Lakukan operasi XOR antara data terenkripsi dan kunci untuk mendapatkan data awal
    decrypted_data = np.bitwise_xor(encrypted_data, key.flatten())  # Melakukan operasi XOR antara data terenkripsi dan kunci

    # Ubah data yang sudah didekripsi ke dalam bentuk gambar
    decrypted_img = decrypted_data.reshape((height, width, 3))  # Mengubah data yang didekripsi ke dalam bentuk gambar

    # Simpan gambar terdekripsi sebagai "gambar_terdekripsi.jpg"
    cv2.imwrite("straw_dekripsi.jpg", decrypted_img)  # Menyimpan gambar terdekripsi

    print("Gambar berhasil didekripsi.")  # Menampilkan pesan bahwa gambar berhasil didekripsi
    return decrypted_data  # Mengembalikan data gambar yang sudah didekripsi

# Contoh penggunaan dari fungsi-fungsi di atas
image_path = "D:\\A SEMS 3\\Keamanan Data\\straw.jpg"  # Ganti dengan path gambar yang ingin dienkripsi

# Enkripsi gambar
encrypted_data, key = encrypt_image(image_path)

# Dekripsi gambar menggunakan data terenkripsi dan kunci yang dihasilkan sebelumnya
decrypted_data = decrypt_image(encrypted_data, key, *cv2.imread(image_path).shape[:2])


# In[ ]:




