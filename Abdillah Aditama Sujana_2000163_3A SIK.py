class perahu:
    def __init__ (self, cc, warna, tahun, nama, ukuran):
        self.cc     = cc
        self.warna  = warna
        self.tahun  = tahun
        self.nama   = nama
        self.ukuran = ukuran
    
    def printname(self):
        print(self.cc)
        print(self.warna)
        print(self.tahun)
        print(self.nama)
        print(self.ukuran)

class Rawai(perahu):
    def __init__(self, cc, warna, tahun, nama, ukuran):
        perahu.__init__(self, cc, warna, tahun, nama,  ukuran)
        self.bahanbakar = "Pertamax"

    def PerRawai(self):
        print("Bahan bakar : ", self.bahanbakar)
        print("CC          : ", self.cc)
        print("Warna       : ", self.warna)
        print("Tahun       : ", self.tahun)
        print("Nama        : ", self.nama)
        print("Merk        : ", self.ukuran)

class Jukung(perahu):
    def __init__(self, cc, warna, tahun, nama, ukuran):
        perahu.__init__(self, cc, warna, tahun, nama, ukuran)
        self.bahanbakar = "Pertalite"

    def PerJukung(self):
        print("Bahan Bakar  : ", self.bahanbakar)
        print("CC           : ", self.cc)
        print("Warna        : ", self.warna)
        print("Tahun        : ", self.tahun)
        print("Nama         : ", self.nama)
        print("Merk         : ", self.ukuran)

x = Rawai("150cc", "Merah", 2018, "Rawai", "Honda")
y = Jukung("250cc", "Hitam", 2015, "Jukung", "Yamaha")

x.PerRawai()
y.PerJukung()


