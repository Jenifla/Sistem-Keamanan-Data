<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>Sistem Keamanan Data</title>
</head>

<body>
    <div class="container">
        <div class="judul">
            <h3>Enkripsi dan Dekripsi</h3>
            <h5>Vigenere Cipher</h5>
        </div>
        <div class="card card-outline card-primary">
            <div class="card-body">
                <?php
                // Memeriksa apakah tombol "enkripsi" atau "dekripsi" telah ditekan
                if (isset($_POST['enkripsi']) || isset($_POST['dekripsi'])) {

                    // Fungsi enkripsi Vigenere Cipher
                    function vigenere_encrypt($input, $key)
                    {
                        $input = strtoupper($input); // Konversi teks input ke huruf besar
                        $key = strtoupper($key); // Konversi kunci ke huruf besar
                        $input_length = strlen($input); // Hitung panjang teks plaintext
                        $key_length = strlen($key); // Hitung panjang kunci yang digunakan
                        $cipher_text = ''; //  Menyimpan hasil enkripsi

                        for ($i = 0, $j = 0; $i < $input_length; $i++) { // Perulangan untuk mengiterasi setiap karakter dalam plaintext
                            if ($input[$i] === ' ') {
                                // Jika karakter adalah spasi, abaikan dan lanjutkan ke karakter berikutnya
                                $cipher_text .= ' ';
                                continue;
                            }
                            $char_input = ord($input[$i]) - 65; // Konversi karakter dalam plaintext menjadi angka & - 65 untuk menhasilkan nilai dengan rentang 0 - 25
                            $char_key = ord($key[$j % $key_length]) - 65; // Konversi karakter dalam key dan mengulang key jika sudah mencapai panjang penuh
                            $char_cipher = ($char_input + $char_key) % 26; // Memperoleh hasil enkripsi dengan menjumlahkan karakter plaintext dan key dan diambil mod 26
                            $cipher_text .= chr($char_cipher + 65); // Konversi hasil enkripsi dalam bentuk angka menjadi karakter huruf
                            $j++;
                        }

                        return $cipher_text;
                    }

                    // Fungsi dekripsi Vigenere Cipher
                    function vigenere_decrypt($input, $key)
                    {
                        $input = strtoupper($input); // Konversi teks input ke huruf besar
                        $key = strtoupper($key); // Konversi kunci ke huruf besar
                        $input_length = strlen($input); // Hitung panjang teks plaintext
                        $key_length = strlen($key); // Hitung panjang kunci yang digunakan
                        $plain_text = '';  //  Menyimpan hasil dekripsi

                        for ($i = 0, $j = 0; $i < $input_length; $i++) { // Perulangan untuk mengiterasi setiap karakter dalam plaintext
                            if ($input[$i] === ' ') {
                                // Jika karakter adalah spasi, abaikan dan lanjutkan ke karakter berikutnya
                                $plain_text .= ' ';
                                continue;
                            }
                            $char_input = ord($input[$i]) - 65; // Konversi karakter dalam plaintext menjadi angka & - 65 untuk menhasilkan nilai dengan rentang 0 - 25
                            $char_key = ord($key[$j % $key_length]) - 65; // Konversi karakter dalam key dan mengulang key jika sudah mencapai panjang penuh
                            $char_plain = ($char_input - $char_key + 26) % 26; // Memperoleh hasil dekripsi dengan mengkurangkan karakter plaintext dan key dan diambil mod 26
                            $plain_text .= chr($char_plain + 65); // Konversi hasil dekripsi dalam bentuk angka menjadi karakter huruf
                            $j++;
                        }

                        return $plain_text;
                    }
                }
                ?>

                <!-- Form  -->
                <form name="skd" method="post">
                    <!-- Label inputan -->
                    <div class="label">
                        <p>Masukan Text </p>
                    </div>
                    <!-- Form input text -->
                    <div class="input-group mb-3">
                        <input type="text" name="plain" class="form-control">
                    </div>
                    <div class="input-group mb-3">
                        <input type="text" name="key" class="form-control" placeholder="Masukkan Kunci">
                    </div>
                    <div class="box-footer">
                        <table class="table table-stripped">
                            <tr>
                                <!-- button enkripsi dan dekripsi -->
                                <td><input class="btn" type="submit" name="enkripsi" value="Enkripsi" style="width: 100%"></td>
                                <td><input class="btn" type="submit" name="dekripsi" value="Dekripsi" style="width: 100%"></td>
                            </tr>
                        </table>
                    </div>
                </form>
            </div>
        </div>
        <!-- Hasil enkripsi/dekripsi -->
        <div class="output">

        </div>
        <div class="card card-outline card-primary">
            <div class="card-output">
                <h4>Output</h4>
                <table>
                    <!-- Menampilkan hasil output dari enkripsi/dekripsi -->
                    <tr>
                        <td> Output yang dihasilkan : </td>
                        <td><b>
                                <?php if (isset($_POST['enkripsi']) && isset($_POST['plain']) && isset($_POST['key'])) {
                                    echo vigenere_encrypt($_POST['plain'], $_POST['key']); //memanggil fungsi enkripsi dan menampilkannya
                                }
                                if (isset($_POST['dekripsi']) && isset($_POST['plain']) && isset($_POST['key'])) {
                                    echo vigenere_decrypt($_POST['plain'], $_POST['key']); //memanggil fungsi dekripsi dan menampilkannya
                                } ?></b></td>
                    </tr>
                    <tr>
                        <!-- menampilkan text yang dimasukkan -->
                        <td>Text yang dimasukkan : </td>
                        <td><b>
                                <?php if (isset($_POST['plain']) && isset($_POST['key'])) {
                                    if (isset($_POST['enkripsi'])) {
                                        echo vigenere_decrypt(vigenere_encrypt($_POST['plain'], $_POST['key']), $_POST['key']); //memanggil fungsi dekripsi yang sebelumnya dienkripsi dan menampilkannya
                                    }
                                    if (isset($_POST['dekripsi'])) {
                                        echo vigenere_encrypt(vigenere_decrypt($_POST['plain'], $_POST['key']), $_POST['key']); //memanggil fungsi enkripsi yang sebelumnya didekripsi dan menampilkannya
                                    }
                                } ?></b></td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
    </form>

    <script>
        $(function() {
            $('.select2').select2()

        })
    </script>
</body>

</html>
<style>
    /* CSS untuk mengatur tampilan elemen-elemen */
    .container {
        width: 40%;
        margin: 87px auto;
    }

    .judul {
        text-align: center;
    }

    .card-body {
        background-color: #CEDEBD;
        padding: 20px;
    }

    .label p {
        font-size: 18px;
    }

    .input-group {
        margin-bottom: 10px;
        /* Jarak bawah antara input teks dan tombol */
    }

    .btn {
        background-color: #435334;
        color: white;
        /* Warna teks tombol */
        border: none;
        width: 100%;
    }

    .output {
        /* Warna latar belakang kotak output */
        padding: 10px;
        margin-top: 40px;
        /* Jarak atas dari kotak output ke elemen sebelumnya */
    }

    .card-output {
        background-color: #9EB384
    }
</style>
