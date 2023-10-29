# Membuat list kendaraan
kendaraan1 = [
    {
        "nama": "Avanza",
        "jenis": "Mobil",
        "merk": "Toyota",
        "warna": "Hitam",
        "harga": "200_000_000",
         "jumlah ban": "4"
    },
    {
        "nama": "Ninja 250",
        "jenis": "Motor",
        "merk": "Kawasaki",
        "warna": "Merah",
        "harga": "90_000_000",
        "jumlah ban": "2"
    },
    {
        "nama": "Xenia",
        "jenis": "Mobil",
        "merk": "Daihatsu",
        "warna": "Putih",
        "harga": "250_000_000",
        "jumlah ban": "4"
    },
    {
        "nama": "CBR600RR",
        "jenis": "Motor",
        "merk": "Honda",
        "warna": "Abu-abu",
        "harga": "90_000_000",
        "jumlah ban": "2"
    }
]
kendaraan1.remove("jenis")

# Menampilkan daftar kendaraan
for kend in kendaraan1:
    print("Nama Kendaraan:", kend["nama"])
    print("Jenis Kendaraan:", kend["jenis"])
    print("Merk Kendaraan:", kend["merk"])
    print("warna kendaraan:", kend["warna"])
    print("Harga kendaraan:",kend["harga"])
    print("Jumlah ban kendaraan:",kend["jumlah ban"])
    print(kendaraan1)
    print()

    pesan = """
menu:
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
pilih menu:
"""
pilihan=input(pesan)

match pilihan:
    case "1":
        print("anda memasukan angka 1 untuk menghitung luas persegi")
        sisi=int(input("masukan sisi:"))
        luas=sisi*sisi
        print("luas persegi dengan sisi",sisi,"adalah",luas)
    case "2":
        print("anda memasukan angka 2 untuk menghitung luas lingkaran")
        sisi=int(input("masukan sisi:"))
        luas=sisi*sisi
        print("luas lingkaran dengan sisi",sisi,"adalah",luas)
    case "3":
        print("anda memasukan angka 3 untuk menghitung luas segitiga")
        alas=int(input("masukan alas:"))
        tinggi=int(input("masukan tinggi:"))
        luas=1/2*(alas*tinggi)
        print("luas segitiga dengan alas,tinggi",alas,tinggi,"adalah",luas)
