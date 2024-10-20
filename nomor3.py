# Program pengelolaan barang berdasarkan jumlah stok
harga_air = 5000
stok_air = 8
harga_tissue = 9800
stok_tissue = 2
harga_mie = 2200
stok_mie = 9

print("Produk Tersedia:")
print("001. Air Mineral: Rp.5000")
print("002. Tissue     : Rp.9800")
print("003. Mie Instan : Rp.2200")
produk = (input("Input kode produk yang ingin dibeli: "))

if produk == "001":
    print("Stok Tersedia: ", stok_air)
    print("Harga Rp.",harga_air)
    nominal_air = int(input("Nominal yang ingin dibeli: "))
    if nominal_air > 8:
         print("Stok tidak cukup.") 
    elif nominal_air <= 0:
        print("Pembelian Gagal.")
    elif nominal_air <= 8 :
        harga_total = harga_air * nominal_air
        all = "Produk: Air Mineral, " + str(nominal_air) + ", Harga: Rp."+str(harga_air) + ", Total: Rp." + str(harga_total)
        print(all)

elif produk == "002":
    print("Stok Tersedia: ", stok_tissue)
    print("Harga Rp.",harga_tissue)
    nominal_tissue = int(input("Nominal yang ingin dibeli: "))
    if nominal_tissue > 2:
         print("Stok tidak cukup.") 
    elif nominal_tissue <= 0:
        print("Pembelian Gagal.")
    elif nominal_tissue <= 2 :
        harga_total = harga_tissue * nominal_tissue
        all = "Produk: Tissue, " + str(nominal_tissue) + ", Harga: Rp."+str(harga_tissue) + ", Total: Rp." + str(harga_total)
        print(all)

elif produk == "003":
    print("Stok Tersedia: ", stok_mie)
    print("Harga Rp.",harga_mie)
    nominal_mie = int(input("Nominal yang ingin dibeli: "))
    if nominal_mie > 9:
         print("Stok tidak cukup.") 
    elif nominal_mie <= 0:
        print("Pembelian Gagal.")
    elif nominal_mie <= 9 :
        harga_total = harga_mie * nominal_mie
        all = "Produk: Mie Instan, " + str(nominal_mie) + ", Harga: Rp."+str(harga_mie) + ", Total: Rp." + str(harga_total)
        print(all)

else:
    print("Pembelian Gagal.")