class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bergerak(self):
        print(self.nama, "Lompat")

class Kucing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu

    def bersuara(self):
        print("cicit cicit!")

kucing = Kucing("UDIN", 1, "JAGABAYAN")
kucing.bergerak() 
kucing.bersuara()  