# Soal Nomor 4 : Menentukan Karakter Huruf Kapital, Huruf Kecil, dan Angka
print('Pengujian jenis karakter')
print('------------------------')
Karakter = (input('Karakter = '))

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'F', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'f', 'w', 'x', 'y', 'z']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]

kapital = Karakter in uppercase
kecil = Karakter in lowercase
angka = Karakter in digit

print('Huruf kapital?', kapital)
print('Huruf kecil?', kecil)
print('Angka?', angka)