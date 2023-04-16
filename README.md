# Super-Kasir
Aplikasi Super Kasir Supermarket untuk melakukan input barang secara mandiri oleh pembeli.

## Tujuan

Program ini berfungsi sebagai self-service sistem pembayaran kasir, dimana user dapat melakukan input secara mandiri berupa: nama barang dan jumlah pembelian. User dapat menambah, menghapus, dan mengubah jumlah pembelian daftar belanja yang sudah mereka masukkan. Program ini juga mempunyai fitur diskon, pembelian barang dengan harga tertentu lebih murah, dan juga sistem poin ke member id user.

## Cara menggunakan program
Download main.py dan ckasir.py ke dalam satu direktori lokal. Kemudian jalankan main.py

## Alur Kode

![flow_chart](https://user-images.githubusercontent.com/130892412/232321179-5b30f869-121d-421d-b5a6-185bf2d2e452.png)

## Function

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

## Hasil Test Case

1. Menambahkan daftar belanja

![main_menu](https://user-images.githubusercontent.com/130892412/232312748-f8ded799-4640-4b9e-a398-a0358b751b84.png)

![input_item](https://user-images.githubusercontent.com/130892412/232312879-db021872-808a-4566-a54d-ea6f1198e923.png)

Ketika input yang dimasukkan user tidak sesuai, akan muncul pesan kesalahan.

2. Menampilkan keranjang belanja

![check_out](https://user-images.githubusercontent.com/130892412/232313023-6100a84c-9a2f-41f2-b149-25b336cebc52.png)

3. Mengubah daftar belanja

![edit_item](https://user-images.githubusercontent.com/130892412/232313085-d9a4b4b1-da9e-48a6-b0a5-25768268f788.png)

4. Menghapus semua daftar belanja

![delete_all](https://user-images.githubusercontent.com/130892412/232313139-c032ec23-80cf-4b1b-b04c-a862f2283912.png)

5. Memasukkan item khusus beli murah

![beli_murah](https://user-images.githubusercontent.com/130892412/232313227-13a68f62-1ff6-4099-8d04-061587359ae0.png)

6. Mendapatkan diskon

![diskon](https://user-images.githubusercontent.com/130892412/232313278-c8e67359-4076-427c-8555-81868a874dfc.png)

7. Mendapatkan poin belanja

![member_id](https://user-images.githubusercontent.com/130892412/232313339-39132f27-cbb2-4f78-95c8-f4a3ed669f33.png)

## Future Works

1. Masukan input dengan nama barang cukup sulit jika variasi nama barang sangat banyak, dan jumlah barang yang dijual supermarket juga banyak. Input sebaiknya menggunakan kode barang, bukan nama barang.

2. Perlu perbaikan pada fitur member id yang masih belum terhubung pada database sistem, sehingga jumlah poin belum terupdate secara otomatis
