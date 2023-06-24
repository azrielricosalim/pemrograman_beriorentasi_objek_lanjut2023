#NAMA   : ALFA RIZKI
#NIM    : 210511167
#KELAS  : K1

class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang
    
    def tulis_jurnal(self, judul, isi):
        jurnal = Jurnal(judul, isi, self)
        return jurnal
    
class Jurnal:
    def __init__(self, judul, isi, penulis):
        self.judul = judul
        self.isi = isi
        self.penulis = penulis

p1 = Peneliti("LUIS", "olahraga")


j1 = p1.tulis_jurnal("metode pelatihan dribble bola basket yang benar ", "pelatihan ini ditujukan untuk menambah ilmu sekaligus mengoreksi")


print(j1.judul)
print(j1.penulis.nama)