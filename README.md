# Super-Kasir
Aplikasi Super Kasir Supermarket untuk melakukan input barang secara mandiri oleh pembeli.

Tujuan

Program ini berfungsi sebagai self-service sistem pembayaran kasir, dimana user dapat melakukan input secara mandiri berupa: nama barang dan jumlah pembelian. User dapat menambah, menghapus, dan mengubah jumlah pembelian daftar belanja yang sudah mereka masukkan. Program ini juga mempunyai fitur diskon, pembelian barang dengan harga tertentu lebih murah, dan juga sistem poin ke member id user.

Alur Kode


Function

Ada 5 function di module ckasir.py:
1. edit_item

Fungsi ini digunakan untuk mengubah dictionary user. Dictionary user bisa diibaratkan sebagai 'keranjang belanja'. Key pada dictionary ini berupa item nama_barang (sesuai key pada dictionary toko berupa nama barang yang dijual), dan value berupa list yang berisi 2 item, yaitu [jumlah pembelian, harga pembelian].

2. check_out

Fungsi ini untuk melakukan cetak keranjang belanja atau dictionary user, dengan menampilkan nama barang yang dibeli, jumlah pembelian, dan harga pembelian. Di baris akhir akan ada total harga pembelian yang dibayar oleh user.

3. beli_murah

Fungsi ini hanya akan dipanggil pada kondisi tertentu, jika total pembelian oleh user mencapai batas tertentu. Pada fungsi ini, user diperbolehkan memilih salah satu barang dari list dengan harga yang lebih murah dari harga biasa. Harga ini kemudian akan ditambahkan ke harga total belanja user.

4. diskon

Fungsi ini dipanggil setelah beli murah. Fungsi diskon akan mengurangi total belanja user sesuai persyaratan. 

5. member_id

Pada fungsi ini, user dapat memasukkan member id pada Supermarket. User akan mendapatkan poin sesuai dengan total belanja yang akan diakumulasikan pada member id.

Hasil Test Case

1. Menambahkan daftar belanja

foto layar awal

foto input barang

2. Menampilkan keranjang belanja

foto check_out

3. Mengubah daftar belanja

foto edit

4. Menghapus semua daftar belanja

5. Memasukkan item khusus beli murah

6. Mendapatkan diskon

7. Mendapatkan poin belanja
