kendaraan1 = ["Supra Mk2","mobil","toyota","3000"]
print(kendaraan1)

kendaraan1=kendaraan1 + ["Abu-Abu",4,300_000_000]
kendaraan1.remove("mobil")
print(kendaraan1)

pesan = """
menu:
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
pilih menu:
"""
pilihan = input(pesan)

match kendaraan1:
    case "1":
        print