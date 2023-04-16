import ckasir

from ckasir import *

print_pattern = ('------------------------------------------------')

print(print_pattern)
print('Selamat datang di LayanLain Store')
print(print_pattern)
print('Anda dapat memasukkan barang-barang yang ingin anda beli pada program ini')
print('Berikut adalah daftar barang-barang di toko kami')
user1 = Transaksi()
for key,value in Transaksi.dict_barang.items():
    print(f'{key:<10}{"-":<5}{"Rp ":<1}{value}')
print('')
print('Pssssttt... ada diskon hingga 10 % untuk total belanja yang Anda beli lho...')
print(print_pattern)
user1.edit_item()
print(print_pattern)
user1.check_out()
print(print_pattern)
user1.diskon()
user1.member_id()
print(print_pattern)
print('Silakan lanjutkan ke pembayaran')
print(print_pattern)
exit_input = input('Silahkan ketik "exit" untuk keluar dari program: ')
