class Transaksi:
    dict_barang = {'mie':3_000, 'telur':30_000,'tepung':30_000,'minyak':30_000,'sirop':15_000,'susu':45_000,'sabun':10_000,'sampo':30_000,'odol':10_000}
    dict_user = {}
    list_murah = ['tisu','uht','wafer']
    total_belanja = 0 #total belanja awal
    total_belanja2 = 0 #total belanja ditambah beli murah
    harga_diskon = 0 #total belanja setelah beli murah dikurangi diskon
       
    def __init__(self,nama_barang='',jumlah_beli=0):
        self.nama_barang = nama_barang
        self.jumlah_beli = jumlah_beli
                 
    def edit_item(self):
        """
        Fungsi untuk melakukan editing pada dict_user.
        Editing dapat berupa menambah key, mengubah value, dan menghapus key-value
        """
        print('------------------------------------------------')
        print('Harap memasukkan nama barang sesuai dengan yang kami tampilkan')
        print('Kemudian masukkan jumlah pembelian anda dalam angka (contoh: 1 atau 5 atau 10)')
        print('Untuk menghapus barang, masukkan nama barang, kemudian masukkan angka 0 pada jumlah pembelian')
        print('Saat sudah selesai berbelanja, anda bisa menekan tombol "-"')
        while True:
            add_item = input('Masukkan nama barang: ')
            if add_item == '-':
                break
            elif add_item in Transaksi.dict_barang:
                Transaksi.total_belanja = 0
                while True:
                    try:
                        jumlah_beli = int(input('Masukkan jumlah pembelian:  '))
                        break
                    except ValueError:
                        print('!! Masukkan jumlah pembelian dengan angka !!')
                if jumlah_beli == '0':
                    Transaksi.dict_user.pop(hapus_item)
                    print(f'{hapus_item} sudah dihapus')
                else:
                    self.jumlah_beli = jumlah_beli
                    self.harga_barang = Transaksi.dict_barang[add_item]
                    self.total_harga = int(self.jumlah_beli) * int(self.harga_barang)
                    self.list_harga = [self.jumlah_beli, self.total_harga]
                    self.dict_beli = {add_item: self.list_harga}
                    Transaksi.dict_user.update(self.dict_beli)
            else:
                print(f'{add_item} tidak ada dalam katalog kami. Mohon masukkan dengan nama barang dengan benar.')

    def diskon(self):
        """
        Fungsi untuk menghitung diskon yang didapatkan dari total_belanja
        """
        self.diskon1 = Transaksi.total_belanja * 0.1
        self.diskon2 = Transaksi.total_belanja * 0.08
        self.diskon3 = Transaksi.total_belanja * 0.05
        if Transaksi.total_belanja >= 500_000:
            Transaksi.harga_diskon += Transaksi.total_belanja - self.diskon1
            print(f'Selamat anda mendapatkan diskon 10% sebesar Rp {self.diskon1}')
            print(f'Total belanja anda adalah Rp {Transaksi.harga_diskon}')
        elif Transaksi.total_belanja >= 300_000:
            Transaksi.harga_diskon += Transaksi.total_belanja - self.diskon2
            print(f'Selamat anda mendapatkan diskon 8% sebesar Rp {self.diskon2}')
            print(f'Total belanja anda adalah Rp {Transaksi.harga_diskon}')
        elif Transaksi.total_belanja >= 200_000:
            Transaksi.harga_diskon += Transaksi.total_belanja - self.diskon3
            print(f'Selamat anda mendapatkan diskon 5% sebesar Rp {self.diskon3}')
            print(f'Total belanja anda adalah Rp {Transaksi.harga_diskon}')
        else:
            Transaksi.harga_diskon += Transaksi.total_belanja
            

    def check_out(self):
        """
        Fungsi untuk melakukan cetak pada dict_user untuk menampilkan
        nama item yang dibeli, jumlah item, dan harga total per item
        """
        while True:
            print('Berikut keranjang belanja anda:')
            print(f'{"Nama barang":<15}{"I":<5}{"Jumlah pembelian":<20}{"I":<5}{"Harga":<5}')
            for key,value in Transaksi.dict_user.items():
                print(f'{key:<15}{"-":<11}{value[0]:<14}{"-":<5}{value[1]:<5}')
            total_harga = sum([val[1] for val in Transaksi.dict_user.values()])
            Transaksi.total_belanja += total_harga
            print(f'Total belanja anda adalah Rp {Transaksi.total_belanja},-')
            print('------------------------------------------------')
            check_question = input('Belanjaan anda sudah sesuai? (y = ya, e=edit, d=delete all): ')
            if check_question.lower() == 'y':
                if Transaksi.total_belanja >= 50000:
                    self.beli_murah()
                break
            elif check_question.lower() == 'e':
                self.edit_item()
            elif check_question.lower() == 'd':
                Transaksi.dict_user.clear()
                Transaksi.total_belanja = 0
                print('Keranjang belanja anda sudah kosong')
                print('Anda ingin belanja lagi?')
                print('------------------------------------------------')
                self.edit_item()
            else:
                print('Masukkan input yang sesuai')
                
    def beli_murah(self):
        print('------------------------------------------------')
        print('Selamat!!! Belanja anda lebih dari Rp 50.000,-')
        print('Anda dapat melakukan pembelian murah untuk 1 item hanya dengan harga Rp 5.000,-')
        print('Silahkan pilih barang di bawah ini')
        print(Transaksi.list_murah)
        beli_murah = input('Masukkan nama item beli murah anda: ')
        if beli_murah == '-':
            pass
        elif beli_murah in Transaksi.list_murah:
            Transaksi.total_belanja += 5000
            print(f'Baik, {beli_murah} sudah ditambahkan ke keranjang belanja anda.')
            print(f'Total belanja anda menjadi Rp {Transaksi.total_belanja},-')
        else:
            print(f'{beli_murah} tidak ada dalam daftar beli murah')

    def member_id (self):
        """
        Fungsi untuk menambahkan jumlah poin pada id member user
        """
        print('------------------------------------------------')
        print('Punya member id? Masukkan member id anda untuk poin belanja!')
        poin_member = input('Masukkan member id anda: ')
        if poin_member == '-':
            pass
        else:
            self.jumlah_poin = int(Transaksi.harga_diskon / 100)
            print(f'Selamat! {self.jumlah_poin} poin sudah dimasukkan ke dalam id {poin_member}')


