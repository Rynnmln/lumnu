# Program Diskon Tambahan
kaos = 50000
kemeja = 100000
batik = 150000

print("""List Pakaian
[1] Kaos Polos: Rp. 50.000
[2] Kemeja    : Rp. 100.000
[3] Batik     : Rp. 150.000
=================================================
Diskon 10% dengan total belanja Rp. 300.000
Diskon 20% dengan total belanja Rp. 1.000.000
Diskon 40% dengan total belanja Rp. 2.500.000""")
produk = input("Pilih barang yang ingin dibeli: ")
print("=================================================")
if produk == "1":
    print("Kaos Polos: Rp. 50.000")
    jumlah = int(input("Jumlah yang ingin dibeli: "))
    print("=================================================")
    harga = kaos * jumlah
    if harga >= 2500000:
        diskon = harga - (harga * 2 / 5)
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 40%
Pembayaran Rp.""" + str(diskon))
    elif harga >= 1000000:
        diskon = harga - (harga / 5)            
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 20%
Pembayaran Rp.""" + str(diskon))
    elif harga >= 300000:
        diskon = harga - (harga / 10)
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 10%
Pembayaran Rp.""" + str(diskon))
    else:
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 0%
Pembayaran Rp.""" + str(harga))
        
elif produk == "2":
    print("Kemeja: Rp. 100.000")
    jumlah = int(input("Jumlah yang ingin dibeli: "))
    print("=================================================")
    harga = kemeja * jumlah
    if harga >= 2500000:
        diskon = harga - (harga * 2 / 5)
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 40%
Pembayaran Rp.""" + str(diskon))
    elif harga >= 1000000:
        diskon = harga - (harga / 5)
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 20%
Pembayaran Rp.""" + str(diskon))
    elif harga >= 300000:
        diskon = harga - (harga / 10)
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 10%
Pembayaran Rp.""" + str(diskon))
    else:
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 0%
Pembayaran Rp.""" + str(harga))
        
elif produk == "3":
    print("Batik: Rp. 150.000")
    jumlah = int(input("Jumlah yang ingin dibeli: "))
    print("=================================================")
    harga = batik * jumlah
    if harga >= 2500000:
        diskon = harga - (harga * 2 / 5)
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 40%
Pembayaran Rp.""" + str(diskon))
    elif harga >= 1000000:
        diskon = harga - (harga / 5)
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 20%
Pembayaran Rp.""" + str(diskon))
    elif harga >= 300000:
        diskon = harga - (harga / 10)
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 10%
Pembayaran Rp.""" + str(diskon))
    else:
        print("Total belanja: Rp." + str(harga))
        print("""Diskon: 0%
Pembayaran Rp.""" + str(harga))
        
else:
    print("Pembelian dibatalkan.")