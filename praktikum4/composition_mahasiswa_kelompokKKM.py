#NAMA   : ALFA RIZKI
#NIM    : 210511167
#KELAS  : K1

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok = None
    
    def gabung_kelompok(self, kelompok):
        self.kelompok = kelompok
        kelompok.tambah_anggota(self)
    
class KelompokKKM:
    def __init__(self, nama):
        self.nama = nama
        self.anggota = []
    
    def tambah_anggota(self, anggota):
        self.anggota.append(anggota)

m1 = Mahasiswa("LUIS", "210511675")
k1 = KelompokKKM("Kelompok 1")
m1.gabung_kelompok(k1)


print(k1.nama)
for anggota in k1.anggota:
    print(anggota.nama)