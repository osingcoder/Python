bnykBil = int(input('Masukkan angka untuk dicek: '))
Awal = 1
Simpan = 0
Total = 0
while Total<bnykBil:
    Total = Awal + Simpan
    Awal = Simpan
    Simpan = Total
if bnykBil==Total:
    print(bnykBil, 'merupakan bilangan fibonacci')
    print('bilangan fibonacci sebelumnya adalah ', Awal)
    print('bilangan fibonacci sesudahnya adalah ', Awal+Total)
else:
    print(bnykBil, 'bukan bilangan fibonacci')
