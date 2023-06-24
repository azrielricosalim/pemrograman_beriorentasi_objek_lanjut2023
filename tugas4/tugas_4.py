#NAMA   : Azriel Rico Salim
#NIM    : 210511122
#KELAS  : K1

class Bahan:
    def __init__(self, nama, kuantitas):
        self.nama = nama
        self.kuantitas = kuantitas
    
    def __str__(self):
        return f"{self.kuantitas} {self.nama}"
    
class ProdukMakanan:
    def __init__(self, nama, daftar_bahan):
        self.nama = nama
        self.daftar_bahan = daftar_bahan
    
    def tambah_bahan(self, bahan):
        self.daftar_bahan.append(bahan)
        
    def __str__(self):
        return f"{self.nama} terbuat dari: {', '.join(str(bahan) for bahan in self.daftar_bahan)}"
        
        
bahan1 = Bahan("pecel", "500 gram")
bahan2 = Bahan("Nasi", "1 kilogram")
bahan3 = Bahan("Bawang merah", "100 gram")

nasi_lengko = ProdukMakanan("Nasi lengko", [bahan2, bahan3])
ketoprak = ProdukMakanan("ketoprak", [bahan1, bahan3])

print(nasi_lengko)
print(ketoprak)