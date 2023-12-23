#!/usr/bin/env python
# coding: utf-8

# In[5]:


from Crypto.Cipher import DES  # Mengimpor modul DES dari pustaka Crypto
from Crypto.Random import get_random_bytes  # Mengimpor fungsi get_random_bytes dari pustaka Crypto
from Crypto.Util.Padding import pad, unpad  # Mengimpor fungsi pad dan unpad dari pustaka Crypto untuk padding

#Fungsi unutk mendapatkan inputan
def get_user_input():
    # Mengambil input teks dari pengguna untuk dienkripsi dan kunci untuk enkripsi
    text = input("Masukkan teks untuk dienkripsi: ").encode('utf-8')  # Mengambil input teks dan mengenkod ke dalam bentuk utf-8
    key = input("Masukkan kunci (maksimal 8 karakter): ").encode('utf-8')  # Mengambil input kunci dan mengenkod ke dalam bentuk utf-8

    return text, key  # Mengembalikan teks dan kunci yang dimasukkan pengguna

#Fungsi enkripsi
def enkripsi(text, key):
    # Memastikan panjang kunci sesuai dengan panjang yang diperlukan (8 byte)
    if len(key) < 8:
        key = key.ljust(8, b'\x00')  # Jika kurang dari 8 byte, dilakukan padding dengan null bytes
    elif len(key) > 8:
        key = key[:8]  # Jika lebih dari 8 byte, dipotong menjadi 8 byte

    cipher = DES.new(key, DES.MODE_ECB)  # Membuat objek cipher DES dengan kunci yang diberikan dan mode ECB
    padded_text = pad(text, DES.block_size)  # Melakukan padding pada teks agar sesuai dengan blok DES
    ciphertext = cipher.encrypt(padded_text)  # Melakukan enkripsi teks menggunakan kunci DES
    return ciphertext  # Mengembalikan teks terenkripsi

#Fungsi dekripsi
def dekripsi(ciphertext, key):
    # Memastikan panjang kunci sesuai dengan panjang yang diperlukan (8 byte)
    if len(key) < 8:
        key = key.ljust(8, b'\x00')  # Jika kurang dari 8 byte, dilakukan padding dengan null bytes
    elif len(key) > 8:
        key = key[:8]  # Jika lebih dari 8 byte, dipotong menjadi 8 byte

    cipher = DES.new(key, DES.MODE_ECB)  # Membuat objek cipher DES dengan kunci yang diberikan dan mode ECB
    decrypted_text = unpad(cipher.decrypt(ciphertext), DES.block_size)  # Melakukan dekripsi teks dan menghapus padding
    return decrypted_text  # Mengembalikan teks yang telah didekripsi

def main():
    text, key = get_user_input()  # Meminta teks dan kunci dari pengguna

    if len(key) != 8:
        print("Panjang kunci harus maksimal 8 karakter.")
        return  # Menghentikan eksekusi program jika panjang kunci tidak tepat

    print(f'Plaintext: {text}')  # Menampilkan teks yang akan dienkripsi
    print(f'Key: {key}')  # Menampilkan kunci yang akan digunakan

    ciphertext = enkripsi(text, key)  # Melakukan enkripsi teks 
    print(f'Enkripsi: {ciphertext}')  # Menampilkan hasil enkripsi

    decrypted_text = dekripsi(ciphertext, key)  # Melakukan dekripsi teks 
    print(f'Dekripsi: {decrypted_text.decode("utf-8")}')  # Menampilkan hasil dekripsi

if __name__ == "__main__":
    main()


# In[ ]:




